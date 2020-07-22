from flask import Flask, render_template, request, Response, jsonify, send_from_directory

app = Flask(__name__, static_folder='static')

# define routing
@app.route('/')
@app.route('/home')
def main():
    return render_template("home.html")

'''@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')'''

if __name__=='__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)