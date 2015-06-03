import datetime
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
    shown_links = type(list()) == type(session.get('shortener_user_urls'))
    list_urls_by_login = None
    counter = 0
    if session.get('shortener_user_urls'):
        list_urls_by_login = []
        for current_url in session.get('shortener_user_urls'):
            counter += 1
            current_data = dict()
            current_data['url'] = current_url.get('url')
            current_data['link'] = current_url.get('link')
            current_data['number'] = counter
            list_urls_by_login.append(current_data)
    return render_template('shortener/shortener.html', link=current_link,
                           shown_links=shown_links, list_urls=list_urls_by_login)


@app.route('/shortener/new_url', methods=['POST'])
def new_url():
    url = request.form['url']
    current_link = request.form['link']
    login = session.get('login')
    if current_link == "":
        link = add_url(url, None, login)
    else:
        link = add_url(url, current_link, login)

    flash(link)
    if session.get('login'):
        session['shortener_user_urls'].append({'url': url, 'link': link, 'login': login})
    return redirect('/shortener', code=302)


@app.route('/shortener/show_urls_by_login')
def show_urls_by_login():
    if session.get('login') is None:
        return '403'
    urls = get_list_links(session.get('login'))
    session['shortener_user_urls'] = urls
    return redirect('/shortener', code=302)


@app.route('/shortener/hide_urls_by_login')
def hide_urls_by_login():
    if session.get('login') is None:
        return '403'
    session.pop('shortener_user_urls', None)
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
        print(link)
        if url.find('http://') != -1:
            return redirect(get_url(link), code=302)
        elif url.find('https://') != -1:
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
            session.permanent_session_lifetime = datetime.timedelta(minutes=15)
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
    session.pop('shortener_user_urls', None)
    return redirect('/')


if __name__ == '__main__':
    sent_link = None
    app.debug = True
    app.secret_key = os.urandom(24)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)