import socket
from fungsi import send_size, recv_size

# Inisiasi variabel socket
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind ke IP dan port tertentu
tcp_sock.bind( ("0.0.0.0", 6667) )
# Listen 100 permintaan koneksi
tcp_sock.listen(100)

while True :
    # Terima permintaan koneksi dari client
    conn, client_addr = tcp_sock.accept()
    # Terima data dari client
    data = recv_size(conn)
    data = "OK "+data
    # Kirim balik ke client
    send_size(conn, data)
    # Tutup koneksi ke client
    #conn.close()