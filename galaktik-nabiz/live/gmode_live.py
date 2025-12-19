#!/usr/bin/env python3
"""
G-MODE LIVE - SAHNE MOTORU (Stage Engine)
Gerçek zamanlı performans ve sahne kontrolü için motor
"""

import http.server
import socketserver
import webbrowser
import os
import sys
import errno
from pathlib import Path


class GModeStageHandler(http.server.SimpleHTTPRequestHandler):
    """Özel HTTP handler - galaktik-nabiz dizininden servis eder"""
    
    def __init__(self, *args, **kwargs):
        # galaktik-nabiz dizinine geç
        base_path = Path(__file__).parent.parent
        os.chdir(base_path)
        super().__init__(*args, **kwargs)
    
    def log_message(self, format, *args):
        """Log mesajlarını özelleştir"""
        print(f"[STAGE] {format % args}")


def start_stage_engine(port=8000, auto_open=True):
    """
    Sahne motorunu başlat
    
    Args:
        port: HTTP sunucu portu (varsayılan: 8000)
        auto_open: Tarayıcıyı otomatik aç (varsayılan: True)
    """
    print("=" * 60)
    print("G-MODE LIVE - SAHNE MOTORU")
    print("=" * 60)
    print(f"Port: {port}")
    print(f"Dizin: {Path(__file__).parent.parent}")
    print("=" * 60)
    
    try:
        with socketserver.TCPServer(("", port), GModeStageHandler) as httpd:
            url = f"http://localhost:{port}/index.html"
            print(f"\n✓ Sahne motoru çalışıyor: {url}")
            print("✓ CTRL+C ile durdurun\n")
            
            if auto_open:
                print("→ Tarayıcı açılıyor...")
                webbrowser.open(url)
            
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n\n[STAGE] Kapatılıyor...")
        sys.exit(0)
    except OSError as e:
        if e.errno == errno.EADDRINUSE:  # Port already in use
            print(f"\n✗ HATA: Port {port} kullanımda!")
            print(f"  Farklı bir port deneyin: python {sys.argv[0]} --port 8001")
        else:
            print(f"\n✗ HATA: {e}")
        sys.exit(1)


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
        description="G-MODE LIVE - Sahne Motoru",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--port", "-p",
        type=int,
        default=8000,
        help="HTTP sunucu portu (varsayılan: 8000)"
    )
    parser.add_argument(
        "--no-browser",
        action="store_true",
        help="Tarayıcıyı otomatik açma"
    )
    
    args = parser.parse_args()
    start_stage_engine(port=args.port, auto_open=not args.no_browser)
