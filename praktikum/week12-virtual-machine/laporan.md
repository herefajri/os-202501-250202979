
# Laporan Praktikum Minggu 12
Topik: Virtualisasi Menggunakan Virtual Machine 

---

## Identitas
- **Nama**  : Muhammad Fajri Abdullah 
- **NIM**   : 250202979
- **Kelas** : 1IKRB

---

## Tujuan
1. Menginstal perangkat lunak virtualisasi (VirtualBox/VMware).  
2. Membuat dan menjalankan sistem operasi guest di dalam VM.  
3. Mengatur konfigurasi resource VM (CPU, RAM, storage).  
4. Menjelaskan mekanisme proteksi OS melalui virtualisasi.  
5. Menyusun laporan praktikum instalasi dan konfigurasi VM secara sistematis.

---

## Dasar Teori
1. Konsep Virtual Machine (VM): Virtual Machine diabstraksikan sebagai perangkat keras komputer (CPU, memori, disk) ke dalam beberapa lingkungan eksekusi yang berbeda. Sistem operasi guest (Lubuntu) berjalan di atas Virtual Machine Monitor (Hypervisor seperti VirtualBox) yang menciptakan ilusi bahwa OS tersebut memiliki perangkat kerasnya sendiri.
2. Isolasi dan Keamanan (Protection): Salah satu prinsip utama virtualisasi adalah isolasi total. Masalah atau crash yang terjadi pada sistem guest (seperti "lag parah" yang Anda alami) tidak akan mempengaruhi sistem host (Windows) atau VM lainnya karena setiap VM berjalan dalam lingkungannya sendiri yang terisolasi.
3. Alokasi Sumber Daya (Resource Allocation): Sistem operasi bertanggung jawab untuk mengelola resource seperti CPU dan RAM. Dalam virtualisasi, jumlah resource yang diberikan kepada VM diambil dari resource fisik sistem host. Perubahan jumlah CPU dan RAM yang Anda lakukan secara langsung mempengaruhi throughput dan waktu respons sistem guest.
4. Manajemen Memori dan Swapping: Ketika RAM (memori fisik) yang dialokasikan ke VM terlalu kecil (seperti saat Anda mencoba 1 GB), sistem akan melakukan swapping atau menggunakan area di secondary storage sebagai memori tambahan. Hal ini menyebabkan penurunan performa yang drastis karena kecepatan akses disk jauh lebih lambat dibandingkan RAM.
5. Multiprocessing Virtual: Dengan mengonfigurasi jumlah CPU lebih dari satu (misalnya 4 CPU), sistem operasi dapat menjalankan beberapa instruksi secara paralel. Ini meningkatkan kemampuan sistem dalam menangani beban kerja berat meskipun memori fisik yang tersedia terbatas.

---

## Langkah Praktikum
1. **Instalasi Virtual Machine**
   - Instal VirtualBox atau VMware pada komputer host.  
   - Pastikan fitur virtualisasi (VT-x / AMD-V) aktif di BIOS.

2. **Pembuatan OS Guest**
   - Buat VM baru dan pilih OS guest (disini saya menggunakan Oracle Virtual Box dan Lubuntu 24.04.3).  
   - Atur resource awal:
     - CPU: 1–2 core  
     - RAM: 2–4 GB  
     - Storage: ≥ 20 GB 

3. **Instalasi Sistem Operasi**
   - Jalankan proses instalasi OS guest sampai selesai.  
   - Pastikan OS guest dapat login dan berjalan normal.

4. **Konfigurasi Resource**
   - Ubah konfigurasi CPU dan RAM.  
   - Amati perbedaan performa sebelum dan sesudah perubahan resource.

5. **Analisis Proteksi OS**
   - Jelaskan bagaimana VM menyediakan isolasi antara host dan guest.  
   - Kaitkan dengan konsep *sandboxing* dan *hardening* OS.

6. **Dokumentasi**
   - Ambil screenshot setiap tahap penting.  
   - Simpan di folder `screenshots/`.

7. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 12 - Virtual Machine"
   git push origin main
   ```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/instalasi_vm.png)

Gambar Konfigurasi Resource (RAM 2, CPU 1):

![Screenshot hasil](screenshots/konfigurasi_resource_(ram_2_cpu_1).png)


Gambar Konfigurasi Resource (RAM 2, CPU 2):

![Screenshot hasil](screenshots/konfigurasi_resource_(ram_2_cpu_2).png)

Gambar Konfigurasi Resource (RAM 4, CPU 1):

![Screenshot hasil](screenshots/konfigurasi_resource_(ram_4_cpu_1).png)

Gambar Konfigurasi Resource (RAM 4, CPU 2):

![Screenshot hasil](screenshots/konfigurasi_resource_(ram_4_cpu_2).png)

Gambar OS Guest Running (RAM 2, CPU 1):

![Screenshot hasil](screenshots/os_guest_running_(ram_2_cpu_1).png)

Gambar OS Guest Running (RAM 2, CPU 1) versi hitung ulang:

![Screenshot hasil](screenshots/os_guest_running_(ram_2_cpu_1_repeat).png)

Gambar OS Guest Running (RAM 2, CPU 2):

![Screenshot hasil](screenshots/os_guest_running_(ram_2_cpu_2).png)

Gambar OS Guest Running (RAM 4, CPU 1):

![Screenshot hasil](screenshots/os_guest_running_(ram_4_cpu_1).png)


Gambar OS Guest Running (RAM 4, CPU 2)

![Screenshot hasil](screenshots/os_guest_running_(ram_4_cpu_2).png)

## Hasil Observasi Berdasarkan Skenario Resource
Pengujian dilakukan dengan menggunakan aplikasi browser Mozilla Firefox sebagai standar beban kerja. Berikut adalah analisis untuk setiap konfigurasi:

A. Skenario RAM 2 GB & CPU 1 Core
- Performa: Membutuhkan waktu sekitar 16 detik untuk membuka browser pada percobaan awal, dan 6 detik pada percobaan ulang.
- Kondisi Sistem: Menunjukkan utilisasi CPU yang sangat tinggi hingga menyentuh angka 100%.
- Kesimpulan: Meskipun browser bisa terbuka cepat pada pengujian ulang, pengalaman pengguna terasa "kaku" dan tidak responsif (lag) karena satu-satunya inti prosesor dipaksa bekerja maksimal untuk menangani sistem dan aplikasi sekaligus.

B. Skenario RAM 2 GB & CPU 2 Core
Performa: Waktu respon meningkat menjadi 7 detik.
- Kondisi Sistem: Beban kerja terbagi secara paralel ke dua inti prosesor (masing-masing di kisaran 80-88%).
- Kesimpulan: Penambahan Core CPU secara signifikan mengurangi kekakuan sistem dibandingkan penggunaan single-core, meskipun kapasitas RAM masih terbatas.

C. Skenario RAM 4 GB & CPU 1 Core
- Performa: Waktu respon tercatat stabil di angka 6 detik.
- Kondisi Sistem: CPU bekerja di kisaran 86.5%, tidak lagi menyentuh batas kritis 100%.
- Kesimpulan: Kapasitas RAM yang lebih besar memberikan ruang bagi sistem untuk melakukan manajemen memori yang lebih baik, mengurangi ketergantungan pada swap disk, sehingga sistem terasa lebih ringan meskipun hanya menggunakan satu inti CPU.

D. Skenario RAM 4 GB & CPU 2 Core
- Performa: Mencapai waktu respon tercepat, yaitu 5 detik.
- Kondisi Sistem: Penggunaan CPU dan RAM berada pada level yang sangat ideal dan stabil.
- Kesimpulan: Ini merupakan konfigurasi paling optimal. Kombinasi RAM yang luas dan distribusi beban multi-core memberikan pengalaman penggunaan yang paling lancar dan responsif.

## Analisis Proteksi dan Keamanan Sistem
Eksperimen ini sekaligus mendemonstrasikan tiga pilar utama keamanan sistem operasi melalui Virtual Machine:
- Isolasi (Sandboxing): Seluruh kegagalan sistem (seperti error data korup di awal) terbukti hanya terjadi di dalam lingkungan virtual tanpa mempengaruhi stabilitas Windows sebagai Host.
- Resource Hardening: Pembatasan alokasi RAM dan CPU berfungsi untuk mengunci sumber daya. Hal ini mencegah Guest OS mengonsumsi seluruh daya komputasi fisik yang dapat menyebabkan Host mengalami freeze.
- Abstraksi Hardware: VM bertindak sebagai perantara yang mengamankan hardware fisik dari interaksi langsung dengan sistem operasi Guest, meminimalisir risiko eksploitasi pada level firmware.

## Kesimpulan Akhir
Berdasarkan seluruh rangkaian percobaan, ditemukan bahwa sistem operasi modern seperti Lubuntu tetap membutuhkan keseimbangan antara kapasitas memori dan jumlah inti prosesor. Konfigurasi RAM 4 GB dengan 2 CPU Core direkomendasikan sebagai standar minimum untuk mendapatkan performa yang stabil dan aman dalam lingkungan virtualisasi.


---

## Analisis 
- Jelaskan bagaimana VM menyediakan isolasi antara host dan guest.  
   **Jawaban:** 

   Virtual Machine (VM) menyediakan isolasi melalui lapisan yang disebut Hypervisor (dalam hal ini VirtualBox). Berikut adalah mekanisme isolasinya:
   - Abstraksi Hardware: Hypervisor menciptakan lapisan hardware virtual (CPU, RAM, Disk) yang terpisah dari hardware fisik. Guest OS (Lubuntu) merasa berjalan di komputer asli, padahal ia hanya mengakses "tiruan" hardware yang dikelola oleh Host (Windows).
   - Pemisahan Memori: RAM yang Anda alokasikan (misalnya 2 GB atau 4 GB) dikunci oleh Hypervisor hanya untuk digunakan oleh Guest. Guest OS tidak memiliki akses ke alamat memori yang digunakan oleh Host atau aplikasi lain di luar VM tersebut.
   - Isolasi Kegagalan (Fault Isolation): Jika Guest OS mengalami beban kerja berlebih hingga CPU mencapai 100% atau bahkan mengalami crash (seperti pada percobaan 1 CPU), sistem Host tetap berjalan stabil tanpa terganggu karena kegagalan tersebut terkurung di dalam lingkungan virtual.


- Kaitkan dengan konsep *sandboxing* dan *hardening* OS.
   **Jawaban:** 

   **Konsep Sandboxing**

   VM bertindak sebagai Sandbox (kotak pasir) yang sempurna. Dalam percobaan Anda, hal ini terlihat dari:
   - Lingkungan Uji yang Aman: Segala aktivitas yang dilakukan di dalam Lubuntu, seperti membuka browser Mozilla Firefox atau menjalankan perintah terminal, tidak akan memengaruhi integritas file sistem di Windows.
   - Pembatasan Dampak: Jika terdapat proses berbahaya atau error di dalam Guest OS, dampak negatifnya hanya akan terjadi di dalam "kotak" VM tersebut. Host tetap aman karena tidak ada jalur komunikasi langsung kecuali jika dikonfigurasi secara sengaja (seperti Shared Folder).

   **Konsep Hardening OS**
   Hardening adalah tindakan untuk memperkuat keamanan sistem dengan meminimalkan permukaan serangan. Penggunaan VM mendukung hal ini melalui:
   - Pembatasan Sumber Daya (Resource Limit): Dengan menetapkan batas RAM dan CPU, Anda melakukan hardening pada sisi Host. Ini memastikan bahwa Guest OS tidak dapat "memakan" seluruh sumber daya fisik (misalnya mencegah Guest menggunakan 100% RAM fisik), sehingga performa Host tetap terjaga.
   - Minimalisasi Risiko: Dengan menjalankan aplikasi tertentu (misalnya browser untuk riset) di dalam VM, Anda memperkecil celah keamanan pada OS Host. Jika browser di Guest terkena serangan, OS utama Anda (Host) tidak langsung terpapar karena terproteksi oleh lapisan virtualisasi tersebut.

---

## Kesimpulan
- Efisiensi Resource Berbanding Lurus dengan Responsivitas Sistem Berdasarkan hasil eksperimen, alokasi resource memiliki ambang batas minimum untuk kenyamanan penggunaan. Meskipun sistem dapat berjalan dengan 1 CPU dan RAM 2 GB, kondisi tersebut menyebabkan beban kerja CPU mencapai 100% dan sistem terasa kaku. Peningkatan ke RAM 4 GB dan 2 CPU terbukti paling optimal, mampu memangkas waktu tunggu pembukaan aplikasi dari 16 detik menjadi 5 detik saja.

- Keamanan Melalui Isolasi dan Sandboxing Penggunaan VM berhasil mendemonstrasikan konsep sandboxing, di mana Guest OS (Lubuntu) beroperasi dalam lingkungan yang sepenuhnya terisolasi dari Host (Windows). Segala beban kerja berat atau potensi kegagalan sistem di dalam Guest terbukti hanya berdampak di dalam lingkup virtualisasi tersebut tanpa mengganggu integritas dan stabilitas sistem operasi utama pada komputer fisik.

- Penerapan Hardening OS pada Host Pembatasan sumber daya (RAM dan CPU) yang dilakukan selama percobaan merupakan bentuk nyata dari hardening OS. Dengan mengunci alokasi resource bagi VM, Host secara otomatis terlindungi dari risiko pemborosan sumber daya (resource exhaustion). Hal ini memastikan bahwa sistem Host tetap memiliki cadangan performa yang cukup untuk menjalankan fungsi kritis lainnya meskipun Guest OS sedang bekerja pada kapasitas maksimal.

---

## Quiz
1. Apa perbedaan antara host OS dan guest OS? 
    **Jawaban:**  
      - Host OS adalah sistem operasi utama yang terinstal langsung pada perangkat keras fisik (seperti Windows pada laptop Samsung Anda). Host OS memiliki kendali penuh terhadap seluruh hardware dan bertanggung jawab untuk menjalankan aplikasi hypervisor.
      - Guest OS adalah sistem operasi yang berjalan di dalam lingkungan virtual (seperti Lubuntu). Guest OS terisolasi dari perangkat keras fisik dan hanya dapat mengakses sumber daya (CPU, RAM, Disk) yang telah dialokasikan atau dijatahkan oleh hypervisor.


2. Apa peran hypervisor dalam virtualisasi?  
    **Jawaban:**  
      Hypervisor (atau Virtual Machine Monitor) berperan sebagai lapisan perantara yang mengelola dan membagi sumber daya fisik dari host ke beberapa guest. Fungsi utamanya adalah melakukan abstraksi hardware, memastikan setiap VM merasa memiliki perangkat kerasnya sendiri, serta melakukan penjadwalan (scheduling) penggunaan CPU dan memori agar beberapa sistem operasi dapat berjalan secara paralel pada satu mesin fisik tanpa saling mengintervensi.


3. Mengapa virtualisasi meningkatkan keamanan sistem?    
    **Jawaban:**
      - Isolasi: Setiap VM berjalan dalam lingkungan yang terpisah. Jika guest OS terkena serangan malware atau mengalami kegagalan sistem, dampaknya tidak akan menyebar ke sistem host atau VM lainnya.
      - Sandboxing: Aktivitas di dalam VM dibatasi pada "kotak pasir" virtualnya sendiri. Hal ini memungkinkan pengguna untuk menguji aplikasi atau konfigurasi yang berisiko tinggi tanpa mengancam integritas data atau stabilitas sistem operasi utama pada perangkat fisik.



---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
