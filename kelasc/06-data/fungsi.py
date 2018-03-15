import struct

def send_termination(conn, data):
    term_char = "\r\n"
    data = data+term_char
    conn.send( data.encode('ascii') )

def recv_termination(conn):
    # Variabel untu menampung data
    data = ''
    # Iterasi
    while True :
        # Baca data pakai recv()
        buffer = conn.recv(20)
        # Ubah jadi string
        buffer = buffer.decode('ascii')
        # Cek, jika buffer mengandung termination character
        if "\r\n" in buffer :
            # Buang termination character
            data = data.replace("\r\n", "")
            # Tambahkan buffer ke data
            data = data + buffer
            # Return (keluar dari fungsi)
            return data
        # Tambahkan buffer ke data
        data = data + buffer

def send_size(conn, data):
    # Hitung ukuran data
    size = len(data)
    # Pack variabel size
    size = struct.pack("<I", size)
    # Encode data
    data = data.encode('ascii')
    data = size+data
    # Kirim data
    conn.send(data)

def recv_size(conn):
    # Baca ukuran data
    size = conn.recv(4)
    size = struct.unpack("<I", size)[0]
    # Baca data
    data = conn.recv(size)
    # Decode
    data = data.decode('ascii')
    return data
    