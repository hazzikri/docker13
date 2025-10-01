# 🐍 Aplikasi Flask - Tutorial Docker

Aplikasi web sederhana menggunakan Python Flask untuk pembelajaran Docker bagi pemula.

## 📋 Deskripsi

Aplikasi ini menampilkan halaman web sederhana dengan pesan "Hello from Flask!" dan menyediakan endpoint API sederhana. Aplikasi ini dibuat untuk membantu pemula memahami cara menggunakan Docker untuk menjalankan aplikasi Python Flask.

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
cd flask-app

# Atau buat file manual sesuai struktur yang diberikan
```

### Langkah 3: Build Docker Image

```bash
# Build image dengan nama 'flask-app'
docker build -t flask-app .

# Verifikasi image berhasil dibuat
docker images
```

### Langkah 4: Jalankan Container

```bash
# Jalankan container di background dengan port mapping
docker run -d -p 5000:5000 --name flask-container flask-app

# Verifikasi container berjalan
docker ps
```

### Langkah 5: Akses Aplikasi

1. Buka browser dan akses: `http://<EC2-Public-IP>:5000`
2. Anda akan melihat halaman dengan pesan "Hello from Flask!"
3. Coba juga akses endpoint API: `http://<EC2-Public-IP>:5000/api/hello`

**Catatan Penting:**
- Pastikan Security Group EC2 instance Anda mengizinkan traffic pada port 5000
- Ganti `<EC2-Public-IP>` dengan alamat IP publik EC2 instance Anda

## 📱 Ekspektasi Hasil

Ketika aplikasi berhasil berjalan, Anda akan melihat:

1. **Halaman Utama** (`http://<EC2-Public-IP>:5000`):
   - Tampilan halaman web dengan background gradient biru-ungu
   - Judul "Hello from Flask!" dengan emoji ular
   - Badge hijau bertuliskan "Docker Container Berjalan"
   - Informasi framework, port, dan status
   - Link ke endpoint API

2. **Endpoint API** (`http://<EC2-Public-IP>:5000/api/hello`):
   - Response JSON: `{"message": "Hello from Flask API!", "status": "success"}`

## 🛠️ Perintah Docker Berguna

```bash
# Melihat container yang berjalan
docker ps

# Melihat semua container (termasuk yang berhenti)
docker ps -a

# Menghentikan container
docker stop flask-container

# Menjalankan kembali container yang sudah ada
docker start flask-container

# Melihat logs container
docker logs flask-container

# Masuk ke dalam container (debugging)
docker exec -it flask-container /bin/bash

# Menghapus container
docker rm flask-container

# Menghapus image
docker rmi flask-app
```

## 📝 PR (Pekerjaan Rumah)

### Tugas Praktik:

1. **Build dan Jalankan Aplikasi**
   - Lakukan build image untuk aplikasi Flask ini
   - Jalankan container dari image yang sudah dibuat
   - Pastikan aplikasi dapat diakses melalui browser

2. **Screenshot dan Dokumentasi**
   - Akses aplikasi melalui browser menggunakan Public IP EC2
   - Buat screenshot halaman utama aplikasi
   - Buat screenshot response dari endpoint `/api/hello`
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
   docker rm container_name → menghapus container
   docker rmi image_name → menghapus image
   docker logs container_name → melihat log output dari container
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
   docker version → melihat versi Docker yang terinstall
   ```

4. **Laporan Tugas**
   - Buat laporan sederhana berisi:
     - Screenshot aplikasi yang berjalan
     - Daftar 20+ perintah Docker dengan penjelasan
     - Kendala yang dihadapi (jika ada) dan cara mengatasinya
     - Kesimpulan pembelajaran

### 📤 Pengumpulan Tugas:

Kumpulkan file berikut:
- Screenshot aplikasi Flask yang berjalan di browser
- Screenshot response API endpoint
- File teks berisi daftar perintah Docker
- Laporan singkat pengalaman menggunakan Docker

---

**Selamat belajar Docker! 🐳**

*Tutorial ini dibuat untuk Aceng Academy - Docker Learning Path*