#Soal 3
angka_terendah = 10
angka_tertinggi = 25

for bilangan in range(angka_terendah,angka_tertinggi):
    for i in range(2,bilangan-1):
        if (bilangan % i) == 0:
            print(bilangan,'bukan bilangan prima')
            break
    else:
            print(bilangan, 'adalah bilangan prima')

