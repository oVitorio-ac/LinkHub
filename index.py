from flask import Flask, render_template, url_for
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do .env
load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    user_info = {
        'name': 'Vitório Augusto Cavalheiro',
        'profile_picture': 'https://avatars.githubusercontent.com/u/88901960?v=4',
        'instagram': os.getenv('INSTAGRAM_URL', 'https://www.instagram.com/default'),
        'email': os.getenv('EMAIL', 'mailto:default@example.com'),
        'whatsapp': os.getenv('WHATSAPP_URL', 'https://wa.me/00000000000'),
        'github': os.getenv('GITHUB_URL', 'https://github.com/default'),
        'linkedin': os.getenv('LINKEDIN_URL', 'https://www.linkedin.com/in/default'),
        'pix_key': os.getenv('PIX_KEY', 'sua-chave-pix-aqui')
    }
    return render_template('index.html', user_info=user_info)

if __name__ == '__main__':
    app.run(debug=True)
