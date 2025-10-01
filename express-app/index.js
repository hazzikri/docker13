const express = require('express');
const path = require('path');

const app = express();
const PORT = 3000;

// Middleware untuk serve static files
app.use(express.static('public'));

// Route untuk halaman utama
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Route API sederhana
app.get('/api/hello', (req, res) => {
    res.json({
        message: 'Hello from Express API!',
        status: 'success',
        timestamp: new Date().toISOString()
    });
});

// Route untuk health check
app.get('/health', (req, res) => {
    res.json({ status: 'OK', service: 'Express App' });
});

app.listen(PORT, '0.0.0.0', () => {
    console.log(`🚀 Express server running on http://0.0.0.0:${PORT}`);
});