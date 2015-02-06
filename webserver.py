from flask import Flask, render_template, redirect, request, flash, get_flashed_messages, session, url_for
from data import add_url, get_url, get_list_links
import os
from sign import validate_user, is_registered, add_user

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/todolist')
def runToDoList():
    return render_template('todolist/todolist.html')



@app.route('/shortener')
def run_short_sites():
    messages = get_flashed_messages()
    current_link = None
    if messages:
        for message in messages:
            current_link = message
    return render_template('shortener/shortener.html', link=current_link)

@app.route('/shortener/new_url', methods=['POST'])
def new_url():
    url = request.form['url']
    current_link = request.form['link']
    if current_link == "":
        link = add_url(url)
    else:
        link = add_url(url, current_link)

    flash(link)

    return redirect('/shortener', code=302)

@app.route('/shortener/redirect', methods=['POST'])
def shorten_redirect():
    link = request.form['link']
    return redirect('/send/' + link)

@app.route('/send/<link>')
def redirect_url(link):
    if get_url(link) is None:
        return '404'
    else:
        url = get_url(link)
        if link.find('http://') != -1:
            return redirect(get_url(link), code=302)
        else:
            return redirect('http://' + url, code=302)


@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        if validate_user(login, password):
            session['login'] = request.form['login']
            return redirect('/', code=302)
        else:
            flash("Wrong login or password", 'error')
            return render_template('sign_in.html')
    else:
        return render_template('sign_in.html')


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        counter = 0
        if is_registered(login):
            flash('Username is busy', 'login_errors')
            counter += 1
        if len(login) == 0:
            flash('Username is empty', 'login_errors')
            counter += 1
        if len(password) < 6:
            flash('Password should be greater than 6 symbols', 'password_errors')
            counter += 1
        if counter > 0:
            return render_template('sign_up.html')
        else:
            add_user(login, password)
            flash('You have successfully registered', 'info')
            return redirect(url_for('sign_in'), code=302)
    else:
        return render_template('sign_up.html')


@app.route('/sign_out', methods=['POST'])
def sign_out():
    if 'login' not in session:
        return redirect(url_for('sign_in'))

    session.pop('login', None)
    return redirect('/')


if __name__ == '__main__':
    sent_link = None
    app.debug = True
    app.secret_key = 'DSJIOPJ OIROJRO  O* UH#u8ch'
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)