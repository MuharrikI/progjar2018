import socket
from fungsi import send_termination, recv_termination

# Inisiasi objek socket TCP/IPv4
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Inisiasi handshaking
tcp_sock.connect( ("127.0.0.1", 6667) )

# Kirim teks
data = "Jurusan Teknik Informatika (TIF) Fakultas Ilmu Komputer Universitas Brawijaya (FILKOM UB) kembali mengadakan kegiatan audiensi dengan orang tua/wali mahasiswa angkatan 2011/2012 dan mahasiswa Seleksi Alih Program (SAP) 2014/2015 di gedung F FILKOM UB pada hari Sabtu (3-2-2018). Kegiatan tahunan ini dihadiri oleh Ketua Jurusan TIF Tri Astoto Kurniawan, S.T., M.T., Ph.D., seluruh Ketua Program Studi di bawah naungan Jurusan TIF, ketua Unit Jaminan Mutu (UJM) Jurusan, Bagian Kemahasiswaan, serta para undangan. Diadakannya kegiatan ini bertujuan untuk menginformasikan kepada orang tua mahasiswa tentang evaluasi keberhasilan studi menjelang batas masa studi, dan diskusi terkait permasalahan yang sering menghambat mahasiswa serta solusinya. Dalam sambutannya, Tri Astoto menyampaikan bahwa apabila sampai batas maksimal mahasiswa tidak memenuhi syarat keberhasilan studi, maka pihak fakultas akan mengambil jalan terakhir berupa tawaran pengunduran diri bagi mahasiswa yang bersangkutan."
send_termination(tcp_sock, data)

# Baca kembalian dari server
data = recv_termination(tcp_sock)
print(data)
# Tutup koneksi
tcp_sock.close()