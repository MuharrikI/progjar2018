import socket

udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Tambahkan opsi broadcast
udp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# Inisiasi variabel data dan alamat server
data = "Selamat Pagi"
server_addr = ("10.211.55.255", 6666)
# Kirim ke server
udp_sock.sendto(data.encode('ascii'), server_addr )
# Terima data dari server
data, addr = udp_sock.recvfrom(100)
# Print ke layar
print(data.decode('ascii'))
