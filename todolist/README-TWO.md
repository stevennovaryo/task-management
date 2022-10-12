# To Do List

Link aplikasi di Heroku : [Link](https://pbp-tugas-2-insta-x.herokuapp.com/todolist)

## Asynchronous Programming dan Synchronous Programming
Pada Asynchronous Programming, program melakukan suatu pekerjaan tanpa menunggu pekerjaan yang lain sehingga dapat melakukan pekerjaan lain selagi menunggu suatu pekerjaan selesai. Contohnya ketika menunggu response dari server, program web dapat tetap berjalan melakukan pekerjaan lain. Untuk melakukan asynchronous programming, biasanya kita menggunakan multithread agar bisa melakukan beberapa pekerjaan secara pararel.

Pada Synchronous Programming, program harus menunggu suatu pekerjaan hingga selesai sebelum dapat melakukan pekerjaan selanjutnya. Dengan kata lain, program harus melakukan serangkaian pekerjaan secara sekuensial dan tidak pararel. Jika diterapkan dalam web, maka ketika website merequest ke server, website tersebut tidak akan bisa digunakan karena harus menunggu response dari server sebelum bisa mengupdate website tersebut.

## Event-Driven Programming
Event-Driven Programming adalah paradigma pemrograman dimana alur pekerjaan suatu program sebagian besar diatur oleh event yang terjadi. Suatu event umumnya merupakan user input seperti menekan tombol atau menginput suatu text. Karena alur program dominan diatur oleh event seperti user input, maka user interface menjadi bagian penting dari program ini.

Pada tugas ini, salah satu contoh penerapan event-driven programming adalah tombol add task yang mengirimkan input user ke server dan kemudian mengupdate page secara asynchrounous berdasarkan response server. Alur pekerjaan website sepenuhnya didikte oleh tekanan tombol tersebut sehingga bisa disebut event-driven programming.

## Asynchronous Programming pada AJAX
Dengan menggunakan AJAX, website dapat mengirimkan request dan menerima response secara asynchronous. Ketika response dari server sampai ke browser, AJAX akan mengupdate website dari background. Karena response diterima secara asynchronous, website masih bisa digunakan oleh user meskipun AJAX sedang menunggu response server untuk interaksi user terakhir. Dengan begini, user dapat terus menerus menggunakan website tanpa perlu menunggu setiap kali user melakukan sesuatu dalam website.

## Penjelasan langkah
- Membuat fungsi `get_task_json` di `views.py` yang mengembalikan response berupa `json` yang berisi data semua task milik user tersebut. Kemudian memasukkan path ke `urls.py` agar bisa diakses. Terakhir menggunakan `jQuery` pada `todolist.html` untuk melakukan `AJAX GET`.
- Membuat tombol `Add Task` ke `todolist.html` untuk menggantikan `Create Task`. Kemudian membuat modal yang akan muncul ketika tombol tersebut ditekan. Terakhir memasukkan form pembuatan task seperti di `create_task.html` ke dalam modal.
- Membuat fungsi `add_task` di `views.py` yang akan menerima form dari modal untuk membuat task baru dan mengembalikan JSON berisi data yang diperlukan untuk AJAX mengupdate websitenya.
- Menambahkan path `/todolist/add` ke `urls.py`
- Menggunakan `AJAX POST` untuk menghubungkan form model ke path yang sudah dibuat.
- Menambahkan `data-bs-dismiss="modal"` ke tombol `input` agar menutup modal setelah mensubmit form.
- Menggunakan data yang dikembalikan `add_task` untuk mengupdate website.