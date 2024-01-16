import random
import string

# Inisiasikan daftar untuk menyimpan akun
accounts = []


def create_account():  # Fungsi untuk membuat akun
    balance = 0
    name = input("Masukkan Nama Pengguna : ").capitalize()
    account_number = str(random.randint(10000, 99999))

    password_length = 6
    password_char = string.ascii_uppercase + string.digits
    password = ''.join(random.choice(password_char)
                       for _ in range(password_length))

    account = {
        "name": name,
        "account_number": account_number,
        "password": password,
        "balance": balance
    }
    accounts.append(account)
    print(f"""
    Akun Berhasil Dibuat!
    Nomor Akun Anda Adalah : {account_number}
    Password Akun Anda Adalah : {password}
    """)
    print("=" * 50)


def deposit(account):  # Fungsi untuk menyetor uang
    while True:
        try:
            amount = float(input("Masukkan Jumlah Setoran : Rp. "))
            account["balance"] += amount
            print("Setoran Berhasil.")
            print(f"Saldo Terkini : Rp. {account['balance']}")
            print("=" * 50)
            break
        except ValueError:
            print('Jumlah Setoran Tidak Valid.')


def withdraw(account):  # Fungsi untuk menarik uang
    while True:
        try:
            amount = float(input("Masukkan Jumlah Penarikkan : Rp. "))
            if account["balance"] >= amount:
                account["balance"] -= amount
                print("Penarikkan Berhasil.")
                print(f"Saldo Terkini : Rp. {account['balance']}")
                print("=" * 50)
                break
            else:
                print("Saldo Tidak Mencukupi.")
        except ValueError:
            print('Jumlah Penarikan Tidak Valid.')


def print_book(account):  # Fungsi untuk mencetak buku rek
    print("Data Akun :")
    print("Nama Nasabah : ", account["name"])
    print("Nomor Akun   : ", account['account_number'])
    print("Saldo        : ", account['balance'])
    print("="*50)


def login():  # Fungsi untuk log in
    while True:
        account_number = input("Masukkan Nomor Akun : ")
        akun_ada = next(
            (account for account in accounts if account["account_number"] == account_number), None)

        if akun_ada:
            while True:
                password = input("Masukkan Password : ").upper()
                if akun_ada["password"] == password:
                    print("Anda Berhasil Masuk.")
                    print("=" * 50)
                    return akun_ada  # Mengembalikan akun yang berhasil login
                else:
                    print("Maaf, Password Yang Anda Masukkan Salah.")

        else:
            print("Maaf, Nomor Akun Tidak Tersedia.")


def opsi(account):  # fungsi sebagai menu setelah log in
    print(f"Hai {account['name']}")
    while True:
        print("Silahkan Pilih Opsi Layanan Kami!")
        print("1. Setor")
        print("2. Tarik")
        print("3. Cetak Buku")
        print("4. Log out")
        print("=" * 50)
        pilihan = (input(">>> "))

        if pilihan == '1':
            deposit(account)

        elif pilihan == '2':
            withdraw(account)

        elif pilihan == '3':
            print_book(account)

        elif pilihan == '4':
            print('Kembali ke menu utama')
            return
        else:
            print("Maaf, Opsi Yang Anda Pilih Tidak Tersedia Dilayanan Kami.")


# program utama
while True:
    print("=" * 50)
    print(" " * 16, "---SISTEM BANK---")
    print("=" * 50)

    print("""
Silahkan Pilih Opsi Layanan : 
1. Daftar
2. Log in
3. Keluar""")
    print("=" * 50)
    choice = (input(">>> "))
    print("")
    if choice == '1':
        create_account()

    elif choice == '2':
        account = login()
        opsi(account)

    elif choice == '3':
        print("Terima Kasih Telah Menggunakan Layanan Kami.")
        break
    else:
        print("Maaf, Opsi Yang Anda Pilih Tidak Tersedia Dilayanan Kami.")
