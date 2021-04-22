from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = ''
posts = [
    {
        'author': 'Antontioo',
        'title': 'Blogg 1',
        'content': 'AAAAAAAAAAAAAAAAAAAAAAAaaaaaAAAsAAAAAAAAAAAAAAAAA',
        'date_posted': 'April 15, 2021'
    },
    {
        'author': 'evil anton',
        'title': 'Blogg 2',
        'content': 'BBBBBBBBBBBBBBBBBBBBBBB',
        'date_posted': 'April 16, 2021'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Konto har skapats för {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('Du är nu inloggad!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Inloggning misslyckades. Kontrollera användarnamn och lösenord', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(host='localhost', port=9874, debug=True)


