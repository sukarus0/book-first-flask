from flask import Flask, request

app = Flask(__name__)

@app.route('/index')
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/users/<username>')
def get_user(username):
    return username

@app.route('/posts/<int:post_id>')
def get_post(post_id):
    return str(post_id)

@app.route('/uuid/<uuid:uuid>')
def get_uuid(uuid):
    return str(uuid)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
