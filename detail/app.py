from flask import Flask, render_template, request, redirect
import redis

app = Flask(__name__)

r = redis.StrictRedis(host='localhost', port=6379, db=0)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/userdetail', methods=['GET', 'POST'])
def user_detail():
    if request.method == 'GET':
        return render_template('add_user.html')
    elif request.method == 'POST':
        name = request.form['name']
        year = request.form['year']
        city = request.form['city']
        problem = request.form['problem']

        r.set(name+':name', name)
        r.set(name+':year', year)
        r.set(name+':city', city)
        r.set(name+':problem', problem)

        if request.form['name'] and request.form['year'] and request.form['city'] and request.form['problem']:
            message = 'User added successfully.'
            return render_template('home.html', message=message)
        else:
            return render_template('add_user.html', message='All field are required!!!')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        return render_template('search.html')
    elif request.method == 'POST':
        name = request.form['search']
        if name:
            name1 = r.get(name+':name')
            year1 = r.get(name + ':year')
            city1 = r.get(name + ':city')
            problem1 = r.get(name + ':problem')
            return render_template('user_detail.html', name=name1, year=year1, city=city1, problem=problem1)
        else:
            return render_template('search.html', message='Field are required!!!')




@app.route('/error')
def error():
    return render_template('no_user.html')

if __name__ == '__main__':
    app.run(debug=True)
