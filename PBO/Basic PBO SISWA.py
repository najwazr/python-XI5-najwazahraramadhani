class siswa:
    #class variable
    jumlah_siswa = 0
    #konstruktor
    def __init__(self, nama, kelas, alamat, nilai):
        self.nama = nama
        self.kelas = kelas
        self.alamat = alamat
        self.nilai = nilai
        siswa.jumlah_siswa += 1
    #method
    def viewSiswa(self):
        print("Data Siswa")
        print("Nama:", self.nama)
        print("Kelas:", self.kelas)
        print("Alamat:", self.alamat)
        print("---------------------")

    def viewNilai(self):
        print("Data Nilai")
        print("Nama:", self.nama)
        for nilai in self.nilai:
            print("Nilai:", nilai)
        print("---------------------")

    def viewKeterangan(self):
        print("Keterangan")
        print("Nama:", self.nama)
        print("Kelas:", self.kelas)
        rata = sum(self.nilai)/len(self.nilai)
        print("Rata-rata:", rata)
        if rata >= 75:
            keterangan = "Lulus."
        else:
            keterangan = "Tidak lulus."
        print("Keterangan:", keterangan)
        print("---------------------")

#instansiasi objek
siswa1 = siswa("Finda", "XII MIPA 1", "Magelang", [98, 79, 88, 78])
siswa2 = siswa("Umi", "XII MIPA 2", "Bantul", [92, 76, 58, 74])
siswa3 = siswa("Patrick", "XII MIPA 3", "Bikini Bottom", [80, 48, 72, 60])
#pemanggilan objek siswa 1
siswa1.viewSiswa()
siswa1.viewNilai()
siswa1.viewKeterangan()
#pemanggilan objek siswa 2
siswa2.viewSiswa()
siswa2.viewNilai()
siswa2.viewKeterangan()
#pemanggilan objek siswa 3
siswa3.viewSiswa()
siswa3.viewNilai()
siswa3.viewKeterangan()
print("Jumlah siswa:", siswa.jumlah_siswa)