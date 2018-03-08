import socket
from threading import Thread

def handle_thread(conn):
    while True :
        try :
            # Terima data dari client
            data = conn.recv(100)
            data = data.decode('ascii')
            data = "OK "+data
            # Kirim balik ke client
            conn.send( data.encode('ascii') )            
        except(socket.error):
            # Tutup koneksi ke client
            conn.close()
            print("Koneksi ditutup client")
            # Keluar di perulangan
            break

# Inisiasi variabel socket
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind ke IP dan port tertentu
tcp_sock.bind( ("0.0.0.0", 6667) )
# Listen 100 permintaan koneksi
tcp_sock.listen(100)

while True :
    # Terima permintaan koneksi dari client
    conn, client_addr = tcp_sock.accept()
    # Buat thread baru untuk setiap koneksi yang diterima
    t=Thread(target=handle_thread, args=(conn,))
    # Jalankan thread tersebut
    t.start()
    