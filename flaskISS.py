
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
import iss_locale

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def dynamic_page():
    return iss_locale.findISS()

if __name__ == '__main__':
    app.run(debug=True)
