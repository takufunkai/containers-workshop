from flask import Flask, render_template, url_for
import random

app = Flask(__name__)

quotes = [
    "Logic will get you from A to B. Imagination will take you everywhere.",
    "There are 10 kinds of people. Those who know binary and those who don't",
    '''
    There are two ways of constructing a software design. One way is to make it
    so simple that there are obviously no deficiencies and the other is to make it
    so complicated that there are no obvious deficiencies.
    ''',
    "It's not that I'm so smart, it's just that I stay with problems longer.",
    "It is pitch dark. You are likely to be eat by a grue."
]

@app.route("/test")
def hello_world():
    quote_index = random.randint(0, len(quotes) - 1)
    image_url = url_for('static', filename='smile.jpg')
    gh_url = "https://github.com/takufunkai/containers-workshop"
    return render_template(
        'index.html', 
        quote=quotes[quote_index], 
        image_url=image_url,
        gh_url=gh_url)

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
