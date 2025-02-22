import psutil

def get_open_ports():
    open_ports = set()  # Tekrarlanan çıktıları engellemek için "set" yapısı kullanıldı.
    try:
        # Tüm ağ bağlantılarını al.
        for conn in psutil.net_connections(kind='inet'):
            # Yalnızca 'LISTEN' durumundaki bağlantıları al.
            if conn.status == psutil.CONN_LISTEN:
                open_ports.add(conn.laddr.port)  # Set'e ekle.
    except psutil.AccessDenied:
        print("Erişim engellendi! Yönetici yetkileri gerekli olabilir.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
    
    return open_ports

if __name__ == "__main__":
    ports = get_open_ports()
    if ports:
        print("Açık portlar:")
        for port in sorted(ports):  # Port numaralarını küçükten büyüğe doğru yansıt.
            print(port)
    else:
        print("Açık port bulunamadı.")
