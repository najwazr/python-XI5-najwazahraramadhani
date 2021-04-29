class Siswa:
    def __init__(self, nis, nama, kelas):
        self.__nis = nis
        self.__nama = nama
        self.__kelas = kelas
    
    #getter
    def getnis(self):
        return self.__nis
    
    #setter
    def setnis(self, newnis):
        self.__nis = newnis

wawan = Siswa(16158, "Najwa Zahra Ramadhani", "XI MIPA 5")

print(wawan.getnis())
wawan.setnis(10000)
print(wawan.getnis())