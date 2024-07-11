#!/usr/bin/python3
"""
Flask web application script:
- Hosts on 0.0.0.0 at port 5000
- Routes:
  /: Displays 'Hello HBNB!'
  /hbnb: Displays 'HBNB'
  /c/<text>: Displays 'C ' followed by the value of the text variable,
             replaces underscores with spaces.
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Display 'Hello HBNB!' at the root URL """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Display 'HBNB' at the URL /hbnb """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Display 'C ' followed by the text provided in the URL,
    replacing underscores with spaces.
    """
    return 'C ' + text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
