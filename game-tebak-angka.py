# TEBAK ANGKA
print("TEBAK TEBAKAN ANGKA\n")

# angka yang harus di tebak
angka_tebakan = 7

# inputan user untuk menebak angka dan rules
print("Maksimal penebakan angka hanya 8 kali")
inputUser = int(input("Masukan tebakan angka untuk mendapatkan hasil yang benar = "))
kesempatan_nebak = 1

# sistem penebak angka
while inputUser != angka_tebakan and kesempatan_nebak < 8:
    if inputUser == angka_tebakan:
        print(f"Angka yang anda pilih adalah = {inputUser}")
        print("Selamat tebakan tepat!!")
        

    elif inputUser > angka_tebakan:
        print("\n")
        print(f"Angka yang anda pilih adalah = {inputUser}")
        print("Waduhh, coba pilih angka lebih rendah")
        inputUser = int(input("Masukan tebakan angka untuk mendapatkan hasil yang benar = "))
        kesempatan_nebak += 1

    elif inputUser < angka_tebakan:
        print("\n")
        print(f"Angka yang anda pilih adalah = {inputUser}")    
        print("Hampir, coba pilih angka lebih tinggi")
        inputUser = int(input("Masukan tebakan angka untuk mendapatkan hasil yang benar = "))
        kesempatan_nebak += 1

# untuk memberi hasil akhir
print("\n")
print("Game Selesai")
if angka_tebakan == inputUser:
    print("Selamat Tebakan anda tepat!!")

else:
    print("Kesempatan habis, anda gagal")
