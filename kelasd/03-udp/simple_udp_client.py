import socket

udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Inisiasi variabel data dan alamat server
data = "Selamat Pagi"
server_addr = ("127.0.0.1", 6666)
# Kirim ke server
udp_sock.sendto(data.encode('ascii'), server_addr )
# Terima data dari server
data, addr = udp_sock.recvfrom(100)
# Print ke layar
print(data.decode('ascii'))
