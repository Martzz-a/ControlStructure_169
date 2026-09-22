first = float(input("Enter first number: "))
second = float(input("Enter second number: "))
third = float(input("Enter third number: "))

if first > second and first > third:
    print("Angka pertama adalah angka terbesar:", first)
elif second > first and second > third:
    print("Angka kedua adalah angka terbesar:", second)
elif third > first and third > second:
    print("Angka ketiga adalah angka terbesar:", third)
else:
    print("Semua angka sama")