# Katalog

Link aplikasi di Heroku : [Link](https://pbp-tugas-2-insta-x.herokuapp.com/katalog)

## Bagan

![Bagan](./Bagan.png?raw=true)

1. User memberikan request ke server Django
2. `urls.py` memproses request tersebut dan melakukan routing ke views yang terpilih
3. `views.py` yang terpilih memproses request tersebut dan melakukan query ke `models.py` jika diperlukan
4. `models.py` mengambil data dari database sesuai permintaan `views.py` dan mengembalikan data tersebut ke `views.py`
5. `views.py` memilih template html yang diperlukan dan menggunakan data dari `models.py` untuk memproses template tersebut
6. `views.py` mengirimkan template html yang sudah diproses kembali ke User
7. User menampilkan template html tersebut di web browser

## Virtual Environment

### Alasan menggunakan virtual environment
Dengan menggunakan virtual environment, kita dapat memisahkan package library yang diperlukan untuk setiap projek yang kita miliki.
Selain itu, setiap projek dapat menggunakan library yang sama dengan versi berbeda tanpa menghasilkan konflik.
Contohnya, projek A menggunakan python 2 sedangkan projek B menggunakan python 3. Jika tidak menggunakan virtual environment, maka
umumnya kita hanya bisa mengakses salah satu dari kedua versi python tersebut dalam waktu yang sama sehingga setiap kali kita ingin
mengerjakan projek lain, kita perlu mengatur terlebih dahulu versi python yang digunakan komputer kita. Selain itu, jika kita mengupdate
library tanpa menggunakan virtual environment, ada kemungkinan projek lain yang menggunakan library yang sama akan menjadi rusak karena
versinya tidak compatible. Dengan menggunakan virtual environment, setiap kali kita pindah projek kita tinggal masuk ke virtual
environment projek tersebut dan perubahan pada library di virtual environment tersebut tidak akan dilakukan pada virtual environment
lain sehingga tidak ada kemungkinan konflik pada projek lain.

### Membuat aplikasi Django tanpa virtual environment
Bisa saja membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Namun, seperti yang sudah ditulis di atas,
banyak sekali kerumitan yang muncul jika terdapat projek lain yang menggunakan library yang sama sehingga jauh lebih baik untuk
menggunakan virtual environment.

## Penjelasan langkah

### Langkah 1
Membuat fungsi `show_katalog` yang akan mereturn template html pada `views.py`

### Langkah 2
Memasukkan routing ke `views.py` di dalam `urls.py` folder katalog dan folder project_django menggunakan variable `urlpatterns`

### Langkah 3
Melakukan `migration` dan `loaddata` dari `initial_catalog_data.json` untuk memasukkan data ke local database. Kemudian
mengambil semua objects yang ada di database untuk dimasukkan sebagai context ke template html oleh `views.py`

### Langkah 4
Karena workflows, Procfile, dan lain-lain sudah tersetup dari template repo, maka tinggal membuat app baru di Heroku,
kemudian memasukkan `HEROKU_API_KEY` dan `HEROKU_APP_NAME` ke repository secret 