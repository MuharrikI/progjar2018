import socket

udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Aktifkan opsi broadcast
udp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# Inisiasi variabel data dan address
data = "Selamat pagi"
server_addr = ("10.211.55.255", 6666)
# Kirim data ke server
udp_sock.sendto(data.encode('ascii'), server_addr)
# Baca data yang dikembalikan server
data = udp_sock.recv(1000)
data = data.decode('ascii')
print(data)