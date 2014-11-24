from flask import Flask, render_template, redirect, request
from data import add_url, get_url
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/todolist')
def runToDoList():
    return render_template('todolist/todolist.html')

@app.route('/shortener')
def run_short_sites():
    return render_template('shortener/shortener.html')

@app.route('/shortener/new_url', methods=['POST'])
def new_url():
    url = request.form['url']
    current_link = request.form['link']
    if current_link == "":
        link = add_url(url)
    else:
        link = add_url(url, current_link)
    return render_template('shortener/new.html', link=link)

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

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)