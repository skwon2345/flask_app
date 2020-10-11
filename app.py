from flask import Flask, render_template

app = Flask(__name__)

all_posts = [
    {
        'title': 'Post 1',
        'content': 'This ifss the contenet of Post 1.',
        'author': 'Aaron'
    },
    {
        'title': 'Post 2',
        'content': 'This is the contenet of Post 2.'
    },
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts')
def posts():
    return render_template('posts.html', posts=all_posts)

@app.route('/home/<int:id>')
def hello(id):
    return "Hello, " + str(id)

@app.route('/onlyget', methods=['GET'])
def get_req():
    return 'You can only get this webpage.'

if __name__ == "__main__":
    app.run(debug=True)
