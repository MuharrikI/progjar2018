# Import socket
import socket

# Inisiasi socket TCP/IPv4
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind ke address dan port tertentu
tcp_sock.bind( ('0.0.0.0', 6667) )

# Listen sebanyak 100 permintaan koneksi
tcp_sock.listen(100)

while True :
    # Terima permintaan koneksi
    conn, client_address = tcp_sock.accept()
    # Terima string dari client
    data = conn.recv(100)
    data = data.decode('ascii')
    # Tambah "OK"
    data = "OK "+data
    # Kirim balik ke client
    conn.send(data.encode('ascii'))
    # Tutup koneksi
    #conn.close()