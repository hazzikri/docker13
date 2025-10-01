# ⚡ Aplikasi Express.js - Tutorial Docker

Aplikasi web sederhana menggunakan Node.js Express untuk pembelajaran Docker bagi pemula.

## 📋 Deskripsi

Aplikasi ini menampilkan halaman web interaktif dengan pesan "Hello from Express!" dan menyediakan beberapa endpoint API. Aplikasi ini dibuat untuk membantu pemula memahami cara menggunakan Docker untuk menjalankan aplikasi Node.js Express.

## 🚀 Cara Menjalankan di Ubuntu EC2 Instance

### Langkah 1: Install Docker

```bash
# Update package list
sudo apt update

# Install Docker
sudo apt install docker.io -y

# Start dan enable Docker service
sudo systemctl start docker
sudo systemctl enable docker

# Tambahkan user ke grup docker (opsional, untuk menjalankan docker tanpa sudo)
sudo usermod -aG docker $USER

# Logout dan login kembali, atau jalankan:
newgrp docker

# Verifikasi instalasi Docker
docker --version
```

### Langkah 2: Clone atau Download Source Code

```bash
# Jika menggunakan git
git clone <repository-url>
cd express-app

# Atau buat file manual sesuai struktur yang diberikan
```

### Langkah 3: Build Docker Image

```bash
# Build image dengan nama 'express-app'
docker build -t express-app .

# Verifikasi image berhasil dibuat
docker images
```

### Langkah 4: Jalankan Container

```bash
# Jalankan container di background dengan port mapping
docker run -d -p 3000:3000 --name express-container express-app

# Verifikasi container berjalan
docker ps
```

### Langkah 5: Akses Aplikasi

1. Buka browser dan akses: `http://<EC2-Public-IP>:3000`
2. Anda akan melihat halaman dengan pesan "Hello from Express!"
3. Coba juga akses endpoint berikut:
   - API: `http://<EC2-Public-IP>:3000/api/hello`
   - Health Check: `http://<EC2-Public-IP>:3000/health`

**Catatan Penting:**
- Pastikan Security Group EC2 instance Anda mengizinkan traffic pada port 3000
- Ganti `<EC2-Public-IP>` dengan alamat IP publik EC2 instance Anda

## 📱 Ekspektasi Hasil

Ketika aplikasi berhasil berjalan, Anda akan melihat:

1. **Halaman Utama** (`http://<EC2-Public-IP>:3000`):
   - Tampilan halaman web dengan background gradient biru
   - Ikon petir (⚡) dan judul "Hello from Express!"
   - Badge hijau bertuliskan "Node.js Container Active"
   - Informasi framework, port, status, dan environment
   - Tombol link ke API endpoint dan health check
   - Animasi sederhana pada badge

2. **Endpoint API** (`http://<EC2-Public-IP>:3000/api/hello`):
   - Response JSON dengan message, status, dan timestamp

3. **Health Check** (`http://<EC2-Public-IP>:3000/health`):
   - Response JSON: `{"status": "OK", "service": "Express App"}`

## 🛠️ Perintah Docker Berguna

```bash
# Melihat container yang berjalan
docker ps

# Melihat semua container (termasuk yang berhenti)
docker ps -a

# Menghentikan container
docker stop express-container

# Menjalankan kembali container yang sudah ada
docker start express-container

# Melihat logs container
docker logs express-container

# Melihat logs secara real-time
docker logs -f express-container

# Masuk ke dalam container (debugging)
docker exec -it express-container /bin/sh

# Menghapus container
docker rm express-container

# Menghapus image
docker rmi express-app
```

## 🔧 Troubleshooting

### Masalah Umum:

1. **Port sudah digunakan:**
   ```bash
   # Cek proses yang menggunakan port 3000
   sudo lsof -i :3000
   
   # Atau gunakan port lain
   docker run -d -p 8080:3000 --name express-container express-app
   ```

2. **Container tidak bisa diakses:**
   - Pastikan Security Group mengizinkan port 3000
   - Cek apakah container benar-benar berjalan: `docker ps`
   - Cek logs untuk error: `docker logs express-container`

3. **Build gagal:**
   - Pastikan file package.json ada dan valid
   - Cek koneksi internet untuk download dependencies

## 📝 PR (Pekerjaan Rumah)

### Tugas Praktik:

1. **Build dan Jalankan Aplikasi**
   - Lakukan build image untuk aplikasi Express ini
   - Jalankan container dari image yang sudah dibuat
   - Pastikan aplikasi dapat diakses melalui browser

2. **Screenshot dan Dokumentasi**
   - Akses aplikasi melalui browser menggunakan Public IP EC2
   - Buat screenshot halaman utama aplikasi
   - Buat screenshot response dari endpoint `/api/hello`
   - Buat screenshot response dari endpoint `/health`
   - Simpan screenshot sebagai bukti tugas

3. **Eksplorasi Docker Commands**
   - Buat daftar minimal 20 perintah Docker beserta penjelasan fungsinya
   - Format: `perintah` → penjelasan singkat
   - Contoh yang harus disertakan:

   ```
   docker ps → menampilkan daftar container yang sedang berjalan
   docker images → menampilkan daftar image yang tersedia
   docker build -t nama . → membuild image dari Dockerfile dengan tag nama
   docker run -d -p host:container image → menjalankan container di background dengan port mapping
   docker stop container_name → menghentikan container yang berjalan
   docker start container_name → menjalankan kembali container yang sudah ada
   docker restart container_name → restart container yang berjalan
   docker rm container_name → menghapus container
   docker rmi image_name → menghapus image
   docker logs container_name → melihat log output dari container
   docker logs -f container_name → melihat log secara real-time
   docker exec -it container_name /bin/bash → masuk ke dalam container secara interaktif
   docker pull image_name → download image dari Docker Hub
   docker push image_name → upload image ke Docker Hub
   docker inspect container_name → melihat detail informasi container
   docker stats → melihat penggunaan resource container secara real-time
   docker network ls → melihat daftar network Docker
   docker volume ls → melihat daftar volume Docker
   docker system prune → membersihkan resource Docker yang tidak terpakai
   docker-compose up → menjalankan multi-container dengan docker-compose
   docker-compose down → menghentikan dan menghapus container dari docker-compose
   ```

4. **Eksperimen Tambahan**
   - Coba jalankan container dengan port yang berbeda
   - Coba akses container dari dalam menggunakan `docker exec`
   - Bandingkan performa dengan aplikasi yang berjalan langsung di host

5. **Laporan Tugas**
   - Buat laporan sederhana berisi:
     - Screenshot aplikasi yang berjalan
     - Screenshot semua endpoint yang tersedia
     - Daftar 20+ perintah Docker dengan penjelasan
     - Perbandingan dengan aplikasi Flask (jika sudah dikerjakan)
     - Kendala yang dihadapi (jika ada) dan cara mengatasinya
     - Kesimpulan pembelajaran

### 📤 Pengumpulan Tugas:

Kumpulkan file berikut:
- Screenshot aplikasi Express yang berjalan di browser
- Screenshot response dari semua endpoint API
- File teks berisi daftar perintah Docker
- Laporan perbandingan dengan aplikasi lain
- Dokumentasi eksperimen yang dilakukan

---

**Selamat belajar Docker dengan Node.js! 🚀**

*Tutorial ini dibuat untuk Aceng Academy - Docker Learning Path*