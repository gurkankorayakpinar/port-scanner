import psutil

def get_open_ports():
    open_ports = set()  # Tekrarlanan portları önlemek için set
    try:
        # Tüm ağ bağlantılarını al
        for conn in psutil.net_connections(kind='inet'):
            # Yalnızca 'LISTEN' durumundaki bağlantıları al
            if conn.status == psutil.CONN_LISTEN:  # 'LISTEN' sabitini kullanmak daha güvenli
                open_ports.add(conn.laddr.port)  # Port'u sete ekle
    except psutil.AccessDenied:
        print("Erişim engellendi! Yönetici yetkileri gerekli olabilir.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
    
    return open_ports

if __name__ == "__main__":
    ports = get_open_ports()
    if ports:
        print("Açık Portlar:")
        for port in sorted(ports):  # Portları sıralı şekilde yazdır
            print(port)
    else:
        print("Açık port bulunamadı.")
