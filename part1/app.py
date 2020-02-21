import flask
Server = flask.Flask(__name__)

@Server.route('/')
def home():
    return flask.render_template('home.html')

@Server.route('/register')
def registrationForm():
    return flask.render_template('registerForm.html')

@Server.route('/registerinput', methods=['POST'])
def register():
    try:
        return flask.render_template('showUser.html', UserLib=flask.request.form)
    except:
        return flask.render_template('failure.html')

if __name__ == "__main__":
    Server.run(debug=True)