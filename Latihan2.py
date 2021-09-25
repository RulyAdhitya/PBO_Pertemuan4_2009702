# Membuat Class Mahasiswa Sebagai Child dari Class Manusia

class Manusia:
    def __init__(self, nama_depan, nama_belakang):
        self.firstname = nama_depan
        self.lastname = nama_belakang

    def printname(self):
        print("Nama saya " + self.firstname, self.lastname)


class Mahasiswa(Manusia):
    pass


data = Mahasiswa("Ruly", "Adhitya")
data.printname()
