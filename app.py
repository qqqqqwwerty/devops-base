import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import datetime

PORT = int(os.environ.get('APP_PORT', 5000))
LOG_FILE = os.environ.get('LOG_PATH', '/var/log/app/access.log')
ENV = os.environ.get('APP_ENV', 'development')

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{ENV}] {timestamp} - GET {self.path}\n"
        
        try:
            with open(LOG_FILE, 'a') as f:
                f.write(log_entry)
        except Exception as e:
            print(f"Log error: {e}")

        html_content = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Junior DevOps Engineer | Кемерово</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
            color: #e0e0e0;
        }
        .container {
            background: #1f1f3a;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
            max-width: 900px;
            width: 100%;
            overflow: hidden;
            border: 1px solid #333;
        }
        .header {
            background: linear-gradient(135deg, #0f3460 0%, #1a1a2e 100%);
            color: #e0e0e0;
            padding: 40px;
            text-align: center;
            border-bottom: 2px solid #333;
        }
        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
            font-weight: 700;
            color: #4cc9f0;
        }
        .header p {
            font-size: 1.2em;
            opacity: 0.9;
            color: #a0a0a0;
        }
        .content { padding: 40px; }
        .section { margin-bottom: 30px; }
        .section h2 {
            color: #4cc9f0;
            font-size: 1.8em;
            margin-bottom: 15px;
            border-bottom: 2px solid #4cc9f0;
            padding-bottom: 10px;
        }
        .section p {
            color: #b0b0b0;
            line-height: 1.6;
            font-size: 1.1em;
        }
        .skills {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 15px;
        }
        .skill {
            background: linear-gradient(135deg, #4cc9f0 0%, #4361ee 100%);
            color: #1a1a2e;
            padding: 8px 20px;
            border-radius: 25px;
            font-size: 0.9em;
            font-weight: 500;
        }
        .contact {
            background: #16213e;
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
            border: 1px solid #333;
        }
        .contact p { margin: 10px 0; color: #b0b0b0; }
        .contact strong { color: #4cc9f0; }
        .footer {
            background: #16213e;
            text-align: center;
            padding: 20px;
            color: #888;
            font-size: 0.9em;
            border-top: 1px solid #333;
        }
        .status {
            display: inline-block;
            background: #4cc9f0;
            color: #1a1a2e;
            padding: 5px 15px;
            border-radius: 15px;
            font-size: 0.8em;
            margin-top: 10px;
            font-weight: 600;
        }
        a {
            color: #4cc9f0;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Привет! Я Junior DevOps</h1>
            <p>18 лет | Кемерово, Россия</p>
            <span class="status">В поиске вакансии Junior DevOps Engineer</span>
        </div>
        <div class="content">
            <div class="section">
                <h2>Обо мне</h2>
                <p>
                    Я начинающий DevOps-инженер из Кемерова. Мне 18 лет, и я увлечен автоматизацией, 
                    контейнеризацией и современными методами разработки ПО. Стремлюсь развиваться в 
                    области облачных технологий и CI/CD пайплайнов.
                </p>
            </div>
            <div class="section">
                <h2>Мои навыки</h2>
                <div class="skills">
                    <span class="skill">Docker</span>
                    <span class="skill">Docker Compose</span>
                    <span class="skill">Linux</span>
                    <span class="skill">Git</span>
                    <span class="skill">Nginx</span>
                    <span class="skill">Python</span>
                    <span class="skill">Bash</span>
                    <span class="skill">PostgreSQL</span>
                    <span class="skill">CI/CD</span>
                    <span class="skill">Мониторинг</span>
                </div>
            </div>
            <div class="section">
                <h2>Что я изучаю</h2>
                <p>
                    В настоящее время углубляюсь в Kubernetes, Terraform, Ansible и облачные платформы. 
                    Интересуюсь DevOps практиками и методологией DevSecOps.
                </p>
            </div>
            <div class="section">
                <h2>Контакты</h2>
                <div class="contact">
                    <p><strong>Локация:</strong> Кемерово, Россия</p>
                    <p><strong>Возраст:</strong> 18 лет</p>
                    <p><strong>Telegram:</strong> <a href="https://t.me/jowexsa">@jowexsa</a></p>
                    <p><strong>Телефон:</strong> +7 923 600 61 46</p>
                    <p><strong>Статус:</strong> В поиске вакансии Junior DevOps Engineer</p>
                    <p><strong>Стек:</strong> Docker, Linux, CI/CD, Monitoring</p>
                </div>
            </div>
        </div>
        <div class="footer">
            <p>© 2026 | Junior DevOps Portfolio | Environment: """ + ENV + """</p>
        </div>
    </div>
</body>
</html>"""

        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(html_content.encode('utf-8'))

if __name__ == '__main__':
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    print(f"Starting server on port {PORT}...")
    server = HTTPServer(('0.0.0.0', PORT), Handler)
    server.serve_forever()