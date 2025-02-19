class Programmer:
    def __init__(self, nama, nim, role, fitur):
        self.nama = nama
        self.nim = nim
        self.role = role
        self.fitur = fitur

    def perkenalan(self):
        print(f"Halo, saya {self.nama} ({self.nim}), seorang {self.role}.")
        print("\nFitur yang telah saya kerjakan:")
        for idx, fitur in enumerate(self.fitur, start=1):
            print(f"{idx}. {fitur}")
        print(f"\nTotal fitur yang saya kembangkan: {len(self.fitur)}")

    def motivasi(self):
        print("\nPesan motivasi: 'Jangan pernah berhenti belajar dan teruslah berkembang!'")

if __name__ == "__main__":
    yasir = Programmer(
        nama="YASIR GALUH ADI SAPUTRO",
        nim="2213010482",
        role="Mahasiswa",
        fitur=["Search", "Halaman Navigasi"]
    )
    
    yasir.perkenalan()
    yasir.motivasi()
