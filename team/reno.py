class BukanProgrammer:
    def __init__(self, nama, nim, kelas, kontribusi):
        self.nama = nama
        self.nim = nim
        self.kelas = kelas
        self.kontribusi = kontribusi

    def perkenalan(self):
        print(f"Nama saya {self.nama}, kelas {self.kelas}")
        print(f"NIM saya {self.nim}")
        print("Kontribusi saya:")
        for k in self.kontribusi:
            print(f"- {k}")

def main():
    kontribusi = [
        "Merubah tampilan menjadi lebih dinamis menggunakan Jinja",
        "CRUD data peminjam"
    ]
    mahasiswa = BukanProgrammer("Muh. Reno Afrido. A", 2213010493, "5I", kontribusi)
    mahasiswa.perkenalan()

if __name__ == '__main__':
    main()
