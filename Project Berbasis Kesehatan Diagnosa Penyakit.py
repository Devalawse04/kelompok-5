import os

print("+==========================================================+")
print("|\tSelamat Datang Di Aplikasi Sistem Kesehatan\t   |")
print("|\t\t   Diagnosa Tifus & Covid-19\t\t   |")
print("+==========================================================+")
nama = input("Nama :\t ")
pilihan = input("Hello,"+nama+"\n Apakah Anda Ingin Melakukan Diagnosa ? (Y/N): ")

os.system("cls")

while pilihan == "Y":
  print("\n Apakah Anda Mersakan Gejala Berikut Ini :")
  print("1.Demam / Suhu Badan Tinggi ")
  print("2.Nafsu Makan Berkurang ")
  print("3.Diare ")
  print("4.Kelelahan & Lemas ")
  diag1 = input(" Jawab Y/N : ")

  if diag1 == "Y":
    print("\n Apakah Anda Juga Merasakan Gejala Ini :")
    print("5.Ruam Merah ")
    print("6.Mual Muntah")

    diag2 = input(" Jawab Y/N : ")

    if diag2 == "Y" :
      print("\n Hi, "+nama+" Hasil Awal Diagnosa Kamu Adalah :")
      print(" Gejala Tifus,Segeralah Kedokter !!!")

    elif diag2 == "N":
      print("\n Apakah Anda Juga Mersakan Gejala Berikut Ini :")
      print("1.Demam/Suhu Badan Tinggi")
      print("2.Sakit Kepla")
      print("3.Hilangnya Indra Perasa/Penciuman")
      print("4.Nyeri Tengkorokan ")
      diag3 = input(" Jawab Y/N : ")
