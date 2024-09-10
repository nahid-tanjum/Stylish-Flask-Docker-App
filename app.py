from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <head>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f9;
                    text-align: center;
                    padding: 50px;
                }
                h1 {
                    color: #333;
                    font-size: 48px;
                }
                p {
                    color: #666;
                    font-size: 20px;
                }
                .container {
                    margin: 0 auto;
                    padding: 20px;
                    max-width: 600px;
                    background-color: #fff;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    border-radius: 8px;
                }
                a {
                    color: #3498db;
                    text-decoration: none;
                }
                a:hover {
                    text-decoration: underline;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Hello from Docker!</h1>
                <p>Welcome to my beautifully styled Dockerized Flask web app.</p>
                <p>This app was created for <strong>Task 4.3 Distinction</strong>.</p>
                <a href="https://docker.com">Learn more about Docker</a>
            </div>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
