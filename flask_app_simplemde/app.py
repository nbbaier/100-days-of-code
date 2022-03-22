from flask import Flask, render_template
from flask_simplemde import SimpleMDE

app = Flask(__name__)
app.config['SIMPLEMDE_JS_IIFE'] = True
app.config['SIMPLEMDE_USE_CDN'] = True
SimpleMDE(app)

@app.route('/')
def hello():
    return render_template('hello.html')

if __name__ == '__main__':
    app.run(debug=True)
