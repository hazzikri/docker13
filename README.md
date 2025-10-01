# 🐳 Docker Tutorial - 3 Aplikasi Web Sederhana

Repository ini berisi 3 aplikasi web sederhana untuk pembelajaran Docker bagi pemula. Setiap aplikasi menggunakan framework yang berbeda untuk memberikan pengalaman belajar yang komprehensif.

## 📁 Struktur Project

```
Docker/
├── flask-app/          # Aplikasi Python Flask
│   ├── app.py
│   ├── templates/
│   │   └── index.html
│   ├── requirements.txt
│   ├── Dockerfile
│   └── README.md
├── express-app/        # Aplikasi Node.js Express
│   ├── index.js
│   ├── public/
│   │   └── index.html
│   ├── package.json
│   ├── Dockerfile
│   └── README.md
├── fastapi-app/        # Aplikasi Python FastAPI
│   ├── main.py
│   ├── templates/
│   │   └── index.html
│   ├── static/
│   ├── requirements.txt
│   ├── Dockerfile
│   └── README.md
└── README.md           # File ini
```

## 🚀 Aplikasi yang Tersedia

### 1. 🐍 Flask App (Port 5000)
- **Framework**: Python Flask
- **Fitur**: Halaman web sederhana + API endpoint
- **URL**: `http://<EC2-IP>:5000`
- **API**: `/api/hello`

### 2. ⚡ Express App (Port 3000)
- **Framework**: Node.js Express
- **Fitur**: Halaman web interaktif + multiple endpoints
- **URL**: `http://<EC2-IP>:3000`
- **API**: `/api/hello`, `/health`

### 3. 🚀 FastAPI App (Port 8000)
- **Framework**: Python FastAPI
- **Fitur**: Halaman web modern + dokumentasi API otomatis
- **URL**: `http://<EC2-IP>:8000`
- **API**: `/api/hello`, `/api/info`, `/health`
- **Docs**: `/docs` (Swagger UI), `/redoc` (ReDoc)

## 🎯 Tujuan Pembelajaran

Tutorial ini dirancang untuk membantu pemula memahami:

1. **Konsep Dasar Docker**
   - Apa itu container dan image
   - Cara membuat Dockerfile
   - Build dan run container

2. **Praktik Docker**
   - Build image dari source code
   - Menjalankan container dengan port mapping
   - Debugging dan troubleshooting

3. **Perbandingan Framework**
   - Flask vs Express vs FastAPI
   - Kelebihan dan kekurangan masing-masing
   - Use case yang tepat untuk setiap framework

## 🔧 Quick Start

### Prasyarat
- Ubuntu EC2 instance
- Akses SSH ke EC2 instance
- Koneksi internet yang stabil

### Langkah 1: Install Docker di Ubuntu EC2

```bash
# Update package list
sudo apt update

# Install Docker
sudo apt install docker.io -y

# Start dan enable Docker service
sudo systemctl start docker
sudo systemctl enable docker

# Tambahkan user ke grup docker (opsional)
sudo usermod -aG docker $USER
newgrp docker

# Verifikasi instalasi
docker --version
docker run hello-world
```

### Langkah 2: Konfigurasi Security Group EC2

Pastikan Security Group mengizinkan traffic pada port:
- **Port 22**: SSH access
- **Port 3000**: Express App
- **Port 5000**: Flask App  
- **Port 8000**: FastAPI App

**Cara setting**: AWS Console → EC2 → Security Groups → Edit inbound rules → Add rule untuk setiap port dengan source 0.0.0.0/0

### Langkah 3: Menjalankan Aplikasi Satu per Satu

```bash
# Clone repository
git clone <repository-url>
cd Docker

# Build dan jalankan Flask App
cd flask-app
docker build -t flask-app .
docker run -d -p 5000:5000 --name flask-container flask-app
cd ..

# Build dan jalankan Express App
cd express-app
docker build -t express-app .
docker run -d -p 3000:3000 --name express-container express-app
cd ..

# Build dan jalankan FastAPI App
cd fastapi-app
docker build -t fastapi-app .
docker run -d -p 8000:8000 --name fastapi-container fastapi-app
cd ..

# Verifikasi semua container berjalan
docker ps
```

### Akses Aplikasi

Setelah semua container berjalan, akses melalui browser:

1. **Flask**: `http://<EC2-Public-IP>:5000`
2. **Express**: `http://<EC2-Public-IP>:3000`
3. **FastAPI**: `http://<EC2-Public-IP>:8000`

## 📚 Panduan Belajar

### Langkah 1: Mulai dengan Flask
- Paling sederhana dan mudah dipahami
- Konsep dasar web framework
- Dockerfile sederhana

### Langkah 2: Lanjut ke Express
- Framework JavaScript yang populer
- Lebih banyak fitur dan endpoint
- Perbandingan dengan Flask

### Langkah 3: Eksplorasi FastAPI
- Framework modern dengan performa tinggi
- Dokumentasi API otomatis
- Fitur-fitur advanced

### Langkah 4: Perbandingan dan Analisis
- Bandingkan ketiga framework
- Pahami kelebihan dan kekurangan
- Pilih framework yang tepat untuk project

## 🔧 Perintah Docker Penting

```bash
# Management Container
docker ps                    # List running containers
docker ps -a                 # List all containers
docker stop <container>      # Stop container
docker start <container>     # Start container
docker restart <container>   # Restart container
docker rm <container>        # Remove container

# Management Image
docker images               # List images
docker build -t <name> .    # Build image
docker rmi <image>          # Remove image
docker pull <image>         # Download image

# Debugging
docker logs <container>     # View logs
docker exec -it <container> /bin/bash  # Enter container
docker inspect <container> # Container details
docker stats               # Resource usage

# Cleanup
docker system prune        # Clean unused resources
docker container prune     # Clean stopped containers
docker image prune         # Clean unused images
```

## 📝 Tugas dan Evaluasi

### Tugas Wajib:
1. ✅ Build dan jalankan ketiga aplikasi
2. 📸 Screenshot semua aplikasi yang berjalan
3. 📋 Buat daftar 20+ perintah Docker dengan penjelasan
4. 📊 Bandingkan ketiga framework
5. 📄 Buat laporan pembelajaran

### Kriteria Penilaian:
- **Teknis (40%)**: Aplikasi berhasil berjalan di Docker
- **Dokumentasi (30%)**: Screenshot dan laporan lengkap
- **Pemahaman (20%)**: Daftar perintah Docker dan penjelasan
- **Analisis (10%)**: Perbandingan framework dan kesimpulan

## 🎓 Tips untuk Pemula

### Do's ✅
- Baca README setiap aplikasi dengan teliti
- Coba semua endpoint yang tersedia
- Eksperimen dengan perintah Docker
- Buat catatan kendala dan solusinya
- Screenshot setiap langkah penting

### Don'ts ❌
- Jangan skip langkah instalasi Docker
- Jangan lupa konfigurasi Security Group
- Jangan hapus container sebelum screenshot
- Jangan copy-paste tanpa memahami
- Jangan lewatkan dokumentasi API FastAPI

## 🆘 Troubleshooting Umum

### Port sudah digunakan
```bash
sudo lsof -i :<port>
# Atau gunakan port lain
docker run -d -p <new-port>:<container-port> <image>
```

### Container tidak bisa diakses
- Cek Security Group EC2
- Pastikan container berjalan: `docker ps`
- Cek logs: `docker logs <container>`

### Build gagal
- Cek koneksi internet
- Pastikan file requirements/package.json ada
- Cek syntax Dockerfile

### Permission denied
```bash
sudo usermod -aG docker $USER
newgrp docker
```

## 📞 Support

Jika mengalami kesulitan:

1. **Cek dokumentasi** di README masing-masing aplikasi
2. **Lihat logs** container untuk error message
3. **Coba troubleshooting** yang disediakan
4. **Tanya instruktur** jika masih stuck

## 🚀 Menjalankan Multiple Containers

Setelah berhasil menjalankan aplikasi satu per satu, coba jalankan semua aplikasi sekaligus:

### Build Semua Images

```bash
# Build semua images sekaligus
cd flask-app && docker build -t flask-app . && cd ..
cd express-app && docker build -t express-app . && cd ..
cd fastapi-app && docker build -t fastapi-app . && cd ..
```

### Jalankan Semua Containers

```bash
# Jalankan semua container
docker run -d -p 5000:5000 --name flask-container flask-app
docker run -d -p 3000:3000 --name express-container express-app
docker run -d -p 8000:8000 --name fastapi-container fastapi-app

# Verifikasi semua berjalan
docker ps
```

### Management Commands

```bash
# Stop semua container
docker stop flask-container express-container fastapi-container

# Start semua container
docker start flask-container express-container fastapi-container

# Hapus semua container
docker rm flask-container express-container fastapi-container

# Lihat logs
docker logs flask-container
docker logs express-container
docker logs fastapi-container
```

## 🏆 Bonus Challenge

Setelah menyelesaikan tugas dasar, coba:

1. **Custom Network**: Hubungkan container dalam satu network
2. **Volume Mounting**: Implementasikan persistent storage
3. **Environment Variables**: Konfigurasi aplikasi dengan env vars
4. **Health Checks**: Tambahkan health check di Dockerfile
5. **Multi-stage Build**: Optimasi ukuran image
6. **Container Monitoring**: Monitor resource usage container
7. **Load Testing**: Test performa aplikasi dengan tools seperti Apache Bench

## 📈 Learning Path Selanjutnya

Setelah menguasai tutorial ini:

1. **Docker Networking** - Advanced container networking
2. **Docker Volumes** - Data persistence dan sharing
3. **Docker Swarm** - Container orchestration
4. **Kubernetes** - Advanced orchestration
5. **CI/CD** - Automated deployment
6. **Monitoring** - Container monitoring dan logging
7. **Security** - Container security best practices

---

**Selamat belajar Docker! 🐳**

*Dibuat dengan ❤️ untuk Aceng Academy*

*\"The best way to learn Docker is by doing!\"*