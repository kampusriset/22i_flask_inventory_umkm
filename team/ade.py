class Programmer:
    def __init__(self, nama, nim, role, fitur):
        self.nama = nama
        self.nim = nim
        self.role = role
        self.fitur = fitur

    def perkenalan(self):
        print(f"Halo, perkenalkan nama saya {self.nama}.")
        print(f"NIM: {self.nim}")
        print(f"Role: {self.role}\n")
        print("Saya telah mengerjakan beberapa fitur berikut:")
        for idx, fitur in enumerate(self.fitur, start=1):
            print(f"{idx}. {fitur}")


if __name__ == "__main__":
    ade = Programmer(
        nama="Bayu Ade",
        nim="2213010496",
        role="Programmer",
        fitur=["Landing Page", "Authentication", "Controller"]
    )
    ade.perkenalan()