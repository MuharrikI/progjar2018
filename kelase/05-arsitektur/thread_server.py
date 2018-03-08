import socket
from threading import Thread

# Inisiasi objek socket TCP/IPv4
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind ke IP dan port tertentu
tcp_sock.bind( ("0.0.0.0", 6667) )
# Listen sebanyak x permintaan koneksi
tcp_sock.listen(100)

def handle_thread(conn):
    while True:
        try :
            # Terima text dari client
            data = conn.recv(100)
            data = data.decode('ascii')
            data = "OK "+data
            # Kirim balik ke client
            conn.send( data.encode('ascii') )  
        except(socket.error):
            # Tutup koneksi
            conn.close()
            print("Koneksi diputus")
            break

while True :
    # Terima permintaan koneksi dari client
    conn, client_addr = tcp_sock.accept()
    # Buat thread baru setiap ada permintaan koneksi
    t=Thread(target=handle_thread, args=(conn,))
    # Start thread
    t.start()
    
    