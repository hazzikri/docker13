# Menggunakan Node.js 18 sebagai base image
FROM node:18-alpine

# Set working directory di dalam container
WORKDIR /app

# Copy package.json dan package-lock.json (jika ada)
COPY package*.json ./

# Install dependencies
RUN npm install --only=production

# Copy semua file aplikasi ke dalam container
COPY . .

# Expose port 3000
EXPOSE 3000

# Command untuk menjalankan aplikasi
CMD ["npm", "start"]