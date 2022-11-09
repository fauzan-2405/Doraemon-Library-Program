# Doraemon-Library-Program

## Spesifikasi Program
Program ini dapat dianalogikan seperti program library (tetapi diperbagus seperti kantong ajaib doraemon). Program ini awalnya akan meminta user untuk login pada program. Jika user belum memiliki akun, maka user dapat membuat akun baru. Admin dapat menambahkan user baru secara langsung. Informasi tentang akun ini (username dan password) akan tersimpan di file user.csv

### F01 - Register
Pengguna yang belum login ke sistem inventarisasi dapat mendaftar ke sistem. Admin dapat mendaftarkan pengguna baru dengan memasukkan nama, username, password, dan alamat. Pengguna yang mendaftar otomatis memiliki role "user". Nama yang diinput otomatis memiliki kapitalisasi yang benar ketika diinputkan ke sistem.

### F02 - Login
Saat masuk ke aplikasi, pengguna bisa login dengan memasukkan username dan password. Bila username dan password yang diinput coock dengan username dan password pada file user, maka pengguna berhasil loagin.

### F03 - Pencarian Gadget Berdasarkan Rarity
Pengguna dapat mencari gadget dengan rarity tertentu. Pengguna akan memasukkan rarity (C,B,A, S) kemudian aplikasi akan menampilkan gadget dengan rarity tersebut.

### F04 - Pencarian Gadget Berdasarkan Tahun Ditemukan
Pengguna dan Admin dapat melakukan pencarian gadget berdasarkan tahun ditemukan. Pengguna memasukkan sebuah tahun, misalnya yyyy, dan kategori pencarian, yaitu: [=,<,>,>=,<=].

### F05 - Menambah Item
Admin dapat menambahkan item ke dalam inventori. Admin memasukkan ID item yang akan ditambahkan (gadget atau consumable). Jika ID diawali dengan huruf G, maka admin akan emmasukkan nama gadget berdasarkan deskripsi gadget. Jika ID diawali dengan huruf C, admin akan memasukkan nama consumable beserta deskripsi consumable tersebut.

### F06 -  Menghapus Gadget atau Consumable
Admin memiliki wewenang untuk menghapus suatu item pada database. Bila item sudah dihapus, maka entry item akan hilang dari file bila di-save.

### F07 - Mengubah Jumlah Gadget atau Consumable pada Inventory
Admin dapat mengubah jumlah gadget dan consumable yang terdapat dalam sistem.

### F08 - Meminjam Gadget
User dapat melakukan peminjaman gadget yang akan menambahkan entry pada file history bila di-save. Program akan memvalidasi apakah peminjaman yang dilakukan valid, yaitu peminjaman tidak melebihi stok yang ada pada sistem. User tidak dapat meminjam jenis gadget yang sama ketika sedang meminjam gadget tersebut.

### F09 - Mengembalikan Gadget
Prosedur ini dignuakan untuk mengembalikan gadget secara seutuhnya. Karena Doraemon memiliki mesin waktu, tanggal pengembalian tidak harus lebih besar dari tanggal peminjaman

### F10 - Meminta Consumable
Prosedur ini digunakan oleh user untuk meminta consumable yang tersedia. Program akan memvalidasi masukan, yaitu apakah jumlah yang diminta tidak melebihi stok yang tersedia)

### F11 - Melihat Riwayat Peminjaman Gadget
Prosedur ini digunakan oleh Admin sebagai bantuan untuk melihat riwayat peminjaman gadget. Data bisa dibaca dari file yang tersedia. Program akan memperlihatkan 5 entry data terbaru jika terdapat lebih dari 5 data.

### F12 - Melihat Riwayat Pengembalian Gadget
Prosedur ini digunakan oleh Admin sebagai bantuan sebagai bantuan untuk melihat riwayat pengembalian gadget. Data bisa dibaca dari file yang tersedia. Bila terdapat lebih dari 5 entry, program akan mengeluarkan 5 entry data paling baru.

### F13 - Melihat Riwayat Pengembalian Consumable
Prosedur ini digunakan oleh Admin sebagai bantuan untuk melihat riwayat pengembalian consumable. 
Data bisa dibaca dari file yang tersedia. Bila terdapat lebih dari 5 entry, program akan mengeluarkan 5 entry data paling baru.

### F14 - Load Data
Prosedur ini digunakan untuk melakukan laoding data ke dalam sistem. Prosedur ini akan otomatis dijalankan ketika sistem mulai pertama kali bila diberikan input nama folder yang berisi file penyimpanan.

### F15 - Save Data
Prosdur ini digunakan untuk melakukan penyimpanan data ke dalam file setelah dilakukan perubahan.

### F16 - Help
Prosedur ini digunakan untuk memberikan panduan penggunaaan sistem.

### f17 - Exit
Prosedur ini digunakan untuk keluar dari aplikasi.
