from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Talha Ejaz',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 25, 2023'
    },
    {
        'author': 'Muhammad Ejaz',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 25, 2023'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
