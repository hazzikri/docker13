from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/hello')
def hello_api():
    return {'message': 'Hello from Flask API!', 'status': 'success'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)