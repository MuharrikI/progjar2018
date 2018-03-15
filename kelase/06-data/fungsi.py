import struct

# Fungsi untuk mengirimkan data dengan metode termination char
def send_termination(conn, data):
    # Definisikan termination character
    term_char = "\r\n"
    # Tambahkan termination character di belakang data
    data = data + term_char
    # Encode
    data = data.encode('ascii')
    # Kirimkan ke receiver
    conn.send(data)

# Fungsi untuk menerima data dengan metode termination char
def recv_termination(conn):
    data = ""
    # Buat iterasi
    while True :
        # Tampung data
        buff = conn.recv(20)
        buff = buff.decode('ascii')
        # Jika data yang dibaca mengandung \r\n
        if "\r\n" in buff :
            # Bersihkan \r\n dari variabel buff
            buff = buff.replace("\r\n", "")
            # Tambahkan ke data
            data = data + buff
            # keluar dari fungsi
            return data
        else :
            # Tambahkan buff ke data
            data = data + buff

# Fungsi kirim data menggunakan ukuran data
def send_size(conn, data):
    # Baca ukuran datanya
    size = len(data)
    # Pack jadi integer unisgned little endian
    size = struct.pack("<I", size)
    # Encode string data
    data = data.encode('ascii')
    # Gabungkan antara header dan payload
    data = size+data
    # Kirim ke receiver
    conn.send(data)

# Fungsi untuk membaca data
def recv_size(conn):
    #Baca ukuran datanya
    size = conn.recv(4)
    size = struct.unpack("<I", size)[0]
    # Baca payloadnya
    data = conn.recv(size)
    data = data.decode('ascii')
    # return
    return data
