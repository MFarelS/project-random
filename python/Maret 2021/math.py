try:
    a = int(input("Masukkan nilai A : "))
    b = int(input("Masukkan nilai B : "))
except:
    print("\nInput tidak valid!")
else:
    # penjumlahan
    c = a + b
    print(f"\nHasil {a} + {b} = {c}")
    # pengurangan
    c = a - b
    print(f"Hasil {a} - {b} = {c}")
    # perkalian
    c = a + b
    print(f"Hasil {a} * {b} = {c}")
    # pembagian
    c = a / b
    print(f"Hasil {a} / {b} = {c:.2f}")
    # modulus
    c = a % b
    print(f"Hasil {a} % {b} = {c}")
    # pangkat
    c = a ** b
    print(f"Hasil {a} ** {b} = {c}")
