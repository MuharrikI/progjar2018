# Import socket
import socket
from threading import Thread

# Inisiasi socket TCP/IPv4
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind ke address dan port tertentu
tcp_sock.bind( ('0.0.0.0', 6667) )

# Listen sebanyak 100 permintaan koneksi
tcp_sock.listen(100)

def handle_thread(conn):
    while True :
        try :
            # Terima string dari client
            data = conn.recv(100)
            data = data.decode('ascii')
            # Tambah "OK"
            data = "OK "+data
            # Kirim balik ke client
            conn.send(data.encode('ascii'))            
        except(socket.error):
            print("Koneksi ditutup")
            break
            # Tutup koneksi
            conn.close()

while True :
    # Terima permintaan koneksi
    conn, client_address = tcp_sock.accept()
    # Buat thread baru untuk setiap permintaan koneksi
    t=Thread(target=handle_thread, args=(conn,))
    # Start thread
    t.start()
    