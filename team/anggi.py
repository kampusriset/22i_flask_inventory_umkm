class Programmer:
    def __init__(self, nama: str, nim: str, role: str, proyek: list):
        self.nama = nama
        self.nim = nim
        self.role = role
        self.proyek = proyek

    def tampilkan_perkenalan(self):
        perkenalan = (
            f"Halo, perkenalkan nama saya {self.nama}.\n"
            f"NIM: {self.nim}\n"
            f"Role: {self.role}\n"
            f"\nSaya telah mengerjakan beberapa fitur berikut:\n"
        )
        fitur_list = "\n".join([f"{i+1}. {fitur}" for i, fitur in enumerate(self.proyek)])
        print(perkenalan + fitur_list)


def main():
    anggi = Programmer(
        nama="Anggi Susanati",
        nim="2213010502",
        role="Programmer",
        proyek=["Login", "Register", "Forgot Password", "Basic CRUD"]
    )
    anggi.tampilkan_perkenalan()


if __name__ == "__main__":
    main()
