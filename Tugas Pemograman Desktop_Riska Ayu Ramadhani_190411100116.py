#no.1
print ("Menghitung rerata nilai")
v=int(input("Masukkan nilai a :"))
w=int(input("Masukkan nilai b :"))
x=int(input("Masukkan nilai c :"))
y=int(input("Masukkan nilai d :"))
z=int(input("Masukkan nilai e :"))
rerata=(v+w+x+y+z)/5
print("reratanya adalah : ", rerata)


#no.2
sisi= int(input ("Masukkan sisi persegi :"))
luas= sisi*sisi
keliling= 4*sisi
print("Luas persegi adalah =", luas)
print("Keliling persegi adalah =", keliling)

#no.3
tinggi=float(input("Masukkan Tinggi Badan:"))
berat=float(input("Masukkan Berat Badan:"))
BMI=berat/(tinggi)**2
print("BMI anda adalah")
if BMI <18.5:
    print("Berat badan anda kurang, mulai makan yang banyak ya")
elif BMI >18.5 and BMI <19:
    print("Berat badan anda normal, pertahankan")
elif BMI >19 and BMI <29:
    print("Berat badan anda berlebih, coba kurangi makan")
elif BMI>30:
    print("Obesitas")

#no.4
print("Mencari Nilai Minimum dan Maksimum")
data = int(input("Masukkan jumlah data:"))
angka=[]
for i in range (data):
    nip=int(input("Masukkan angka:"))
    angka.append(nip)
min=angka[0]
max=angka[len(angka)-1]
for j in angka:
    if min>j:
        min=j
    if max<j:
        max=j
angka.sort()
print("List data", angka)
print("Nilai Maksimum:", max)
print("Nilai Minimum:", min)

print("")
print("")

#no.5
print("Menentukan Validasi username dan password")
username="pemdesk"
password="informatika"
for a in range (3):
    uname=input("Masukkan username:")
    pw=input("Masukkan password:")
    y=3
    if (uname==username) and (pw==password):
        print("Anda berhasil masuk")
        break
    else:
        print("Maaf, username atau password salah. Silahkan coba lagi.")
        continue
print("\n Coba lagi lain kali")
