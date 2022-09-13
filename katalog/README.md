# Katalog

Link aplikasi di Heroku : [Link](https://pbp-tugas-2-insta-x.herokuapp.com/katalog)

## Bagan

![Bagan](./Bagan.png?raw=true)

1. User memberikan request ke server Django
2. urls.py memproses request tersebut dan melakukan routing ke views yang terpilih
3. views.py yang terpilih memproses request tersebut dan melakukan query ke models.py jika diperlukan
4. models.py mengambil data dari database sesuai permintaan views.py dan mengembalikan data tersebut ke views.py
5. views.py memilih template html yang diperlukan dan menggunakan data dari models.py untuk memproses template tersebut
6. views.py mengirimkan template html yang sudah diproses kembali ke User
7. User menampilkan template html tersebut di web browser
