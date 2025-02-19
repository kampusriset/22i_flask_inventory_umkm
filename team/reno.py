class bukan_Programmer:
  def __init__(self, nama, nim, kelas, kontribusi):
  self.nama = nama
  self.nim = nim
  self.kelas = kelas
  self.kontribusi = kontribusi

  def perkenalan(nama, nim, kelas, kontribusi):
    print (f"Nama saya {self.nama}, kelas {self.kelas}")
    print (f"NIM saya {self.nim}")
    print (f"kontribusi saya:")
    for k in self.kontribusi:
      print(f"- {k})
    
kontribusi = ["Merubah tampilan menjadi lebih dinamis menggunakan jinja", 
             "CRUD data peminjam"]
mahasiswa = bukan_Programmer("Muh. Reno Afrido. A", 2213010493, "5I", kontribusi)
mahasiswa.perkenalan()               
