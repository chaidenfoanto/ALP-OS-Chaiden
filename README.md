# **ALP Operating System**

Nama  : Chaiden Richardo Foanto
NIM   : 0806022310023

### **Reimplementasi Basic CLI pada Sistem Linux Menggunakan Python**

## **Deskripsi Proyek**
Proyek ini bertujuan untuk membuat aplikasi Command Line Interface (CLI) sederhana menggunakan Python, yang mampu meniru beberapa fungsi dasar dari shell/terminal Linux. Program ini memungkinkan pengguna untuk menjalankan berbagai perintah seperti `ls`, `pwd`, `cd`, hingga beberapa command unik tambahan yang dibuat untuk menambah fungsionalitas dan kenyamanan.

Aplikasi ini cocok untuk digunakan di sistem operasi berbasis UNIX maupun Windows, serta dapat dijalankan langsung di terminal Python.

---

## **Fitur Utama**
Aplikasi CLI ini mendukung **12 command dasar** yang wajib diimplementasikan serta **3 command tambahan unik** untuk meningkatkan fungsionalitas. 

---

## **Daftar Command**
### **Command Dasar**
| Command                | Deskripsi                                                                 |
|------------------------|---------------------------------------------------------------------------|
| `ls`                  | Menampilkan daftar file dan folder di direktori saat ini.                |
| `pwd`                 | Menampilkan direktori kerja saat ini.                                    |
| `cd <path>`           | Mengubah direktori kerja ke `<path>`.                                    |
| `mkdir <directory>`   | Membuat direktori baru dengan nama `<directory>`.                        |
| `rmdir <directory>`   | Menghapus direktori kosong bernama `<directory>`.                        |
| `touch <file>`        | Membuat file kosong baru dengan nama `<file>`.                           |
| `rm <file>`           | Menghapus file bernama `<file>`.                                         |
| `cp <source> <dest>`  | Menyalin file dari `<source>` ke `<dest>`.                               |
| `mv <source> <dest>`  | Memindahkan atau mengganti nama file/direktori dari `<source>` ke `<dest>`.|
| `clear`               | Membersihkan layar terminal.                                             |
| `exit`                | Keluar dari CLI.                                                        |
| `help`                | Menampilkan daftar perintah yang tersedia beserta deskripsinya.         |

### **Command Tambahan**
| Command                   | Deskripsi                                                                 |
|---------------------------|---------------------------------------------------------------------------|
| `find_large <size>`       | Menampilkan file di direktori saat ini yang lebih besar dari `<size>` byte.|
| `tree`                    | Menampilkan struktur direktori dalam bentuk pohon.                       |
| `joke`                    | Menampilkan lelucon acak untuk hiburan.                                  |

---

## **Cara Menjalankan Program**
1. Pastikan Anda telah menginstal Python 3 di komputer Anda.
2. Salin kode program ke dalam file Python, misalnya `simple_cli.py`.
3. Buka terminal atau command prompt.
4. Navigasikan ke direktori tempat file Python berada.
5. Jalankan program dengan perintah:  
   ```bash
   python simple_cli.py
    ```
6. Program akan memulai CLI sederhana. Ketikkan perintah yang diinginkan dan tekan Enter.

---

## Contoh Penggunaan Command

### **Command Dasar**
1. **Melihat daftar file dan folder:**  
   ```bash
   ls
    ```
   Menampilkan semua file dan folder di direktori saat ini.
   
2. **Melihat direktori kerja saat ini:**  
   ```bash
   pwd
    ```

3. **Berpindah ke direktori baru:**  
   ```bash
   cd
    ```

4. **Membuat direktori baru:**  
   ```bash
   mkdir <nama_direktori>
    ```

5. **Menghapus direktori:**  
   ```bash
   rmdir <nama_direktori>
    ```

6. **Membuat file baru:**  
   ```bash
   touch <nama_file>
    ```

7. **Menhapus file:**  
   ```bash
   rm <nama_file>
    ```

8. **Menyalin file ke lokasi baru:**  
   ```bash
   cp <sumber> <tujuan>
    ```

9. **Memindahkan atau mengganti nama file/direktori:**  
   ```bash
   mv <sumber> <tujuan>
    ```

10. **Membersihkan layar terminal:**  
   ```bash
   clear
   ```

11. **Keluar dari program:**  
   ```bash
   exit
   ```

12. **Melihat daftar perintah yang tersedia:**  
   ```bash
   help
   ```


### **Command Tambahan**
1. **Menampilkan file lebih besar dari ukuran tertentu:**  
   ```bash
   help
   ```

2. **Menampilkan struktur direktori dalam bentuk pohon:**
  ```bash
   tree
   ```

3. **Menampilkan lelucon acak:**
  ```bash
    joke
  ```

