import socket
import select

# Inisiasi objek socket TCP/IPv4
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind ke IP dan port tertentu
tcp_sock.bind( ("0.0.0.0", 6667) )
# Listen sebanyak x permintaan koneksi
tcp_sock.listen(100)

list_monitor = [ tcp_sock ]

while True :
    # Cek aktifitas I/O untuk TCP socket dan koneksi
    inputready, outputready, errorready = select.select(list_monitor, [ ], [ ])

    # Iterasi untuk setiap aktifitas input yang siap dibaca
    for conn in inputready:
        # Jika input berhubungan dengan socket TCP, maka accept permintaan handshaking
        if conn == tcp_sock :
            # Terima permintaan koneksi dari client
            conn, client_addr = tcp_sock.accept()
            # Masukkan koneksi yg baru dibuat ke list monitor 
            list_monitor.append(conn)
        # Else, jika aktifitas inputnya berhubungan dengan koneksi
        else:
            try :
                # Terima text dari client
                data = conn.recv(100)
                data = data.decode('ascii')
                data = "OK "+data
                # Kirim balik ke client
                conn.send( data.encode('ascii') )               
            except(socket.error):
                # Tutup koneksi
                conn.close()
                # Hapus koneksi mati dari list monitor
                list_monitor.remove(conn)
                print("Koneksi telah diputus")

    
    