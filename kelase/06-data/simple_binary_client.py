import socket
import struct

# Inisiasi objek socket
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Koneksikan client ke server
tcp_sock.connect( ("127.0.0.1", 6667) )

# Kirim data ke server
data = 5000000
# Pack variabel data sebagai integer little endian
data = struct.pack("<d", data)
tcp_sock.send( data )
# Terima data dari server
data = tcp_sock.recv(100)
data = data.decode('ascii')
print(data)
# Tutup koneksi
tcp_sock.close()
