from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>ربات مانیتور تلگرام</title>
        <meta charset="utf-8">
        <style>
            body { 
                font-family: Tahoma, Arial, sans-serif;
                direction: rtl;
                text-align: center;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 50px;
            }
            .container {
                background: rgba(255,255,255,0.1);
                padding: 30px;
                border-radius: 15px;
                backdrop-filter: blur(10px);
                max-width: 600px;
                margin: 0 auto;
            }
            h1 { font-size: 2.5em; margin-bottom: 20px; }
            .status { 
                background: #28a745; 
                padding: 10px 20px; 
                border-radius: 25px;
                font-size: 1.2em;
                display: inline-block;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🤖 ربات مانیتور تلگرام</h1>
            <div class="status">✅ فعال و آنلاین</div>
            <p>ربات در حال اجرا روی Railway</p>
            <p>آماده دریافت دستورات تلگرام</p>
        </div>
    </body>
    </html>
    """

@app.route('/health')
def health():
    return "✅ ربات سالم است"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
