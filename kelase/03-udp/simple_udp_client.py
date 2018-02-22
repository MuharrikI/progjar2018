import socket

udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Inisiasi variabel data dan address
data = "Selamat pagi"
server_addr = ("127.0.0.1", 6666)
# Kirim data ke server
udp_sock.sendto(data.encode('ascii'), server_addr)
# Baca data yang dikembalikan server
data = udp_sock.recv(1000)
data = data.decode('ascii')
print(data)