#Import lib/API socket
import socket

# Init objek socket utk UDP/IPv4
udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind ke alamat dan port tertentu
udp_sock.bind( ("0.0.0.0", 6666) )

while True :
    # Receive data yang diterima dari client
    data, client_addr = udp_sock.recvfrom(100)
    # Decode dari bytes ke string
    data = data.decode('ascii')
    # Ubah string
    data = "OK "+data
    # Kirim data ke client dengan alamat pada variabel client_addr
    udp_sock.sendto(data.encode('ascii'), client_addr)