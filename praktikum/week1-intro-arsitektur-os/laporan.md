
# Laporan Praktikum Minggu ke-1
Topik: Arsitektur Sistem Operasi 

---

## Identitas
- **Nama**  : Muhammad Fajri Abdullah 
- **NIM**   : 250202979
- **Kelas** : 1IKRB
---

## Tujuan
Tujuan praktikum minggu ini.  
Diharapkan mahasiswa mampu:
1. Menjelaskan peran sistem operasi dalam arsitektur komputer.
2. Mengidentifikasi komponen utama OS (kernel, system call, device driver, file system).
3. Membandingkan model arsitektur OS (monolithic, layered, microkernel).
4. Menggambarkan diagram sederhana arsitektur OS menggunakan alat bantu digital (draw.io / mermaid).
---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.
- OS adalah suatu sistem yang menghubungkan User dengan Hardware (analoginya seperti perantara atau jika digambarkan seperti tukang pos);
  "Sistem operasi ( operating system ; OS) adalah seperangkat program yang mengelola sumber daya perangkat keras komputer dan menyediakan layanan umum untuk aplikasiperangkat lunak. Sistem operasi adalah jenis yang paling penting dari perangkat lunak sistem  dalam sistem komputer." ESA121 – PENGANTAR APLIKASI KOMPUTER, OPERATING SYSTEM, Posted bynanda, January 29, 2020
- DI OS ada beberapa sistem, software, dan program, seperti; Kernel sebagai inti OS, System Call sebagai penjaga gerbang antara User Zone dan Kernel Zone, Device Driver yang menjembatani antara OS dan Hardware Input ( Hardware Input telah dibahas di mata kuliah Emerging Technologies & Digital Transformation), dan File System yang mana umum kita temui untuk menyimpan file
- Model Arsitektur OS itu punya 3 main model, yaitu; Monolithic dimana semua unsur unsur OS digabung dalam satu kotak besar atau bisa disebut kernel tunggal, Layered dengan OS dibangun berlapis dengan hardware sebagai lapisan paling bawah dan User Interface lapisan paling atas, dan yang terakhir adalah Microkernel dengan mengoperasikan fungsi inti di kernel dan sisanya berada di User Interface dan menentukan akan dijalankan di ruang mana (mau di User Zone atau di Kernel Zone)

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.
> Langkah awal
- Login akun gitHub (Jikalau belum punya bisa mendaftarkan segera)
- Download Git dan VSCode lalu konfigurasi Git
- Masuk link yang telah disediakan Penanggungjawab lalu fork dengan menambahkan NIM dibagian OS-202501-NIM
- Clone repository
- Buat folder Praktikum/week1-introarsitektur-os/screenshoots
- Pengerjaan diagram di draw.io
- buka VSCode, lakukan commit dan push ke GitHub anda
- Buat file baru dengan nama laporan.md isi seusai Markdown yang telah ditentukan dan push 
> atau
- Jika folder sudah dibuat, buat folder khusus lagi untuk week-1
- Namakan file (diusahakan sesuai konteks pembelajaran)
- Anda bisa mengcommit dan push secara manual dari GitHub nya langsung dengan memilih  add file lalu pilih file yang ingin anda push
> untuk Linux
- (https://shell.cloud.google.com/) Buka link tersebut untuk menjalankan perintah Linux yang telah di paparkan dalam penugasan
- Salin code Linux yang telah disiapkan oleh penanggungjawab dan jalankan
- Dokumentasikan setiap eksekusi code dengan screenshoots dan menyalin hasil input (output) dan menyimpannya dalam bentuk .txt
- Screenshoots yang tidak berstatus .png diubah pada link (https://jpg2png.com/) untuk mengubah status .jpeg/.jpg menjadi .png
- Anda bisa melakukan commit dan push ke file terkait

2. Perintah yang dijalankan.
> uname -a

> whoami

> lsmod | head

> dmesg | head

> sudo dmesg | head (Penggunaan input [dmesg | head] mengalami kegagalan dan harus ditambahkan [sudo]) 

3. File dan kode yang dibuat.
- Diagram dibuat dengan draw.io dengan standar .png
- Code dijalankan di Shell Cloud Google dengan standar .png untuk gambar dan .txt untuk code.
Bagian hasilnya bisa dilihat pada bagian "## Hasil Eksekusi" dbagian bawah
4. Commit message yang digunakan.
Commit message yang digunakan "Update laporan.md"
---

## Kode / Perintah
Hasil dari input bedasrakan potongan kode atau perintah utama:
```bash
uname -a
lsmod | head
dmesg | head
```
```bash
Welcome to Cloud Shell! Type "help" to get started, or type "gemini" to try prompting with Gemini CLI.
To set your Cloud Platform project in this session use `gcloud config set project [PROJECT_ID]`.
You can view your projects by running `gcloud projects list`.
herefajri@cloudshell:~$ uname -a
Linux cs-32863767896-default 6.6.105+ #1 SMP PREEMPT_DYNAMIC Sat Sep 27 08:48:45 UTC 2025 x86_64 x86_64 x86_64 GNU/Linux
herefajri@cloudshell:~$ whoami
herefajri
herefajri@cloudshell:~$ lsmod | head
Module                  Size  Used by
ip6table_nat           12288  1
xt_set                 20480  0
ip_set                 53248  1 xt_set
netlink_diag           12288  0
iptable_nat            12288  1
xt_nat                 12288  6
xt_mark                12288  1
veth                   36864  0
nft_limit              16384  1
herefajri@cloudshell:~$ dmesg | head
dmesg: read kernel buffer failed: Operation not permitted
herefajri@cloudshell:~$ sudo dmesg | head
[    0.000000] Linux version 6.6.105+ (builder@2832f747b46d) (Chromium OS 17.0_pre498229-r33 clang version 17.0.0 (/var/cache/chromeos-cache/distfiles/egit-src/external/github.com/llvm/llvm-project 14f0776550b5a49e1c42f49a00213f7f3fa047bf), LLD 17.0.0) #1 SMP PREEMPT_DYNAMIC Sat Sep 27 08:48:45 UTC 2025
[    0.000000] Command line: BOOT_IMAGE=/syslinux/vmlinuz.A init=/usr/lib/systemd/systemd rootwait ro noresume loglevel=7 console=tty1 console=ttyS0,115200 security=apparmor virtio_net.napi_tx=1 nmi_watchdog=0 csm.disabled=1 loadpin.exclude=kernel-module,firmware modules-load=loadpin_trigger firmware_class.path=/var/lib/nvidia/firmware module.sig_enforce=1 dm_verity.error_behavior=3 dm_verity.max_bios=-1 dm_verity.dev_wait=1 i915.modeset=1 cros_efi root=/dev/dm-0 "dm-mod.create=vroot,,,ro,0 4077568 verity 0 PARTUUID=7BCC9916-089B-5741-BDB4-BBF2531D61CC PARTUUID=7BCC9916-089B-5741-BDB4-BBF2531D61CC 4096 4096 509696 509696 sha256 cd005c970a2f850726894bf85289300eaf8bb857b72888c81584d6c76887edb1 495a0ee73578f50cbe5c9e99905ea2149e061977f71182962a65c0e169274c5b"
[    0.000000] BIOS-provided physical RAM map:
[    0.000000] BIOS-e820: [mem 0x0000000000000000-0x0000000000000fff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000000001000-0x0000000000054fff] usable
[    0.000000] BIOS-e820: [mem 0x0000000000055000-0x000000000005ffff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000000060000-0x0000000000097fff] usable
[    0.000000] BIOS-e820: [mem 0x0000000000098000-0x000000000009ffff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000000100000-0x00000000bd221fff] usable
[    0.000000] BIOS-e820: [mem 0x00000000bd222000-0x00000000bd223fff] ACPI data
herefajri@cloudshell:~$ 
```


---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/DIAGRAM_ARSITEKTUR_OS.png)
![Screenshot hasil](screenshots/Screenshot_dmesg=keseluruhan_shell.cloud.google.com.png).


---

## Analisis
**- Jelaskan makna hasil percobaan.**
- [uname -a] untuk menampilkan informasi lengkap tentang OS dan kernel seperti versi kernel,dsb.
- [whoami] untuk menampilan nama User yang berstatus aktif
- [lsmod | head] untuk menampilkan bagian program kernel yang sedang digunakan/dijalankan/dimuat
- [dmesg | head] untuk menampilkan pesan boting dan log kernel/pesan dari kernel (disclaimer: Disini saya menggunakan tambahan perintah/code "sudo" dikarenakan akses yang terbatas dan pengguaan input perintah tersenut untuk mengizinkan akses sementara).

**- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).**  
[uname -a]
Perintah [uname -a] ini adalah permintaan dari program User ke Kernel dan harus mendapatkan izin di zona System Call untuk mendapatkan persetujuan dan dapat melihat detail tentang lingkungan dan juga tentang kernel itu sendiri. Dan hubungannya dengan Arsitektur OS adalah yaitu adanya hubungan di lingkup User dan Kernel Inti, dimana di User Zone [uname -a] mengeksekusi perintah dengan label Manajemen Proses.

[whoami]
Pengelolaan laporan identitas User ke kernel yang mana dikarenakan saya memakai shell.cloud.google jadi menggunakan identitas akun google saya sebagai laporan verifikasi ke System Call yang diteruskan ke Kernel dan menghasilkan output menampilkan nama pengguna aktif. Dan hubungannya dengan Arsitektur OS, sama seperti [uname -a] yaitu dimana Kernel inti mengelola perintah dengan nama Manajemen Proses

[lsmod | head]
Ini sama seperti sebelumnya, memberi perintah dan ya sama System Call akan memverifikasi terlebih dahulu lalu meneruskan ke Kernel. Namun perintah ini adalah perintah untuk menanyakan tentang komponen (Modul Kernel) yang sedang digunakan saat ini. Disini hubungan dengan Arsitektur OS adalah dibagian Manajemen Perangkat dimana Modul yang dipakai dan menjadi tanggung jawab Kernel Inti, modul ini akan ditampilkan oleh perintah [lsmod] sebelumnya 

[dmesg | head]
System Call tetap sama, menyaring tindakan dan perintah, serta verifikasi. Namun untuk kernel disini akan memberikan pandangan tentang inisial-inisial detail tentang Hardware seperti jenis CPU, deteksi perangkat dan konfigurasi kernel. Penggunaan [sudo] menjadi acuan bahwa mekanisme keamanan dan kontrol akses pada kernel aktif. Dan disini hubungannya dengan Arsitektur OS adalah masih tetap dibagian Kernel Inti dimana di bagian tanggungjawab kernel yaitu keamanan yang mana menegakkan izin, seperti yang telah di buat dalam percobaan, dmesg perlu [sudo] untuk bisa mendapatkan izin ke Kernel

**- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?**
Yang terjadi adalah:
- Jika di Linux, semua perintah akan berjalan lancar dari [uname] sampai [dmesg]
- Sedangkan jika di Windows menggunakan hal-hal seperti di CMD maka akan didapat kegagalan kecuali pada bagian [whoami]
---

## Kesimpulan
2–3 poin kesimpulan dari praktikum ini.
- Adanya kegiatan praktikum ini, para mahasiswa dituntut agar mempelajari sistem OS, baik dari segi OS dasar hingga Model Arsitektur OS, serta memahami fungsinya dan bisa menjelaskan dengan bahasa sendiri untuk membuktikan pemahaman dia tentang OS 
- Dengan ini, mahasiswa juga diharuskan emiliki sistem problem solving-nya sendiri dalam mengatasi permasalahan dan dituntut untuk kreatif
---

## Quiz
Quiz
Jawab pertanyaan berikut di bagian Quiz pada laporan:

1. Sebutkan tiga fungsi utama sistem operasi.
**Jawaban:**
- OS bertugas sebagai manajer utama sistem yang mana mengemban tanggung jawab untuk mengirim atau mengirim kembali semua sumber-sumber yang tersedia di sistem
- OS menyediakan ruang atau jembatan agar user bisa berinteraksi dengan hardware
- OS mengelola jalannya suatu proses semua program dengan memastikan semuanya berjalan secara efisien dan tak saling menghalangi serta memanajemen keamanan sistem

2. Jelaskan perbedaan antara kernel mode dan user mode.
**Jawaban:**
- User Mode memiliki eksekusi tindakan yang terbatas dikarenakan adanya batas yang jelas antara ruang User dan Kernel yang dipisahkan oleh beberapa sistem keamanan, salah satunya system call yang diawasi oleh Kernel. Andaikata ada situasi buruk terjadi seperti contohnya hal-hal yang ada keterkaitannya dengan aplikasi ilegal maka operasi akan berhenti karena adanya sistem keamanan tersebut, dan hanya menyebabkan suatu aplikasi berhenti. Sedangkan,
- Kernel Mode itu memiliki akses ke segala bidang bahkan yang paling dalam sekalipun dikarenakan yang beroperasi adalah Kernel atau Inti dari Kernel Mode itu. Tapi jikalau ada suatu tindakan yang berbahaya atau adanya kegagalan maka kerusakannya bisa sangat berbahaya bahkan bisa merusak kinerja sistem komputer.

3. Sebutkan contoh OS dengan arsitektur monolithic dan microkernel.
**Jawaban:**
- Arsitektur Monolithic atau Layanan OS inti yang dijalankan di ruang Kernel Mode seperti Linux.
- Arsitektur Microkernel atau  Layanan OS dasar di Kernel Mode bahkan beberapa ada di User Mode, contohnya seperti Mach, QNX, MINIX.

---

## Refleksi Diri
Sesi refleksi terkait aktivitas praktikum dan yang berhubungan dengan pembelajaran dan penugasan Week-1 :
- Apa bagian yang paling menantang minggu ini?
**Jawaban:**
  Penggunaan pertama kalinya VSCode, GitHub, dan Git Bash untuk mengkaitkan folder dari komputer (File Manager) ke sistem GitHub  
- Bagaimana cara Anda mengatasinya?
**Jawaban:**
  Dengan menginput letak permasalahan dengan bantuan AI (ChatGPT dan Gemini) dengan via chat atau dokumentasi situasi agar AI bisa memahamilebih lanjut terkait  kendala yang dialami user serta bantuan dari teman-teman dalam bentuk penjelasan untuk memastikan aktivitas praktikum berjalan dan menghasilkan output yang sesuai standar penugasan
---

**Credit:**  
1. ESA121 – PENGANTAR APLIKASI KOMPUTER, OPERATING SYSTEM, Posted bynanda, January 29, 2020 (https://bahan-ajar.esaunggul.ac.id/esa121/2020/01/29/operating-system/)
