from flask import Flask, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return redirect('https://dontclickthelink.earthrulerr.repl.co')


app.run(host='0.0.0.0', port=81)
