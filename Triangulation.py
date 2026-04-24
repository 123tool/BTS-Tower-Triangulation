import folium
from folium import plugins
from geopy.distance import geodesic

# --- DATA INTELIJEN (SIMULASI) ---
# Format: [Latitude, Longitude, Jarak Estimasi ke Target (km), Nama Tower]
tower_data = [
    [-7.1234, 112.4567, 1.2, "BTS TOWER 01"],
    [-7.1350, 112.4650, 1.5, "BTS TOWER 02"],
    [-7.1200, 112.4750, 2.0, "BTS TOWER 03"]
]

def calculate_center(towers):
    # Logika sederhana mencari titik tengah dari koordinat BTS
    lat = sum(t[0] for t in towers) / len(towers)
    lon = sum(t[1] for t in towers) / len(towers)
    return [lat, lon]

def generate_map():
    center_loc = calculate_center(tower_data)
    
    # Buat Peta dengan Tema Dark Mode (Hacker Vibes)
    m = folium.Map(location=center_loc, zoom_start=14, tiles='CartoDB dark_matter')

    # Tambahkan Marker untuk setiap Tower
    for t in tower_data:
        # Lokasi Tower
        folium.Marker(
            location=[t[0], t[1]],
            popup=f"{t[3]} (Radius: {t[2]}km)",
            icon=folium.Icon(color='red', icon='signal', prefix='fa')
        ).add_to(m)

        # Radius Sinyal (Triangulation Circle)
        folium.Circle(
            location=[t[0], t[1]],
            radius=t[2] * 1000, # Konversi ke Meter
            color='cyan',
            fill=True,
            fill_opacity=0.1
        ).add_to(m)

    # Titik Estimasi Target (Titik Tengah)
    folium.Marker(
        location=center_loc,
        popup="ESTIMASI POSISI TARGET (SPY-E)",
        icon=folium.Icon(color='green', icon='user', prefix='fa')
    ).add_to(m)

    # Simpan ke HTML
    m.save("spy_e_map.html")
    print(f"\n[+] Peta Berhasil Dibuat: spy_e_map.html")
    print(f"[!] Lokasi Target Terkunci di: {center_loc}")

if __name__ == "__main__":
    generate_map()
