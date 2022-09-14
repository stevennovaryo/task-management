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
Virtual environment dapat memisahkan package library yang diperlukan untuk setiap projek yang kita miliki. Dengan begitu ketika kita menambahkan, mengubah, atau membuang library di suatu virtual environment, perubahan tersebut tidak akan mempengaruhi virtual environment lain.

### Alasan menggunakan virtual environment
Contohnya, projek A menggunakan python 2 sedangkan projek B menggunakan python 3. Jika tidak menggunakan virtual environment, maka umumnya kita hanya bisa mengakses salah satu dari kedua versi python tersebut dalam waktu yang sama sehingga setiap kali kita ingin mengerjakan projek lain, kita perlu mengatur terlebih dahulu versi python yang digunakan komputer kita. Selain itu, jika kita mengupdate library tanpa menggunakan virtual environment, ada kemungkinan projek lain yang menggunakan library yang sama akan menjadi rusak karena versinya tidak compatible. Dengan menggunakan virtual environment, setiap kali kita pindah projek kita tinggal masuk ke virtual environment projek tersebut dan perubahan pada library di virtual environment tersebut tidak akan dilakukan pada virtual environment lain sehingga tidak ada kemungkinan konflik pada projek lain.

### Membuat aplikasi Django tanpa virtual environment
Bisa saja membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Namun, seperti yang sudah ditulis di atas, banyak sekali kerumitan yang muncul jika terdapat projek lain yang menggunakan library yang sama sehingga jauh lebih baik untuk menggunakan virtual environment.

## Penjelasan langkah

### Langkah 1
Membuat fungsi `show_katalog` yang akan mereturn template html pada `views.py`. Fungsi `show_katalog` mengambil semua data `CatalogItem`, menyiapkan context untuk template, mengambil template `katalog.html`, dan terakhir mereturn render template tersebut dengan context.

### Langkah 2
Memasukkan routing ke `views.py` di dalam `katalog/urls.py` dengan memasukkan `path('', show_katalog, name='show_katalog'),` ke dalam variable `urlpatterns`. Kemudian memasukkan routing `katalog.urls` ke `project_django/urls.py` dengan memasukkan `path('katalog/', include('katalog.urls')),` ke dalam variable `urlpatterns`.

### Langkah 3
Menggunakan `python manage.py migration` dan `python manage.py makemigration` untuk memasukkan model CatalogItem ke database. Kemudian menggunakan `python manage.py loaddata initial_catalog_data.json` untuk memasukkan data yang terdapat di `initial_catalog_data.json` ke local database. Setelah memasukkan data ke database, mengimport `CatalogItem` ke `views.py` agar dapat digunakan sebagai context template.

### Langkah 4
Karena workflows, Procfile, dan lain-lain sudah tersetup dari template repo, maka tinggal membuat app baru di Heroku. Setelah itu, memasukkan `HEROKU_API_KEY` dan `HEROKU_APP_NAME` ke repository secret.