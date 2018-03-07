import socket

# Inisiasi objek socket
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Kirim permintaan koneksi ke server
tcp_sock.connect( ("127.0.0.1", 6667) )

# Kirim data
data = "Selamat Sore"
tcp_sock.send( data.encode('ascii') )

# Baca data yang dikirim balik oleh server
data = tcp_sock.recv(100)
data = data.decode('ascii')
print(data)

# Kirim data
data = "Selamat Sore"
tcp_sock.send( data.encode('ascii') )

# Baca data yang dikirim balik oleh server
data = tcp_sock.recv(100)
data = data.decode('ascii')
print(data)

tcp_sock.close()
