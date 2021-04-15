class Karyawan:
    jumlah_karyawan = 0

    def __init__(self, nama, gaji, upah, bidang, alamat):
        self.nama = nama
        self.gaji = gaji
        self.upah = upah
        self.bidang = bidang
        self.alamat = alamat
        Karyawan.jumlah_karyawan += 1
    def tampilkan_jumlah(self):
        print("Total karyawan:", Karyawan.jumlah_karyawan)
    def tampilkan_profil(self):
        print("Nama:", self.nama)
        print("Gaji:", self.gaji)
        print("Upah lembur:", self.upah)
        print("Bidang:", self.bidang)
        print("Alamat:", self.alamat)
    def total_gaji(self):
        print("Total gaji:", self.gaji + self.upah)

karyawan1 = Karyawan("Sarah", 1000000, 200000, "Pelayanan", "Sleman")
karyawan2 = Karyawan("Budi", 2000000, 200000, "Marketing", "Yogyakarta")
karyawan3 = Karyawan("Putri", 5000000, 400000, "TI", "Solo")
karyawan4 = Karyawan("Putra", 8000000, 0, "Pengembangan Bisnis", "Yogyakarta")

karyawan1.tampilkan_profil()
karyawan1.total_gaji()
karyawan2.tampilkan_profil()
karyawan2.total_gaji()
karyawan3.tampilkan_profil()
karyawan3.total_gaji()
karyawan4.tampilkan_profil()
karyawan4.total_gaji()
print("Total karyawan:", Karyawan.jumlah_karyawan)