
# Laporan Praktikum Minggu ke 3
Topik:  Manajemen File dan Permission di Linux

---

## Identitas
- **Nama**  : Muhammad Fajri Abdullah 
- **NIM**   : 250202979
- **Kelas** : 1IKRB

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  
> Tujuan utama dari praktikum ini adalah agar mahasiswa mampu mengoperasikan perintah Linux dasar dengan benar, memahami sistem izin (permission), dan mendokumentasikan hasilnya dalam format laporan Git. Setelah menyelesaikan tugas ini,diharapkan para mahasiswa mampu:

- Menggunakan perintah ls, pwd, cd, cat untuk navigasi file dan direktori.
- Menggunakan chmod dan chown untuk manajemen hak akses file.
- Menjelaskan hasil output dari perintah Linux dasar.
- Menyusun laporan praktikum dengan struktur yang benar.
- Mengunggah dokumentasi hasil ke Git Repository tepat waktu.



---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
**1. Eksperimen 1 – Navigasi Sistem File**
```bash
pwd
ls -1
cd /tmp
ls -a
```
--
#pwd
```bash
herefajri@cloudshell:~$ pwd
/home/herefajri
```
**Analisis & Penjelasan**
- `pwd` adalah singkatan dari "Print Working Directory".
-  Fungsinya menampilkan direktori aktif saat ini.
-  Pada hasil I/O diatas bisa dilihat ada bagian `/home/herefajri` yang mana artinya posisi direktori sedang ada di directory home milik User atau Saya sendiri.

--
#ls -1
```bash
herefajri@cloudshell:~$ ls -l
total 12
-rw------- 1 herefajri herefajri   42 Oct 17 12:58 percobaan.txt
drwxrwxr-x 3 herefajri herefajri 4096 Oct 16 15:23 praktikum
-rwxr-xr-x 1 herefajri herefajri  913 Oct 17 12:58 README-cloudshell.txt
```
**Analisis & Penjelasan**
- 

#cd /tmp
 ```bash
herefajri@cloudshell:~$ cd /tmp
herefajri@cloudshell:/tmp$
```

#ls -a
```bash
herefajri@cloudshell:/tmp$  ls -a
.                               gemini-ide-server-446.json                                      tmp.0NHMVi75Dv  tmp.4QDQea0t1X  vscode-git-a3d1a5f5c9.sock
..                              minikube_delete_7d205c9ac03a60edf48a1c0a3ed3a4d118782338_0.log  tmp.1ivNYhsXLu  tmp.HboOvNEZtn  vscode-ipc-fe411929-83f4-46e2-8a53-d0b91972634c.sock
code-oss-vm-session-state.json  node-compile-cache                                              tmp.2ySuu9UsQG  tmp.VM5vSF8YBB  vscode-skaffold-events-logs
gemini-ide-server-37777.json    tmp                                                             tmp.3qj6157Xs9  tmux-1000
herefajri@cloudshell:/tmp$
```


**2. Eksperimen 2 – Membaca File**
```bash
cat /etc/passwd | head -n 5
```

#cat /etc/passwd | head -n 5
```bash
herefajri@cloudshell:/tmp$ cd
herefajri@cloudshell:~$ cat /etc/passwd | head -n 5
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
```

**3. Eksperimen 3**
```bash
echo "Hello <NAME><NIM>" > percobaan.txt
ls -l percobaan.txt
chmod 600 percobaan.txt
ls -l percobaan.txt
```
```bash
herefajri@cloudshell:~$ echo "Hello MUHAMMAD FAJRI ABDULLAH - 250202979" > percobaan.txt
herefajri@cloudshell:~$ ls -l percobaan.txt
-rw------- 1 herefajri herefajri 42 Oct 17 12:59 percobaan.txt
herefajri@cloudshell:~$ sudo chmod 600 percobaan.txt
herefajri@cloudshell:~$ ls -l percobaan.txt
-rw------- 1 herefajri herefajri 42 Oct 17 12:59 percobaan.txt
herefajri@cloudshell:~$ 

```

dan
```bash
sudo chown root percobaan.txt
ls -l percobaan.txt
```
```bash
herefajri@cloudshell:~$ sudo chown root percobaan.txt
herefajri@cloudshell:~$ ls -l percobaan.txt
-rw------- 1 root herefajri 42 Oct 16 15:26 percobaan.txt
herefajri@cloudshell:~$
```


echo "Hello Muhammad Fajri Abdullah 250202979" > percobaan.txt
ls -l percobaan.txt
chmod 600 percobaan.txt
ls -l percobaan.txt


[Lihat hasil keseluruhan I/O dari Navigasi Sistem File, Membaca File, dan Permission & Ownership.txt](code/keseluruhan.txt)

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
1. Eksperimen 1 – Navigasi Sistem File

![Screenshot hasil](screenshots/Eksperimen%201%20pwd.png)
![Screenshot hasil](screenshots/Eksperimen%201%20ls%20-1.png)
![Screenshot hasil](screenshots/Eksperimen%201%20cd%20tmp.png)
![Screenshot hasil](screenshots/Eksperimen%201%20ls%20-a.png)

2. Eksperimen 2 – Membaca File

![Screenshot hasil](screenshots/E2cat_etcpasswdhead-n5.png)

3. Eksperimen 3– Permission & Ownership

![Screenshot hasil](screenshots/echo%20NAMExNIM.png)
![Screenshot hasil](screenshots/sudo%20chown.png)

_**Bonus:**_
![Screenshot hasil](screenshots/Hasil%20echo%20sampai%20ls%20-1%20sebelum%20root.png)
![Screenshot hasil](screenshots/Hasil_Keseluruhan.png)

---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

## Analisis Hasil
Tugas
1. Dokumentasikan hasil seluruh perintah pada tabel observasi di laporan.md.


2. Jelaskan fungsi tiap perintah dan arti kolom permission (rwxr-xr--).


3. Analisis peran chmod dan chown dalam keamanan sistem Linux.


4. Upload hasil dan laporan ke repositori Git sebelum deadline.



---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. Tuliskan jawaban di bagian Quiz pada laporan:
  **Jawaban:**  
2. Apa fungsi dari perintah chmod?
  **Jawaban:**  
3. Apa arti dari kode permission rwxr-xr--?
  **Jawaban:**  
4. Jelaskan perbedaan antara chown dan chmod.
  **Jawaban:**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
