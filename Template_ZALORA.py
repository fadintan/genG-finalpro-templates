'''
FINAL PROJECT Q3 - ZALORA
Generation Girl Summer Club 2019 - Computer Science 101 - Bahasa Class - Week 2
Mentors: (1) Intan Fadilla Andyani (2) Fathinah Asma Izzati

Developer 1:
Developer 2:
# GOODLUCK GIRLS! #

'''

# buat variabel 'barang' yang merupakan dictionary berisi list barang beserta harganya. 
barang = {......}

# Tampilan awal saat program dijalankan
print("================================ZALORA=================================")
print("[Sign Up]")

# Data diri user berupa nama dan tanggal lahir. Gunakan built-in input!
name = ...... # Expected: "Nama Lengkap >>> "
bday = ...... # Expected: "Tanggal Lahir (DD/MM/YY) >>> "

'''
    Ingat! Input user berupa string, sedangkan kita butuh 'bday' sebagai integer untuk cek apakah tanggal lahir
    user adalah bilangan prima atau bukan. Kita harus slice string bday dan mengambil 2 karakter pertama,
    kemudian kita ubah dari string menjadi integer!
    Bagaimana caranya?
'''
bday = ...... # Slicing & Casting bday menjadi integer

'''
    Setelah menerima nama dan bday, berikan ucapan selamat datang di Zalora! ;)
    Expected: "Halo, [name]! Selamat datang di Zalora."
    Hint: Gunakan print format!
'''
print(......) 


# variabel transaksi = jumlah berapa kali user belanja
transaksi = 0
# variabel 'app' adalah sebuah variabel boolean, sebagai pengukur kapan program berhenti.
app = True

# TO DO: Buat function untuk menjumlahkan total harga barang yang dibeli user
def checkOut(stuffs):
    harga = 0 # Di awal, harga masih 0
    ......
    return ......

# TO DO: Buat function untuk mengecek tanggal lahir user adalah prima atau bukan
# Diskusikan logicnya dengan team-mate mu dan jangan malu untuk bertanya pada mentor ;)
def isPrime(bday):
    ......

# Selama 'app' bernilai True, maka program tidak akan berhenti sampai user memilih menu [b] Exit App
while app == True:
    print("================================ZALORA=================================")
    print("Menu")
    print("[a] Belanja  ||  [b] Exit App")

    '''
        Variabel 'action' menerima input user berupa sebuah huruf antara a atau b 
        untuk mendapatkan menu apa yang dipilih user.
        Gunakan built-in input!
    '''
    action = ...... # Expected: ">>> "

    
    ''' 
        Conditional Logic 1 (User memilih menu [a] atau [b])
        1. Saat user memilih menu 'a', maka yang terjadi adalah:
            1. Print daftar barang beserta harganya yang tersedia di Zalora.
                Hint: print key dan value dictionary 'barang' yang telah kamu buat tadi ;)
                ps. Jangan lupa untuk menambahkan 1 transaksi setiap user melakukan transaksi
            2. User input barang apa saja yang akan dibeli. Input tersebut dimasukkan ke dalam 
               variabel 'keranjang'. Gunakan built-in input!
               ps. Input yang diterima dari user berupa string. Kita harus merubahnya menjadi list
               agar bisa diproses saat kita menghitung total harganya ;) gunakan method split()
            3. Sediakan variabel 'harga' yang berisi total harga barang yang user beli.
               Disini kita gunakan function checkOut(stuffs) yang telah kita buat sebelumnya :)
            4. Print list beserta harga barang yang dibeli user (seperti struk belanja)
            5. Cek apakah user masih bisa mendapatkan diskon (jumlah transaksi belum melebihi 3 kali)

                Conditional Logic 2. (Cek apakah user bisa mendapat diskon)
                1. Cek apakah tanggal lahir user adalah bilangan prima
                   Hint. Gunakan function isPrime(bday) yang telah kalian buat ;)

                   Conditional Logic 3. (Cek bday prima atau bukan)
                   1. Jika prima, maka mendapatkan diskon spesial sebesar
                        (bday)% + Rp 30.000
                   2. Jika bukan prima, maka hanya mendapat diskon Rp 30.000

                    <end of Conditional Logic 3>

                2. Jika transaksi user sudah melebihi 3 kali, maka user tidak akan mendapat
                   diskon apapun
                <end of Conditional Logic 2>
            6. Setiap selesai transaksi, user bisa memilih untuk kembali ke menu atau langsung exit app
        
        2. Jika user memilih menu 'b', maka tutup aplikasi.
    '''
    if action == 'a':
        transaksi = ......

        # print daftar harga barang
        for ...., .... in ...... .items():
            print(......) # Ex: "Barang : Rp 000"

        # user input barang yang mau dibeli
        keranjang = ...... # Ex: "Barang yang dibeli: "

        # ubah variabel 'keranjang' string menjadi list
        keranjang = ...... 

        # var. harga memanggil function checkOut untuk hitung harga barang yg dibeli
        harga = ......

        print("=======================================================================")

        # print list barang beserta harga yang dibeli user
        for i in keranjang:
            print(.......) # Expected: "Sepatu : Rp 000"

        # jika jumlah transaksi user masih kurang dari 4 kali, user mendapat diskon
        if (transaksi ......):

            # print total harga sebelum diskon
            print("Total harga: ", harga)
            print("=======================================================================")

            # diskon jika tanggal lahir user adalah bilangan prima, mendapat diskon spesial
            if (isPrime(bday)):
                diskon = ...... # Perhitungan potongan harga
                print("Selamat! Kamu mendapat diskon tambahan spesial! ;)")
                print(......) # Ex: "Kamu mendapat potongan harga [bday]% + Rp 30.000,- " ps. Gunakan print format
                print("Total belanjaanmu sekarang adalah Rp ", ...... ) # Total belanja setelah mendapat diskon
                print("================================ZALORA=================================")

            # tanggal lahir bukan prima, diskon reguler Rp 30.000
            else:
                diskon = ...... # Diskon reguler Rp 30.000
                print("Selamat! Kamu mendapat potongan harga sebesar Rp 30.000,-!")
                print("Total belanjaanmu sekarang adalah Rp ", ......) # Print total belanja setelah mendapat diskon
                print("================================ZALORA=================================")

            # setelah transaksi, user bisa pilih kembali ke menu atau tutup aplikasi
            print("[a] Kembali ke Menu  ||  [b] Exit App")
            action = input(">>> ")

        # jika transaksi sudah lebih dari 3 kali, tidak mendapat diskon apapun
        else:
            print("Total harga: ", ......) # Total belanja user tanpa diskon
            print("================================ZALORA=================================")
            print("[a] Kembali ke Menu  ||  [b] Exit App")
            action = input(">>> ")

    # jika user memilih untuk menutup aplikasi
    if (action ......): # Jika 'action' adalah 'b'
        print("==========================Thanks for shopping!==========================")
        app = .......


# Template by: Intan Fadilla Andyani
