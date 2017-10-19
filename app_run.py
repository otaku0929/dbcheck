from flask import *
from datetime import datetime
from dbModel import *

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    data = "Deploying a Flask App To Heroku"
    data_UserData = Images.query.all()
    history_dic = {}
    history_list = []
    for _data in data_UserData:
        history_dic['ID'] = _data.id
        history_dic['Url'] = _data.Url
        history_dic['CreateDate'] = _data.CreateDate.strftime('%Y/%m/%d %H:%M:%S')
        history_list.append(history_dic)
        history_dic = {}
    return render_template('index.html', **locals())


@app.route('/API/add_data', methods=['POST'])
def add_data():
    name = request.form['id']
    description = request.form['Url']
    if id != "" and description != "":
        add_data = Images(
            id=id,
            Url=Url,
            CreateDate=datetime.now()
        )
        db.session.add(add_data)
        db.session.commit()
    return redirect('index')


if __name__ == '__main__':
    app.run(debug=True)
