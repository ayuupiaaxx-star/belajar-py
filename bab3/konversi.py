# kakulator konversi satuan
print("=== KAKULATOR KONVERSI ===")
cm = float(imput("Masukkan panjang (cm):"))

# konversi ke berbagai satuan 
meter   = cm / 100
km      = cm / 100000
inci    = cm / 2.54
kaki    = inci / 12

print()
print(cm, "cm =", meter, "meter")
print(cm, "cm =", km, "kilometer")
print(cm, "cm =", round(inci, 2), "inci")
print(cm, "c, =", round(kaki, 2), "kaki")