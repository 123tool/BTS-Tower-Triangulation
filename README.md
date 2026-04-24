## 📍 BTS Tower Triangulation Logic

![Unit](https://img.shields.io/badge/Unit-123Tool%20Intelligence-7000ff?style=for-the-badge)
![Category](https://img.shields.io/badge/Forensics-Geolocation-green?style=for-the-badge)

Alat simulasi pelacakan posisi berdasarkan data koordinat BTS (Base Transceiver Station). Digunakan untuk memahami alur kerja tim forensik digital dalam melacak pergerakan target melalui log seluler.

Tim investigasi biasanya mendapatkan data log dari operator seluler yang berisi daftar koordinat tower (BTS) yang sempat terhubung dengan HP target. Dengan data tersebut, kita bisa melakukan Triangulasi untuk mempersempit area keberadaan target.
​Saya buatkan script Python untuk simulasi pemetaan lokasinya menggunakan library Folium.

Analisis Forensik: Cara Kerjanya?
​Cell ID (BTS): HP kita akan selalu mencari sinyal terkuat. Data tower mana yang terkoneksi dengan HP target dicatat oleh operator beserta kekuatannya.
​Timing Advance (TA): Ini adalah data "jeda waktu" sinyal bolak-balik dari HP ke tower. Dari sini, kita bisa tahu jarak radius HP dari tower tersebut (misal: 1.2km).
​Intersection: Dengan minimal 3 tower (Triangulasi), area pertemuan ketiga radius tersebut adalah posisi paling akurat di mana target berada.

## 🚀 Fitur
- **Multi-Tower Support:** Mensimulasikan data dari 3 tower berbeda.
- **Dynamic Radius:** Menampilkan jangkauan sinyal berdasarkan kekuatan DBm/Jarak.
- **Dark Mode Map:** Visualisasi peta interaktif menggunakan CartoDB Dark Matter.
- **Precise Intersection:** Menghitung estimasi titik tengah keberadaan target.

## 🛠️ Cara Pakai
1. Install requirements: `pip install folium geopy`
2. Jalankan script: `python Triangulation.py`
3. Buka file `spy_e_map.html` di browser laptop Anda.


---
**Developed By:** Rolandino | **Identity:** SPY-E
