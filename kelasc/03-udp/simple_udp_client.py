import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Kirim data ke server
data = "Selamat sore"
sock.sendto( data.encode('ascii'), ("127.0.0.1", 6666) )
# Baca dari server
server_data, server_addr = sock.recvfrom(1000)
# Cetak ke layar
print(server_data.decode('ascii'))