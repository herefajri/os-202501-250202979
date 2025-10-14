
# Laporan Praktikum Minggu ke-2
Topik: Struktur System Call dan Fungsi Kernel
---

## Identitas
- **Nama**  : Muhammad Fajri Abdullah 
- **NIM**   : 250202979
- **Kelas** : 1IKRB
---

## Tujuan
Tujuan praktikum minggu ini.  
> Diharapkan mahasiswa mampu:
- Menjelaskan konsep dan fungsi system call dalam sistem operasi.
- Mengidentifikasi jenis-jenis system call dan fungsinya.
- Mengamati alur perpindahan mode user ke kernel saat system call terjadi.
- Menggunakan perintah Linux untuk menampilkan dan menganalisis system call.


---

## Dasar Teori
- Jembatan komunikasi aman antara User Space yang memiliki keterbatasan gerak dan Kernel Space yang memiliki akses ke semua bidang sekaligus pusat kendali, dipegang oleh System Call, dimana bagian daripada User Space, ketika mereka ingin menjalankan sebuah operasi dengan Kernel harus di periksa oleh System Call. 
- Kernel sebagai pusat kendali memiliki fungsi utama yaitu; manajemen proses, manajemen memori, manajemen perangkat I/O, dan manajemen berkas atau File Ststem. 
- System Call sendiri memiliki beberapa Struktur seperti;
  1. **Permintaan**, untuk memanggil fungsi yang telah disediakan oleh Standard Library (Jembatan awal ke System Call)
  2. **Penyiapan Parameter**, untuk mempersiapkan laporan permintaan yang jelas dan terstruktur untuk dikirim ke Kernel
  3. **Transisi Mode (Trap/Interrupt)**, bagian yang sama dengan System Call namun mekanisme nya ke CPU untuk mengubah hak akses dari User ke Kernel
  4. **Pengembalian Kontrol**, agar setelah kernel selesai menerima, menjalankan tugas, dan memberikan output, anda bisa kembali ke mode pengguna dan bisa input lagi
---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.
   1.  Gunakan Linux (Ubuntu/WSL) dan pastikan perintah `strace` dan `man` sudah terinstal, serta konfigurasikan ke Git.
   2. Untuik menganalisis System Call, jalankan perintah `strace ls`. Catat 5–10 system call pertama yang muncul dan jelaskan fungsinya. Simpan hasil analisis ke `results/syscall_ls.txt`.
   3. Untuk menelusuri System Call File I/O, jalankan perintah 
   `strace -e trace=open,read,write,close cat /etc/passwd`, dan analisis bagaimana file dibuka, dibaca, dan ditutup oleh kernel.
   4. Untuk mengamati Mode Operasi CPU (Mode User vs Kernel), jalankan perintah `dmesg | tail -n 10`, dan amati log kernel yang muncul.
   5. Mekanisme pembuatan Diagram Alur System Call yaitu dengan membuat diagram yang menggambarkan "alur eksekusi system call dari program user hingga kernel dan kembali lagi ke user mode". Anda bisa  menggunakan link  ```bash draw.io``` atau ```bash
   mermaid``` . Simpan sesuai prosedur pengerjaan dengan penempatan di:
     ```praktikum/week2-syscall-structure/screenshots/syscall-diagram.png```.
   6. Anda bisa melakukan commit dan push dengan:
 ```bash
   git add .
   git commit -m "Minggu 2 - Struktur System Call dan Kernel Interaction"
   git push origin main
   ```
atau Anda bisa melakukannya dengan mudah dengan menekan tombol add file di folder Anda.

2. Perintah yang dijalankan.
 ```bash
   strace ls
   ```
 ```bash
   strace -e trace=open,read,write,close cat /etc/passwd
   ```
 ```bash
   dmesg | tail -n 10
   ```

Jika `dmesg | tail -n 10` tak bisa dijalankan, Anda bisa menamnahkan kata `sudo` diawal input dmesg.

3. File dan kode yang dibuat.
Diagram dibuat dengan draw.io dengan standar .png.
Code dijalankan di Shell Cloud Google dengan standar .png untuk gambar dan .txt untuk code. Bagian hasilnya bisa dilihat pada bagian "## Hasil Eksekusi" dbagian bawah.

4. Commit message yang digunakan.
Commit message yang digunakan "Update laporan.md".

---

## Kode / Perintah
Hasil input potongan kode atau perintah utama:
```bash
strace ls
strace -e trace=open,read,write,close cat /etc/passwd
dmesg | tail -n 10
```
```bash
Welcome to Cloud Shell! Type "help" to get started, or type "gemini" to try prompting with Gemini CLI.
To set your Cloud Platform project in this session use `gcloud config set project [PROJECT_ID]`.
You can view your projects by running `gcloud projects list`.
herefajri@cloudshell:~$ strace ls
execve("/usr/bin/ls", ["ls"], 0x7fffabd610d0 /* 62 vars */) = 0
brk(NULL)                               = 0x5cc91f048000
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7be498b74000
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=35463, ...}) = 0
mmap(NULL, 35463, PROT_READ, MAP_PRIVATE, 3, 0) = 0x7be498b6b000
close(3)                                = 0
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libselinux.so.1", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\0\0\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0644, st_size=174472, ...}) = 0
mmap(NULL, 181960, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7be498b3e000
mmap(0x7be498b44000, 118784, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x6000) = 0x7be498b44000
mmap(0x7be498b61000, 24576, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x23000) = 0x7be498b61000
mmap(0x7be498b67000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x29000) = 0x7be498b67000
mmap(0x7be498b69000, 5832, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7be498b69000
close(3)                                = 0
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\220\243\2\0\0\0\0\0"..., 832) = 832
pread64(3, "\6\0\0\0\4\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0"..., 784, 64) = 784
fstat(3, {st_mode=S_IFREG|0755, st_size=2125328, ...}) = 0
pread64(3, "\6\0\0\0\4\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0"..., 784, 64) = 784
mmap(NULL, 2170256, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7be49892c000
mmap(0x7be498954000, 1605632, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x28000) = 0x7be498954000
mmap(0x7be498adc000, 323584, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1b0000) = 0x7be498adc000
mmap(0x7be498b2b000, 24576, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1fe000) = 0x7be498b2b000
mmap(0x7be498b31000, 52624, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7be498b31000
close(3)                                = 0
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libpcre2-8.so.0", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\0\0\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0644, st_size=625344, ...}) = 0
mmap(NULL, 627472, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7be498892000
mmap(0x7be498894000, 450560, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x2000) = 0x7be498894000
mmap(0x7be498902000, 163840, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x70000) = 0x7be498902000
mmap(0x7be49892a000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x97000) = 0x7be49892a000
close(3)                                = 0
mmap(NULL, 12288, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7be49888f000
arch_prctl(ARCH_SET_FS, 0x7be49888f800) = 0
set_tid_address(0x7be49888fad0)         = 1703
set_robust_list(0x7be49888fae0, 24)     = 0
rseq(0x7be498890120, 0x20, 0, 0x53053053) = 0
mprotect(0x7be498b2b000, 16384, PROT_READ) = 0
mprotect(0x7be49892a000, 4096, PROT_READ) = 0
mprotect(0x7be498b67000, 4096, PROT_READ) = 0
mprotect(0x5cc8e3dea000, 8192, PROT_READ) = 0
mprotect(0x7be498bac000, 8192, PROT_READ) = 0
prlimit64(0, RLIMIT_STACK, NULL, {rlim_cur=8192*1024, rlim_max=RLIM64_INFINITY}) = 0
munmap(0x7be498b6b000, 35463)           = 0
statfs("/sys/fs/selinux", 0x7ffdbca0aef0) = -1 ENOENT (No such file or directory)
statfs("/selinux", 0x7ffdbca0aef0)      = -1 ENOENT (No such file or directory)
getrandom("\x5c\x5d\xa1\xfa\x2b\xa7\x72\x3a", 8, GRND_NONBLOCK) = 8
brk(NULL)                               = 0x5cc91f048000
brk(0x5cc91f069000)                     = 0x5cc91f069000
openat(AT_FDCWD, "/proc/filesystems", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0444, st_size=0, ...}) = 0
read(3, "nodev\tsysfs\nnodev\ttmpfs\nnodev\tbd"..., 1024) = 390
read(3, "", 1024)                       = 0
close(3)                                = 0
access("/etc/selinux/config", F_OK)     = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/locale/locale-archive", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=3055776, ...}) = 0
mmap(NULL, 3055776, PROT_READ, MAP_PRIVATE, 3, 0) = 0x7be4985a4000
close(3)                                = 0
ioctl(1, TCGETS, {c_iflag=ICRNL|IXON|IUTF8, c_oflag=NL0|CR0|TAB0|BS0|VT0|FF0|OPOST|ONLCR, c_cflag=B38400|CS8|CREAD, c_lflag=ISIG|ICANON|ECHO|ECHOE|ECHOK|IEXTEN|ECHOCTL|ECHOKE, ...}) = 0
ioctl(1, TIOCGWINSZ, {ws_row=57, ws_col=241, ws_xpixel=0, ws_ypixel=0}) = 0
openat(AT_FDCWD, ".", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 3
fstat(3, {st_mode=S_IFDIR|0750, st_size=4096, ...}) = 0
getdents64(3, 0x5cc91f04ece0 /* 15 entries */, 32768) = 496
getdents64(3, 0x5cc91f04ece0 /* 0 entries */, 32768) = 0
close(3)                                = 0
fstat(1, {st_mode=S_IFCHR|0620, st_rdev=makedev(0x88, 0x1), ...}) = 0
write(1, "README-cloudshell.txt\n", 22README-cloudshell.txt
) = 22
close(1)                                = 0
close(2)                                = 0
exit_group(0)                           = ?
+++ exited with 0 +++
herefajri@cloudshell:~$ strace -e trace=open,read,write,close cat /etc/passwd
close(3)                                = 0
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\220\243\2\0\0\0\0\0"..., 832) = 832
close(3)                                = 0
close(3)                                = 0
read(3, "root:x:0:0:root:/root:/bin/bash\n"..., 131072) = 1419
write(1, "root:x:0:0:root:/root:/bin/bash\n"..., 1419root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
_apt:x:42:65534::/nonexistent:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:998:998:systemd Network Management:/:/usr/sbin/nologin
messagebus:x:100:101::/nonexistent:/usr/sbin/nologin
polkitd:x:997:997:User for polkitd:/:/usr/sbin/nologin
syslog:x:101:102::/nonexistent:/usr/sbin/nologin
dnsmasq:x:999:65534:dnsmasq:/var/lib/misc:/usr/sbin/nologin
dhcpcd:x:102:65534:DHCP Client Daemon,,,:/usr/lib/dhcpcd:/bin/false
redis:x:103:104::/var/lib/redis:/usr/sbin/nologin
sshd:x:104:65534::/run/sshd:/usr/sbin/nologin
postgres:x:105:106:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash
herefajri:x:1000:1000::/home/herefajri:/bin/bash
) = 1419
read(3, "", 131072)                     = 0
close(3)                                = 0
close(1)                                = 0
close(2)                                = 0
+++ exited with 0 +++
herefajri@cloudshell:~$ dmesg | tail -n 10
dmesg: read kernel buffer failed: Operation not permitted
herefajri@cloudshell:~$ sudo dmesg | tail -n 10
[ 4881.081745] sd 0:0:2:0: [sdb] Mode Sense: 1f 00 00 08
[ 4881.082058] sd 0:0:2:0: [sdb] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
[ 4881.182697]  sdb: sdb1
[ 4881.185436] sd 0:0:2:0: [sdb] Attached SCSI disk
[ 4881.414892] EXT4-fs (sdb1): mounted filesystem b9f0e455-8c03-483b-a0d6-629a47561fb9 r/w with ordered data mode. Quota mode: none.
[ 4882.630218] LoadPin: kernel-module pinning-excluded obj="/lib/modules/6.6.105+/kernel/net/ipv4/netfilter/iptable_nat.ko" pid=3205 cmdline="/sbin/modprobe -q -- iptable_nat"
[ 4882.819982] LoadPin: kernel-module pinning-excluded obj="/lib/modules/6.6.105+/kernel/net/netlink/netlink_diag.ko" pid=3232 cmdline="/sbin/modprobe -q -- net-pf-16-proto-4-type-16"
[ 4885.403388] LoadPin: kernel-module pinning-excluded obj="/lib/modules/6.6.105+/kernel/net/netfilter/ipset/ip_set.ko" pid=3509 cmdline="/sbin/modprobe -q -- ipt_set"
[ 4885.425745] LoadPin: kernel-module pinning-excluded obj="/lib/modules/6.6.105+/kernel/net/netfilter/xt_set.ko" pid=3509 cmdline="/sbin/modprobe -q -- ipt_set"
[ 4885.460154] LoadPin: kernel-module pinning-excluded obj="/lib/modules/6.6.105+/kernel/net/ipv6/netfilter/ip6table_nat.ko" pid=3515 cmdline="/sbin/modprobe -q -- ip6table_nat"
herefajri@cloudshell:~$
```
---

## Hasil Eksekusi
Screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/strace%20ls.png)
![Screenshot hasil](screenshots/DiagramStruktur%20SystemCalldanFungsiKernel.png)

---

## Analisis 1
- Jelaskan makna hasil percobaan.
**Jawaban:**

  1. `strace ls` untuk menampilkan setiap yang dipanggil dengan perintah ls (list directory contents) yang terlihat system call seperti `execve`,`openat`, `read`, `write`, dll (bisa dilihat pada "Hasil Eksekusi" diatas) dengan fungsi membuka membuka sistem seperti Glibc dan berkas konfigurasi dan dengan ini kita bisa menilai bahwa perintah sederhana juga perlu izin dari System Call.
  2. `strace -e trace=open,read,write,close cat /etc/passwd` input dimana membatasi output strace hanya pada System Call I/O dasar yaitu `open`, `read`, `write`, dan `close` yang dipanggil oleh perintah `cat `saat menampilkan isi berkas `/etc/passwd` (bisa dilihat pada "Hasil Eksekusi" diatas) dengan ini kita bisa mengamati bahwa input telah masuk (diizinkan) dan kernel bertugas untuk membaca, memproses, lalu memberikan output namun dengan batasan yaitu pada System Call I/O dasar saja.
  3. `dmesg | tail -n 10`   atau `sudo dmesg | tail -n 10`  (disini saya menambahkan `sudo` untuk mengizinkan akses ke kernel untuk sementara dikarenakan saya menggunakan `shell.cloud.google`) untuk menampilkan buffer pesan Kernel dengan isi informasi booting, driver hardware dan pesan diagnosik dari Kernel (log kernel), dan `| tail -n 10` untuk membatasi output hanya pada 10 baris terakhir. Dan ada hal menarik yang umum terjadi dimana ketika saya tak menambahkan `sudo` maka program akan mengeluarkan output `failed` yang mana membuktikan bahwa System Call bekerja dengan baik.              

- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).
**Jawaban:**
   1. Menujukkan bahwa semua layanan, perintah, dan sebagainya, harus melewati System Call yang dikelola Kernel.
   2. Adanya pemanggilan read oleh strace cat, disini menunjukkan bahwa Kernel melaksanakan tugas dan mengembalikannya ke program dan perintah dmesg memanggil Kernel untuk menampilkan pesan internal tentang inisialisasi driver ataupun hardware.
   3. Adanya input strace karena adanya perbedaan yang mana tak bisa ditembus dengan bebas dan percobaan ini memvalidasi arsitektur Dual-Mode Operation (Mode User dengan Mode Kernel).
      
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  
**Jawaban:**
Adanya perbedaan dari hasil input `strace`dimana:
   - Linux akan memunculkan rangkaian kata seperti `read(3,...)`
   - Sedangkan, untuk Windows akan jadi seperti `ReadFile(Handle,Buffer, Size,...)`
 
## Analisis 2 (Tugas & Quiz di docs Week-2)
Dokumentasikan hasil eksperimen strace dan dmesg dalam bentuk tabel observasi.
| No. | Perintah                                      | Tujuan Perintah                                                              | Hasil                                                                                 | Makna dan Analisis yang Didasarkan pada Percobaan dan Hasil                                                                              |
|-----|-----------------------------------------------|----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| 1   | `strace ls`                                   | Untuk menampilkan setiap yang dipanggil dengan perintah ls (list directory contents)                       | Terlihat system call seperti `execve`,`openat`, `read`, `write`, dll (bisa dilihat pada "Hasil Eksekusi" diatas).     | Dengan ini membuktikan bahwa perintah yang sifatnya sederhana seperti `ls` bergantung pada banyak system call untuk bekerja dan memperoleh izin ke kernel.   |
| 2   | `strace -e trace=open,read,write,close cat /etc/passwd` | Perintah dimana membatasi output strace hanya pada System Call I/O dasar yaitu `open`, `read`, `write`, dan `close` yang dipanggil oleh perintah `cat `saat menampilkan isi berkas `/etc/passwd` (bisa dilihat pada "Hasil Eksekusi" diatas).             | Terlihat urutan: `open(...)`, `read(...)`, `write(...)`,dsb.                        | Menunjukkan alur kerja kernel disaat membuka, membaca, menampilkan, dan menutup file.                   |
| 3   | `dmesg \| tail -n 10`   atau `sudo dmesg \| tail -n 10`  (disini saya menambahkan `sudo` untuk mengizinkan akses ke kernel untuk sementara )                 | untuk menampilkan buffer pesan Kernel dengan isi informasi booting, driver hardware dan pesan diagnosik dari Kernel, dan `\| tail -n 10` untuk membatasi output hanya pada 10 baris terakhir.                           | Output berisi informasi log booting, inisialisasi driver, dan pesan diagnostik sistem terkini                      | Memberikan wawasan tentang aktivitas kernel yang tidak terlihat oleh program pada umumnya, kecuali seperti percobaan saya dimana informasi yang sama bisa diakses jika diberi izin, seperti penggunaan `sudo` pada `shell.cloud.google` dengan input `dmesg`, dan bisa dilihat pada bagian "Hasil Eksekusi" diatas.                   |

Tulis analisis 400–500 kata tentang:
  - Mengapa system call penting untuk keamanan OS?
  - Bagaimana OS memastikan transisi user–kernel berjalan aman?
  - Sebutkan contoh system call yang sering digunakan di Linux.
  **Jawaban:**
    
Mengapa System Call itu Penting?

Jadi System Call merupakan suatu mekanisme yang mana berfungsi sebagai antarmuka (API) atau dengan kata lain memungkinkan program di user space untuk berinteraksi dengan kernel sistem operasi yang beroperasi di Kernel Mode. Dikarenakan Kernel mempunyai akses penuh ke banyak sumber daya perangkat dan data penting, disini System Call adalah Penjaga Gerbang atau memegang peran sebagai penjaga demi keamanan dan stabilitas OS agar aplikasi tak bisa dengan sembarangan mengakses bagian dalam OS, dan memastikan hanya permintaan tertentu atau khusus dengan memastikan hal-hal seperti kebenaran alamat memori, izin, dan hal-hal lainnya sebelum menjalankan operasi dan mengeksekusi ke tingkat kernel. 

Transisi user-kernel yang Aman

Untuk memastikan keamanan, transisi dari user mode ke kernel harus dipastikan oleh OS  terkait apakah statusnya aman atau tidak. Tapi transisi ini mungkin dilakukan melalui mekanisme yang disebut dengan Trap atau Interrupt;
1. Aplikasi Memulai Panggilan 
Ketika aplikasi ingin menjalankan operasi yang memerlukan hal khusus seperti halnya `read` atau `write`, operasi itu tak langsung menuju ke zona kode kernel, namun aplikasi menempatkan permintaan atau argumen untuk System Call yang diinginkan dengan lokasi yang ditentukan dan menjalankan instruksi khusus yang dikenal sebagai Trap/ Software Interrupt. 
2. Perubahan Mode CPU
Instruksi/ permintaan tadi memicu adanya Interrupt yang mana secara otomatis mengubah status CPU dari User Mode menjadi Kernel Mode.
3. Kernel Mulai Mengambil Kontrol
Dalam tahap ini, instruksi/permintaan masuk ke Kernel Mode, CPU masuk ke lokasi memori yang telah ditetapkan sebelumnya dalam tabel vektor Interrupt. Lokasi ini mengarah ke System Call Handler kernel yang mana akan membaca register CPU untuk mengindentifikasi System Call yang diminta dan memverifikasi parameter yang dilaporkan.
4. Eksekusi dan Pengembalian 
Setelah validasi dan eksekusi oprasi selesai, kernel memulihkan konteks dari CPU dan mengubah status kembali ke User Mode kembali sebelum mengembalikan kontrol ke aplikasi yang mengajukan permintaan sebelumnya.

Di dalam sistem operasi, khususnya Linux, terdapat banyak system call yang umum digunakan sehari-hari. Beberapa yang paling umum antara lain seperti:
- `read()` untuk membaca dan `write()` untuk menulis data, dari/ke file atau perangkat.
- `open()` untuk membuka dan `close()` untuk menutup, file.
- `fork()` untuk membuat proses baru.
- `execve()` untuk menjalankan program baru dalam proses yang sedang berjalan.
- `wait()` untuk menunggu proses anak (sekedar informasi, ada yang namanya Parent Process/ Proses Induk dan Child Process/Proses Anak) selesai.
- `exit()` untuk keluar dari proses.
- `mmap()` untuk memetakan file atau perangkat ke memori virtual.
- `ioctl()` untuk melakukan operasi khusus pada perangkat.
- `kill()` untuk mengirim sinyal ke proses lain.
---

## Kesimpulan
- System Call dan Transisi Mode adalah penghubung, perantara, dan penjaga keamanan dan stabilitas antara User Space dan Kernel Space
- Dalam praktikum menunjukkan bahwa perintah ls dan cat harus melewati System call dan begitu juga dmesg yang harus dipakaikan sudo jika anda menggunakan shell.cloud.google untuk prantikum ini
---

## Quiz
Quiz:

1. Apa fungsi utama system call dalam sistem operasi?
**Jawaban:** Fungsi utama System Call dalam system operasi adalah untuk menyaring tindakan yang mana bisa berbahaya bagi sistem operasi komputer. System Call ini memprioritaskan proteksi ketat layaknya anda ingin memverifikasi akun dengan akses yang terkontrol (seperti anda harus memberi izin, harus verifikasi dan semacamnya).

2. Sebutkan 4 kategori system call yang umum digunakan.
**Jawaban:**
- Kontrol Proses/Process Control: Fungsinya untuk mengelola pelaksanaan program seperti membuat proses baru seperti halnya fork atau exec.
- Manajemen Berkas/File Management: Fungsinya untuk menjalankan operasi terhadap berkas dan direktori seperti membuka/open dan menutup/close.
- Manajemen Perangkat/Device Management: Fungsinya untuk mengirim dan mengontrol hardware seperti meminta perangkat/request device.
- Pemeliharaan Informasi/Information Maintenance: Fungsinya untuk mengatur informasi sistem seperti mendapatkan waktu, tanggal, ID proses, atau jika dipersingkat intinya tentang sistem yang akan diambil.

3. Mengapa system call tidak bisa dipanggil langsung oleh user program?
**Jawaban:** Dikarenakan adanya System Call itu difungsikan untuk mencegah akses masuk dengan standar ketat atau analoginya seperti penjagaan militer, yang mana anda harus mengizinkan dulu dengan verifikasi kelas atas layaknya anda menghubungkan akun ke komputer lain, maka verifikasinya biasanya 3 tahap, tahap pemberian akses dengan mengetik username dan password, tahap mengkonfirmasi bahwa anda bukan robot dan tahap akhir yaitu pemberian kode verifikasi sebagai kunci akhir untuk masuk ke sistem. Layaknya sistem penjagaan militer namun versi dunia komputer dengan di tempatkan pada kondisi mengkaitkan akun, yang sama halnya dengan cara kerja system call yang mana system call akan memberi peringatan dulu dengan memverifikasi alamat dari sistem yang masuk.

---

## Refleksi Diri
Refleksi diri secara singkat:
- Apa bagian yang paling menantang minggu ini?
  **Jawaban:** Kesulitan dalam memahami materi dan maksud dari apa yang telah disampaikan dan yang ditugaskan.
- Bagaimana cara Anda mengatasinya?  
  **Jawaban:** Membaca, menganalogi, dan mempelajari ulang dan bertanya pada teman.
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
