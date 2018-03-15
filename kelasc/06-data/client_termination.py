import socket
from fungsi import send_termination, recv_termination

# Inisiasi objek socket
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Kirim permintaan koneksi ke server
tcp_sock.connect( ("127.0.0.1", 6667) )

# Kirim data
data = "Jurusan Sistem Informasi (SI) Fakultas Ilmu Komputer, Universitas Brawijaya (FILKOM UB) mengadakan kegiatan audiensi dengan orang tua / wali mahasiswa jurusan SI angkatan 2011 dan 2012 di Fakultas Ilmu Komputer pada Sabtu (24/2). Kegiatan ini bertujuan untuk memberikan informasi dan diskusi kepada orang tua mahasiswa mengenai evaluasi keberhasilan studi mahasiswa menjelang batas maksimal masa studi. Kegiatan yang dipimpin langsung oleh Ketua Jurusan SI, Dr. Eng. Herman Tolle, S.T, M.T ini dihadiri juga oleh seluruh ketua program studi yang berada dibawah Jurusan SI, Ketua UJM Jurusan, Unit Kemahasiswaan, serta para undangan."
send_termination(tcp_sock, data)

# Baca data yang dikirim balik oleh server
data = recv_termination(tcp_sock)
print(data)

tcp_sock.close()
