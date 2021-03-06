import socket
import struct

# Inisiasi objek socket TCP/IPv4
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind ke IP dan port tertentu
tcp_sock.bind( ("0.0.0.0", 6667) )
# Listen sebanyak x permintaan koneksi
tcp_sock.listen(100)

while True :
    # Terima permintaan koneksi dari client
    conn, client_addr = tcp_sock.accept()
    # Terima text dari client
    data = conn.recv(8)
    data = struct.unpack("<d",data)[0]
    # Ubah jadi string
    data = str(data)
    # Kirim balik ke client
    conn.send( data.encode('ascii') )
    # Tutup koneksi
    #conn.close()