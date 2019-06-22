# FINAL PROJECT Q2 - GOJEK
# Generation Girl Summer Club 2019 - Computer Science 101 - Bahasa Class
# Mentors: (1) Intan Fadilla Andyani (2) Fathinah Asma Izzati

# Developer 1:
# Developer 2:

# Deklarasi variabel 
# variabel 'app' adalah sebuah variabel boolean, sebagai pengukur kapan program berhenti.
app = True

# var total = total go-points yang didapatkan user.
total = 0

# var history = sebuah list untuk menyimpan riwayat go-points user.
history = []

# Tampilan awal saat program dijalankan
print("========================================GOJEK=========================================")
print("[Sign Up]")

# variabel 'name' menerima input user berupa string nama user. Gunakan built-in input!
name = ...... # Ex: "Nama >>> "

# Setelah user menginput namanya, berikan ucapan selamat datang. Gunakan built-in print format!
print(......) # Ex: "Halo, [nama]! Selamat datang di GOJEK!"


# Selama 'app' bernilai True, maka program tidak akan berhenti sampai user memilih menu 'e' (Exit)
while (app == True):
    print("========================================GOJEK=========================================")
    print("Menu")
    print("(a) Transaksi  ||  (b) Cek Poin  ||  (c) Penukaran Poin  ||  (d) Riwayat  ||  (e) Exit")

    # variabel 'action' menerima input user berupa sebuah huruf antara a sampai e untuk mendapatkan menu apa yang dipilih user
    # Gunakan built-in input!
    action = ...... # Ex: '>>> '

    # Conditional Logic Menu yang dipilih user
    # Jika user memilih menu (a)
    if (action == 'a'):
        print("1. Go Ride")
        print("2. Go Car")
        print("3. Go Food")

        # variable transaksi menerima input berupa INTEGER, transaksi nomor berapa yang dipilih user.
        # Gunakan built-in input! Jangan lupa casting ke integer yaa ;)
        transaksi = ...... # Ex: "Transaksi yang dilakukan (1/2/3) >>> ""

        # Conditional Logic transaksi yang dipilih user
        # Jika user memilih transaksi no. 1, maka mendapat go-point sebesar 100 poin. Dst.
        # Jangan lupa tambahkan ke [history] setiap user melakukan transaksi! Gunakan method [list].append(object)!
        if ( transaksi == 1):
            go_points = 100
            history.append(......) # Expected: "100 poin dari GO-RIDE"

        elif(......):
            go_points = ......
            ...... # history append. Expected: "200 poin dari GO-CAR"

        elif(......):
            ......
            ......

        # <code-block di luar Conditional Logic transaksi user>  
        # Cetak "Selamat! Anda mendapatkan Go-Points sebanyak [go_points] points!" ---- bisa gunakan built-in print format.
        
        # Setiap selesai transaksi, jangan lupa jumlahkan poin yang didapat user!;)
        total = ......
        

    # kembali ke Conditional Logic Menu yang dipilih user
    # Jika user memilih menu (b), cetak "Total Go-Points anda adalah [total] poin."
    elif (......):
        ......

    # Jika user memilih menu (c), tampilkan LIST item yang bisa ditukarkan. Gunakan Dictionary ;)
    elif (......):
        items = {......}

        # print list merch
        for ......,...... in ......items():
            print(......) # Ex: Sticker : 100 poin

        # user input merch yang mau ditukarkan, masukkan ke variabel 'merch'. Gunakan built-in input!
        merch = ...... # Ex: 'Merch yang mau ditukarkan >>>> '

        # Conditional Logic. Cek apakah poin yang dimiliki user cukup untuk ditukarkan dengan merch yang dipilih
        # Jika cukup, print 'Selamat! Barang akan dikirim ke alamat anda! ;)
            # Jangan lupa untuk mengurangi total poin jika berhasil ditukarkan
        # Jika tidak cukup, print 'Maaf, Go-Pointsmu tidak mencukupi :(
            
        if (total >= items[merch]):
            ...... # print jika barang berhasil ditukarkan
            ...... # kurangi total poin
            ...... # Jangan lupa untuk menambahkan transaksi penukaran poin ke [history]!
                   # Ex: "100 poin dipakai untuk penukaran merch". Gunakan method list append dan built-in print format!
        else:
            ...... # print jika poin tidak mencukupi

    # Jika user memilih menu (d) Riwayat, tampilkan list riwayat transaksi user.
    elif (......):
        # Jika belum melakukan transaksi apapun (list masih kosong), print "Anda belum melakukan transaksi apapun"
        if (......):
            ......
        else: # Print list riwayat transaksi
            for ...... in ......:
                ......

    # Jika user memilih menu (e) Exit, maka print "See Ya!" kemudian program berhenti berjalan ;)
    elif (......):
        ......
        print("================================Thanks For Using GOJEK!================================")
        app = ...... 


# Template by: Intan Fadilla Andyani