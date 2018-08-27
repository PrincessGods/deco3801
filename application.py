from flask import Flask, render_template, url_for
application = app = Flask(__name__)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Aug 25, 2018'
    },

    {
        'author': 'Jason Lin',
        'title': 'Blog Post 2',
        'content': 'wtf',
        'date_posted': 'Aug 25, 2018'
    }
]

@app.route("/")

@app.route("/home")
def home():
    return render_template('index.html', posts = posts, title = "demo1")

@app.route("/about")
def about():
    return "About World!"

if __name__ == '__main__':
    app.run(debug=True)