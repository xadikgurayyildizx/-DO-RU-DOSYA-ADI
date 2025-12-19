#!/usr/bin/env python3
"""
G-MODE LAB - DENE / OYNA (Test / Play)
Deneysel modlar ve görsel efektleri test etme alanı
"""

import http.server
import socketserver
import webbrowser
import os
import sys
import errno
from pathlib import Path


class GModeLabHandler(http.server.SimpleHTTPRequestHandler):
    """Lab modu için özel HTTP handler"""
    
    def __init__(self, *args, **kwargs):
        # galaktik-nabiz dizinine geç
        base_path = Path(__file__).parent.parent
        os.chdir(base_path)
        super().__init__(*args, **kwargs)
    
    def log_message(self, format, *args):
        """Log mesajlarını özelleştir"""
        print(f"[LAB] {format % args}")


def print_lab_menu():
    """Lab menüsünü göster"""
    print("\n" + "=" * 60)
    print("G-MODE LAB - DENEY MODU")
    print("=" * 60)
    print("""
    KULLANILABİLİR MODLAR:
    
    1. NABIZ Görselleştirme (index.html)
       - Temel nabız ve ses sistemi
       - Warp core animasyonu
       - Interaktif kontroller
    
    2. Deneysel Modlar
       - Farklı renk şemaları test et
       - Animasyon hızlarını ayarla
       - Ses frekanslarını dene
    
    ÖNERİLER:
    - Tarayıcı Developer Tools (F12) kullan
    - Console'dan parametreleri değiştir
    - Performance tab'ında FPS izle
    """)
    print("=" * 60)


def start_lab_mode(port=8080, auto_open=True):
    """
    Lab modunu başlat
    
    Args:
        port: HTTP sunucu portu (varsayılan: 8080)
        auto_open: Tarayıcıyı otomatik aç (varsayılan: True)
    """
    print_lab_menu()
    print(f"\nPort: {port}")
    print(f"Dizin: {Path(__file__).parent.parent}")
    print("=" * 60)
    
    try:
        with socketserver.TCPServer(("", port), GModeLabHandler) as httpd:
            url = f"http://localhost:{port}/index.html"
            print(f"\n✓ Lab modu çalışıyor: {url}")
            print("✓ CTRL+C ile durdurun")
            print("\n💡 İPUCU: Tarayıcı console'unda deneyler yapabilirsiniz!")
            print("   - app.classList değiştir")
            print("   - CSS değişkenlerini (--speed, --glow) ayarla")
            print("   - Audio context ile oyna\n")
            
            if auto_open:
                print("→ Tarayıcı açılıyor...")
                webbrowser.open(url)
            
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n\n[LAB] Deney tamamlandı, kapatılıyor...")
        sys.exit(0)
    except OSError as e:
        if e.errno == errno.EADDRINUSE:  # Port already in use
            print(f"\n✗ HATA: Port {port} kullanımda!")
            print(f"  Farklı bir port deneyin: python {sys.argv[0]} --port 8081")
        else:
            print(f"\n✗ HATA: {e}")
        sys.exit(1)


def run_experiments():
    """Deneysel parametreleri göster"""
    print("\n" + "=" * 60)
    print("DENEY PARAMETRELERİ")
    print("=" * 60)
    print("""
    CSS Değişkenleri (Tarayıcı Console'da):
    
    document.documentElement.style.setProperty('--speed', '1s');
    document.documentElement.style.setProperty('--glow', '1');
    
    Sınıf Değiştir:
    
    app.classList.add('pulse-active');
    app.classList.remove('standby');
    app.classList.add('active');
    
    Animasyon Test:
    
    - Spiral hızı: .spiral { animation-duration: 5s }
    - Pulse frekansı: setInterval değerini değiştir (2400ms)
    - Renk geçişleri: conic-gradient değerlerini ayarla
    """)
    print("=" * 60 + "\n")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
        description="G-MODE LAB - Deney ve Test Modu",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--port", "-p",
        type=int,
        default=8080,
        help="HTTP sunucu portu (varsayılan: 8080)"
    )
    parser.add_argument(
        "--no-browser",
        action="store_true",
        help="Tarayıcıyı otomatik açma"
    )
    parser.add_argument(
        "--experiments", "-e",
        action="store_true",
        help="Deney parametrelerini göster"
    )
    
    args = parser.parse_args()
    
    if args.experiments:
        run_experiments()
    else:
        start_lab_mode(port=args.port, auto_open=not args.no_browser)
