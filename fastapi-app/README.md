# 🚀 Aplikasi FastAPI - Tutorial Docker

Aplikasi web modern menggunakan Python FastAPI untuk pembelajaran Docker bagi pemula dengan fokus pada performa tinggi dan dokumentasi API otomatis.

## 📋 Deskripsi

Aplikasi ini menampilkan halaman web interaktif dengan pesan "Hello from FastAPI!" dan menyediakan beberapa endpoint API dengan dokumentasi otomatis. FastAPI adalah framework Python modern yang sangat cepat dan mudah digunakan untuk membangun API.

## ✨ Fitur Unggulan FastAPI

- 🚀 **Performa Tinggi**: Salah satu framework Python tercepat
- 📚 **Dokumentasi Otomatis**: Swagger UI dan ReDoc terintegrasi
- 🔍 **Type Hints**: Validasi data otomatis dengan Pydantic
- ⚡ **Async/Await**: Dukungan penuh untuk operasi asynchronous
- 🛡️ **Keamanan**: Built-in security features

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
cd fastapi-app

# Atau buat file manual sesuai struktur yang diberikan
```

### Langkah 3: Build Docker Image

```bash
# Build image dengan nama 'fastapi-app'
docker build -t fastapi-app .

# Verifikasi image berhasil dibuat
docker images
```

### Langkah 4: Jalankan Container

```bash
# Jalankan container di background dengan port mapping
docker run -d -p 8000:8000 --name fastapi-container fastapi-app

# Verifikasi container berjalan
docker ps
```

### Langkah 5: Akses Aplikasi

1. **Halaman Utama**: `http://<EC2-Public-IP>:8000`
2. **API Endpoints**:
   - Hello API: `http://<EC2-Public-IP>:8000/api/hello`
   - App Info: `http://<EC2-Public-IP>:8000/api/info`
   - Health Check: `http://<EC2-Public-IP>:8000/health`
3. **Dokumentasi API**:
   - Swagger UI: `http://<EC2-Public-IP>:8000/docs`
   - ReDoc: `http://<EC2-Public-IP>:8000/redoc`

**Catatan Penting:**
- Pastikan Security Group EC2 instance Anda mengizinkan traffic pada port 8000
- Ganti `<EC2-Public-IP>` dengan alamat IP publik EC2 instance Anda

## 📱 Ekspektasi Hasil

Ketika aplikasi berhasil berjalan, Anda akan melihat:

### 1. Halaman Utama (`http://<EC2-Public-IP>:8000`)
- Tampilan modern dengan background gradient
- Logo roket (🚀) dan judul "Hello from FastAPI!"
- Badge animasi "High Performance API Container"
- Grid informasi dengan 4 kartu (Framework, Port, Status, Environment)
- Daftar fitur FastAPI
- Tombol link ke berbagai endpoint dan dokumentasi
- Animasi loading pada kartu informasi

### 2. API Endpoints
- **Hello API** (`/api/hello`): Response JSON dengan message, status, timestamp, framework, dan python version
- **App Info** (`/api/info`): Informasi aplikasi lengkap termasuk link dokumentasi
- **Health Check** (`/health`): Status kesehatan aplikasi dengan timestamp

### 3. Dokumentasi API Otomatis
- **Swagger UI** (`/docs`): Interface interaktif untuk testing API
- **ReDoc** (`/redoc`): Dokumentasi API yang lebih detail dan readable

## 🛠️ Perintah Docker Berguna

```bash
# Melihat container yang berjalan
docker ps

# Melihat semua container (termasuk yang berhenti)
docker ps -a

# Menghentikan container
docker stop fastapi-container

# Menjalankan kembali container yang sudah ada
docker start fastapi-container

# Melihat logs container
docker logs fastapi-container

# Melihat logs secara real-time
docker logs -f fastapi-container

# Masuk ke dalam container (debugging)
docker exec -it fastapi-container /bin/bash

# Melihat resource usage
docker stats fastapi-container

# Menghapus container
docker rm fastapi-container

# Menghapus image
docker rmi fastapi-app
```

## 🔧 Troubleshooting

### Masalah Umum:

1. **Port sudah digunakan:**
   ```bash
   # Cek proses yang menggunakan port 8000
   sudo lsof -i :8000
   
   # Atau gunakan port lain
   docker run -d -p 9000:8000 --name fastapi-container fastapi-app
   ```

2. **Container tidak bisa diakses:**
   - Pastikan Security Group mengizinkan port 8000
   - Cek apakah container benar-benar berjalan: `docker ps`
   - Cek logs untuk error: `docker logs fastapi-container`

3. **Build gagal:**
   - Pastikan file requirements.txt ada dan valid
   - Cek koneksi internet untuk download dependencies
   - Pastikan struktur direktori sesuai dengan Dockerfile

4. **Import error:**
   - Pastikan semua dependencies terinstall dengan benar
   - Cek versi Python yang digunakan

## 🎯 Keunggulan FastAPI vs Framework Lain

| Fitur | FastAPI | Flask | Express |
|-------|---------|-------|---------|
| Performa | ⚡ Sangat Tinggi | 🐌 Sedang | 🚀 Tinggi |
| Dokumentasi API | ✅ Otomatis | ❌ Manual | ❌ Manual |
| Type Validation | ✅ Built-in | ❌ Manual | ❌ Manual |
| Async Support | ✅ Native | ⚠️ Limited | ✅ Native |
| Learning Curve | 📈 Mudah | 📈 Mudah | 📈 Mudah |

## 📝 PR (Pekerjaan Rumah)

### Tugas Praktik:

1. **Build dan Jalankan Aplikasi**
   - Lakukan build image untuk aplikasi FastAPI ini
   - Jalankan container dari image yang sudah dibuat
   - Pastikan aplikasi dapat diakses melalui browser

2. **Screenshot dan Dokumentasi**
   - Akses aplikasi melalui browser menggunakan Public IP EC2
   - Buat screenshot halaman utama aplikasi
   - Buat screenshot dari semua endpoint API:
     - `/api/hello`
     - `/api/info`
     - `/health`
   - Buat screenshot dokumentasi Swagger UI (`/docs`)
   - Buat screenshot dokumentasi ReDoc (`/redoc`)
   - Simpan semua screenshot sebagai bukti tugas

3. **Eksplorasi Fitur FastAPI**
   - Coba gunakan Swagger UI untuk testing API
   - Bandingkan dokumentasi Swagger UI vs ReDoc
   - Coba akses endpoint yang tidak ada dan lihat error handling

4. **Eksplorasi Docker Commands**
   - Buat daftar minimal 25 perintah Docker beserta penjelasan fungsinya
   - Fokus pada perintah yang berguna untuk development dan production
   - Format: `perintah` → penjelasan singkat

   **Contoh yang harus disertakan:**
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
   docker inspect container_name → melihat detail informasi container
   docker stats → melihat penggunaan resource semua container
   docker stats container_name → melihat penggunaan resource container tertentu
   docker pull image_name → download image dari Docker Hub
   docker push image_name → upload image ke Docker Hub
   docker network ls → melihat daftar network Docker
   docker network create network_name → membuat network baru
   docker volume ls → melihat daftar volume Docker
   docker volume create volume_name → membuat volume baru
   docker system prune → membersihkan resource Docker yang tidak terpakai
   docker system df → melihat penggunaan disk Docker
   docker-compose up → menjalankan multi-container dengan docker-compose
   docker-compose down → menghentikan dan menghapus container dari docker-compose
   docker version → melihat versi Docker yang terinstall
   ```

5. **Perbandingan Framework**
   - Bandingkan FastAPI dengan Flask dan Express (jika sudah dikerjakan)
   - Buat tabel perbandingan fitur, performa, dan kemudahan penggunaan
   - Berikan kesimpulan framework mana yang paling cocok untuk berbagai use case

6. **Eksperimen Lanjutan**
   - Coba modifikasi kode untuk menambah endpoint baru
   - Coba jalankan container dengan environment variables
   - Coba mount volume untuk persistent data

7. **Laporan Tugas**
   - Buat laporan komprehensif berisi:
     - Screenshot semua halaman dan endpoint
     - Screenshot dokumentasi API (Swagger UI dan ReDoc)
     - Daftar 25+ perintah Docker dengan penjelasan
     - Perbandingan dengan framework lain
     - Analisis keunggulan dan kekurangan FastAPI
     - Eksperimen yang dilakukan dan hasilnya
     - Kendala yang dihadapi dan cara mengatasinya
     - Kesimpulan dan rekomendasi

### 📤 Pengumpulan Tugas:

Kumpulkan file berikut:
- Screenshot aplikasi FastAPI yang berjalan di browser
- Screenshot semua endpoint API
- Screenshot dokumentasi Swagger UI dan ReDoc
- File teks berisi daftar perintah Docker
- Tabel perbandingan framework
- Laporan eksperimen dan analisis
- Dokumentasi modifikasi kode (jika ada)

### 🏆 Bonus Challenge:

1. **Custom Endpoint**: Tambahkan endpoint baru yang menerima parameter
2. **Error Handling**: Buat endpoint yang mendemonstrasikan error handling
3. **Environment Variables**: Gunakan environment variables untuk konfigurasi
4. **Health Check**: Implementasikan health check yang lebih detail
5. **Logging**: Tambahkan logging untuk monitoring aplikasi

---

**Selamat belajar Docker dengan FastAPI! 🚀⚡**

*FastAPI + Docker = The Future of API Development*

*Tutorial ini dibuat untuk Aceng Academy - Docker Learning Path*