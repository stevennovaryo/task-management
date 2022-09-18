# MyWatchList

Link aplikasi di Heroku : [Link](https://pbp-tugas-2-insta-x.herokuapp.com/mywatchlist)

## JSON, XML, HTML
JSON (JavaScript Object Notation) adalah file format yang mudah untuk dibaca manusia. Data direpresentasikan dengan object yang terdiri dari beberapa pasangan attribute-value. Saat ini, JSON merupakan salah satu bentuk data delivery yang paling populer dan sering digunakan. JSON berasal dari bahasa pemrograman JavaScript. Namun, karena format file yang keseluruhannya adalah text, banyak bahasa lain yang ikut menggunakan JSON untuk berbagai hal.

XML (eXtensible Markup Language) adalah file format yang diciptakan dari SGML (Standard Generalized Markup Language) yang bertujuan untuk menyimpan dan mengirimkan data. Mirip dengan HTML, XML menggunakan tag untuk menyimpan data. Tag di XML juga bisa memiliki tag lain sehingga struktur data di XML mirip dengan struktur data tree.

HTML (HyperText Markup Language) adalah file format yang juga merupakan bawaan dari SGML. HTML dibuat dengan tujuan untuk menampilkan data. Penampilan data dalam HTML dilakukan dengan tag untuk menentukan jenis data. Karena tag juga bisa memiliki tag lain, maka struktur data di HTML juga mirip dengan struktur data tree. Saat ini, HTML merupakan file format yang paling sering digunakan oleh berbagai website untuk menampilkan webpage mereka.

Dari ketiga file format di atas, HTML berbeda sendiri karena tujuannya bukan menyimpan dan mengirimkan data, namun untuk menampilkan data. Berdasarkan syntax, maka JSON berbeda sendiri karena XML dan HTML bawaan dari SGML yang menggunakan tag. Mengenai data delivery, saat ini JSON merupakan format yang lebih sering digunakan dibandingkan dengan XML. Hal ini karena JSON memiliki syntax yang lebih mudah dimengerti manusia, dan struktur data JSON mirip dengan struktur sebuah object, sehingga lebih mudah digunakan untuk komunikasi antar program. Untuk penyimpanan data yang lebih kompleks seperti menyimpan UML diagram atau gambar vector, XML digunakan karena struktur tree tag yang lebih powerful dan kompleks. HTML paling sering digunakan untuk menampilkan webpage sebuah website karena tujuan HTML untuk menampilkan data. 

## Data Delivery
Sistem data delivery tentunya diperlukan dalam pengimplementasian platform. Sebuah platform akan memerlukan komunikasi dan mengirimkan data ke banyak pihak dan platform-platform lain. Contohnya jika platform kita membutuhkan data seperti gambar dari pihak lain. Maka kita harus mengirimkan data berupa request ke pihak lain tersebut, dan kemudian menerima data yang dikirimkan platform lain. Begitu juga sebaliknya, bisa saja pihak lain yang meminta data dari platform kita.

Salah satu hal terpenting dari sebuah sistem data delivery adalah memastikan data yang dikirimkan dapat dipahami oleh pihak lain. Hal ini karena pihak yang menggunakan platform lain kemungkinan besar memiliki sistem atau struktur yang berbeda dari platform kita. Contohnya platform lain menggunakan bahasa pemrograman yang berbeda dari platform kita. Karena itulah pada awal web diciptakan, banyak yang mencetus standard untuk penyimpanan dan pengiriman data seperti JSON dan XML. Saat ini, JSON yang paling sering digunakan untuk data delivery sehingga platform baru yang ingin diciptakan juga harus dapat memiliki kemampuan untuk memahami dan mengirimkan format JSON.

## Penjelasan langkah

### Langkah 1
Untuk membuat sebuah aplikasi django baru, kita menggunakan perintah `python manage.py startapp <APP_NAME>`. Pada kasus ini, karena kita ingin membuat aplikasi baru bernama `mywatchlist`, maka perintah yang dijalankan di terminal adalah `python manage.py startapp mywatchlist`. Dari perintah ini maka akan terbuat sebuah folder baru bernama `mywatchlist` yang berisi file-file yang diperlukan untuk sebuah app Django.

### Langkah 2
Untuk menambahkan path agar aplikasi `mywatchlist` dapat diakses di `http://localhost:8000/mywatchlist`, pertama kita menambahkan path ke `mywatchlist.urls` dengan menambahkan `path('mywatchlist/', include('mywatchlist.urls'))` kedalam variable `urlpatterns` di file `project_django/urls.py`. Kemudian, kita perlu menambahkan path lagi dari `mywatchlist.urls` menuju `mywatchlist.views`. Hal ini dilakukan dengan menambahkan function yang nantinya akan menampilkan webpage ke `mywatchlist/views.py` dan kemudian disambungkan ke `mywatchlist.urls` dengan menambahkan path ke function tersebut ke `mywatchlist/urls.py`.

### Langkah 3
Pertama kita membuat class `MyWatchList` di `mywatchlist/models.py`. Kemudian kita mengisi class tersebut dengan atribut-atribut yang kita inginkan untuk class tersebut.

Atribut yang dimasukkan:
- `watched` dengan data type `models.BooleanField()`
- `title` dengan data type `models.TextField()`
- `rating` dengan data type `models.IntegerField()`
- `release_date` dengan data type `models.DateField()`
- `review` dengan data type `models.TextField()`

Setelah class dibuat, kita melakukan perintah `python manage.py makemigrations` dan `python manage.py migrate` untuk memasukkan class model yang baru kita buat ke database.

## Postman Screenshot
![HTML](./HTML.png?raw=true)
![XML](./XML.png?raw=true)
![JSON](./JSON.png?raw=true)