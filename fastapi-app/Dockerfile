# Menggunakan Python 3.9 sebagai base image
FROM python:3.9-slim

# Set working directory di dalam container
WORKDIR /app

# Copy requirements.txt terlebih dahulu untuk memanfaatkan Docker cache
COPY requirements.txt .

# Install dependencies Python
RUN pip install --no-cache-dir -r requirements.txt

# Copy semua file aplikasi ke dalam container
COPY . .

# Expose port 8000
EXPOSE 8000

# Command untuk menjalankan aplikasi dengan uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]