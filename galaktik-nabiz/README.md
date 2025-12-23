# Galaktik Nabız - G-MODE

![G-MODE](https://img.shields.io/badge/G--MODE-NABIZ-a8d8ff?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.6+-blue?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**Galaktik Nabız**, interaktif görsel ve ses efektleriyle çalışan bir nabız (pulse) görselleştirme sistemidir. Warp core animasyonları, dinamik ses sentezi ve modern UI tasarımıyla kullanıcıya sürükleyici bir deneyim sunar.

## 📁 Proje Yapısı

```
galaktik-nabiz/
│
├─ index.html        ← NABIZ (görsel + ses)
│
├─ live/
│   └─ gmode_live.py ← SAHNE MOTORU
│
├─ lab/
│   └─ gmode_lab.py  ← DENE / OYNA
│
└─ README.md
```

## 🚀 Hızlı Başlangıç

### 1. NABIZ Görselleştirme (index.html)

Tarayıcıda doğrudan açın:

```bash
# Dosyayı tarayıcıda aç
open index.html
# veya
xdg-open index.html
```

**Özellikler:**
- ✨ Warp core spiral animasyonu
- 🔊 Dinamik ses sentezi
- 🎮 Interaktif kontroller
- 📊 Sistem paneli ve durum göstergeleri
- 🌊 Pulse (nabız) efektleri

### 2. LIVE Mod - Sahne Motoru

Canlı performans ve sunum için HTTP sunucu:

```bash
cd galaktik-nabiz/live
python3 gmode_live.py
```

**Parametreler:**
```bash
python3 gmode_live.py --port 8000        # Özel port
python3 gmode_live.py --no-browser       # Tarayıcıyı açma
```

**Kullanım Alanları:**
- 🎭 Canlı performanslar
- 🎪 Sahne gösterileri
- 🎬 Medya sunumları
- 🎨 Sanat enstalasyonları

### 3. LAB Mod - Deney ve Test

Deneysel özellikler ve geliştirme için:

```bash
cd galaktik-nabiz/lab
python3 gmode_lab.py
```

**Parametreler:**
```bash
python3 gmode_lab.py --port 8080         # Özel port (varsayılan: 8080)
python3 gmode_lab.py --experiments       # Deney parametrelerini göster
python3 gmode_lab.py --no-browser        # Tarayıcıyı açma
```

**Lab Özellikleri:**
- 🔬 CSS değişkenleri ile deneyler
- 🎨 Renk şemaları testi
- ⚡ Animasyon hızı ayarları
- 🎵 Ses frekansı deneyleri
- 📈 Performance monitoring

## 🎮 Kullanım

### Temel Kontroller

1. **G • AKTİF ET** butonuna tıklayın
2. Sistem başlatma sekansı izleyin
3. NABIZ efektlerini deneyimleyin
4. Tekrar tıklayarak kapatın

### Durum Modları

| Mod | Açıklama | Görsel Efekt |
|-----|----------|--------------|
| **STANDBY** | Bekleme modu | Düşük parlaklık, yavaş animasyon |
| **BOOTING** | Başlatma | Mavi ton, sistem mesajları |
| **ACTIVE** | Aktif mod | Tam parlaklık, pulse efektleri |
| **SHUTTING DOWN** | Kapanma | Gri ton, fade out |

### Sistem Paneli

- 🔊 **Audio Level**: Ses seviyesi (MID/LOW/HIGH)
- 🌊 **Pulse Sync**: Nabız senkronizasyonu
- 🔄 **Color Invert**: Renk inversiyon modu
- ⚡ **Spiral Velocity**: Spiral dönüş hızı
- ⭕ **Warp Stability**: Warp çekirdek stabilitesi

## 🛠️ Geliştirme

### Tarayıcı Console'da Deneyler

```javascript
// CSS değişkenlerini değiştir
document.documentElement.style.setProperty('--speed', '1s');
document.documentElement.style.setProperty('--glow', '1');

// Sınıf değiştir
const app = document.querySelector('.app');
app.classList.add('pulse-active');
app.classList.remove('standby');

// Animasyon kontrolü
const spiral = document.querySelector('.spiral');
spiral.style.animationDuration = '5s';
```

### Özelleştirme

**Renk Şeması:**
- Primary: `#a8d8ff` (Açık mavi)
- Secondary: `#5b4fff` (Mor-mavi)
- Background: `#02040a` (Koyu lacivert)

**Animasyon Süreleri:**
- Spiral dönüşü: 18s
- Pulse interval: 2.4s
- Pulse duration: 170ms

## 📋 Sistem Gereksinimleri

### Tarayıcı
- Modern tarayıcı (Chrome, Firefox, Safari, Edge)
- JavaScript enabled
- Web Audio API desteği

### Python (LIVE/LAB modları için)
- Python 3.6+
- Standart kütüphane (http.server, socketserver, webbrowser)

## 🎯 Özellikler

- ✅ Tamamen bağımsız (dependency yok)
- ✅ Responsive tasarım
- ✅ Performanslı animasyonlar
- ✅ Audio API entegrasyonu
- ✅ Modern UI/UX
- ✅ Türkçe arayüz
- ✅ Cross-platform (Python)

## 📝 Lisans

MIT License - Detaylar için LICENSE dosyasına bakın.

## 🙏 Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/yeni-ozellik`)
3. Commit yapın (`git commit -am 'Yeni özellik: X'`)
4. Branch'i push edin (`git push origin feature/yeni-ozellik`)
5. Pull Request açın

## 📞 İletişim

Sorular, öneriler ve geri bildirimler için issue açabilirsiniz.

---

**Control the Flow.** 🌊
