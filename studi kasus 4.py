Buku = {
    "judul" : "Laskar Pelangi",
    "penulis" : "Andrea Hirata",
    "tahun terbit" : 2005
    }
  

while True:
    print("\n^MENU PENGELOLAAN DATA BUKU^")
    print("1. Menampilkan data buku")
    print("2. Menambahkan data penerbit")
    print("3. Mengubah data penulis")
    print("4. Mengahapus data penerbit")
    print("5. Keluar")

    Pilihan = input("Pilih menu (1-5): ")

    if Pilihan == "1":
      print("\n---Data Buku---")
      print("Judul  :", Buku["judul"])
      print("Penerbit   :", Buku["penulis"])
      print("Tahun terbit :", Buku["tahun terbit"])
    
    elif Pilihan == "2":
        penerbit = input("Masukkan nama penerbit: ")
        Buku["penerbit"] = penerbit
        print("Penerbit berhasil diatambahkan!")

    elif Pilihan == "3":
      penulis_baru = input("Masukkan penulis baru: ")
      Buku["penulis"] = penulis_baru
      print("Data penulis berhasil diperbarui!")

    elif Pilihan == "4":
      if "penerbit" in Buku:
        del Buku["penerbit"]
        print("Data penerbit berhasil di hapus!")

    else:
      Pilihan == "5"
      print("𖹭 Terima Kasih 𖹭")    
      break
    
print("\n---Data Buku Terbaru---")
print(Buku)
      
    





























# laskar pelangi (Andrea Hirata 2005), Bumi Manusia (Pramoedya Ananta Toer 1980), Laut bercerita (Leila S. Chudori 2017)
