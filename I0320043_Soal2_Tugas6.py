data = []
nilai = " "
while nilai != "-":
    nilai = input("Masukkan nilai: ")
    if nilai != "-":
        data.append(int(nilai))
        if nilai == "-":
            break
print("Nilai anda adalah sebagai berikut: ")
print(data)
n = len(data)
rata_rata = sum(data)/n
print(rata_rata)