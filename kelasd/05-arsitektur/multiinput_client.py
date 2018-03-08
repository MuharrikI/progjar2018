import socket

# Inisiasi objek socket TCP/IPv4
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Inisiasi handshaking
tcp_sock.connect( ("127.0.0.1", 6667) )

for i in range(0,2):
    # Kirim teks
    data = "Selamat sore"
    tcp_sock.send( data.encode('ascii') )

    # Baca kembalian dari server
    data = tcp_sock.recv(100)
    data = data.decode('ascii')
    print(data)
    
# Tutup koneksi
tcp_sock.close()