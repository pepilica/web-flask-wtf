from flask import Flask, render_template


app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def colon(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('train.html', name=prof)


@app.route('/list_prof/<param>')
def list_prof(param):
    return render_template('jobs.html', name=param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')