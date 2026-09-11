# Program Cek Kondisi Nilai
nama = input("Nama siswa  : ")
nilai = int(input("Nilai ujian : "))
hadir = input("Hadil 80%? (ya/tidak): ")

# Operatorperbandingan 
print()
print("=== HASIL CEK ===")
print("NILAI >= 75 :", nilai >= 75)
print("NILAI >= 90 :", nilai >= 90)
print("NILAI antar 75-89:", nilai >= 75 and nilai <= 89)

# OPerator logika 
hadir_ok = hadir == "ya"
lulus    = nilai >= 75 and hadir_ok
remedial = nilai < 75 or not hadir_ok

print("Lulus        :", lulus)
print("Perlu remedial:", remedial)
