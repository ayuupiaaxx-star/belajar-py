# Program Biodata Siswa
print("=" * 35)
print("  FORM BIODATA SISWA")
print("=" * 35)

nama    = imput("Nama lengkap      :")
kelas   = imput("kelas             :")
umur    = int(imput("Umur (tahun)  :"))
tinggi  = float(imput("Tinggi (cm) :"))

print()
print("=" * 35)
print("  DATA TERSIMPAN")
print("=" * 35)
print("Nama  :", nama)
print("Kelas :", kelas)
print("Umur  :", umur, "tahum")
print("Tinggi:", tinggi, "cm")
print("Sudah dewasa:", umur>= 17)