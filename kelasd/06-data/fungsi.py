import struct

# Fungsi untuk mengirim data dengan termination character
def send_termination(conn, data):
    # Definisikan termination character
    term_char = "\r\n"
    # Tambahkan termination character pada data yang akan dikirim
    data = data+term_char
    # Encode ascii
    data = data.encode('ascii')
    # Kirim data
    conn.send(data)

def recv_termination(conn):
    data = ''
    while True :
        # Variabel untuk menampung buffer
        buffer = conn.recv(20)
        buffer = buffer.decode('ascii')
        # Jika variabel buffer mengandung termination character, maka...
        if "\r\n" in buffer :
            # Buang termination character dari buffer
            buffer = buffer.replace("\r\n", "")
            # Kita tambahkan buffer yang dibaca ke data
            data = data + buffer
            # Keluar dari fungsi
            return data
        # Tambahkan data dengan buffer yang diterima
        data = data+buffer

# Fungsi untuk kirim data beserta ukurannya 
def send_size(conn, data):
    # Hitung ukuran datanya
    size = len(data)
    # Pack menggunakn struct
    size = struct.pack("<I", size)
    # Encode string data
    data = data.encode('ascii')
    # Tambahkan size ke data
    data = size+data
    # Kirim
    conn.send(data)

# Fungsi untuk menerima data
def recv_size(conn):
    # Baca ukuran datanya
    size = conn.recv(4)
    size = struct.unpack("<I", size)[0]
    # Baca payloadnya
    data = conn.recv(size)
    data = data.decode('ascii')
    # Kembalikan data
    return data 


