from flask import Flask, request, render_template
import redis

app = Flask(__name__)

# connect to server
r = redis.StrictRedis(host='localhost', port=6379, db=0)


@app.route("/")
def index():
    return render_template('index.html')

# @app.route('/submission')
#def submission():
#    return render_template('submission.html')
# server create

@app.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('createQuestion.html')
    elif request.method == 'POST':
        title = request.form['title']
        question = request.form['question']
        answer = request.form['answer']

        r.set(title+':question', question)
        r.set(title+':answer', answer)

        return render_template('submission.html')
    else:
        return '<h2>Invalid request</h'


if __name__=='__main__':
    app.run()
