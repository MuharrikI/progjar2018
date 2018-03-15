# Import socket
import socket
import struct

# Inisiasi socket TCP/IPv4
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind ke address dan port tertentu
tcp_sock.bind( ('0.0.0.0', 6667) )

# Listen sebanyak 100 permintaan koneksi
tcp_sock.listen(100)

while True :
    # Terima permintaan koneksi
    conn, client_address = tcp_sock.accept()
    # Terima string dari client
    data = conn.recv(4)
    data = struct.unpack("<I", data)[0]
    data = 20 + data
    # Tambah "OK"
    data = "OK "+str(data)
    # Kirim balik ke client
    conn.send(data.encode('ascii'))
    # Tutup koneksi
    #conn.close()