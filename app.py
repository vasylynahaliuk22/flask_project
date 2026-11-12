from flask import Flask, render_template, request

app = Flask(__name__)
users = [] 

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/news')
def news():
    news_list = [
        {"title": "Запуск нашого Flask-сайту", "date": "12.11.2026", "text": "Ми успішно розробили багатосторінковий веб-додаток!"},
        {"title": "Оновлення дизайну", "date": "12.11.2026", "text": "Додано сучасну темну кольорову схему та зручну навігацію."}
    ]
    return render_template('news.html', news_list=news_list)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        users.append({'name': name, 'email': email, 'message': message})
        return render_template('result.html', name=name, email=email, message=message)
    return render_template('register.html')

@app.route('/users')
def show_users():
    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)