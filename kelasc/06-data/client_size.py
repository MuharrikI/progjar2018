import socket
from fungsi import send_size, recv_size

# Inisiasi objek socket
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Kirim permintaan koneksi ke server
tcp_sock.connect( ("127.0.0.1", 6667) )

# Kirim data
data = "Jurusan Sistem Informasi"
send_size(tcp_sock, data)

# Baca data yang dikirim balik oleh server
data = recv_size(tcp_sock)
print(data)

tcp_sock.close()
