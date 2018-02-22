import socket

# Inisiasi objek socket IPv4/UDP
udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Aktifkan opsi broadcast
udp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# Bind/ikat server di alamat IP dan port tertentu
udp_sock.bind( ("0.0.0.0", 6666) )
while True :
    # Terima data dari client
    data, client_addr = udp_sock.recvfrom(1000)
    # Konversi dari bytes jadi string
    data = data.decode('ascii')
    print(data)
    # Olah string
    data = "OK "+data
    # Kirim balik ke client
    udp_sock.sendto( data.encode('ascii'), client_addr)

