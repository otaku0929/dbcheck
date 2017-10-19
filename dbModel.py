from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgres://rjrtqczwllnrdw:6f23d3af95bbdd7511cdd1849d3eb712dcc140a0cfe24d12a88643f7d2de0ead@ec2-54-83-205-71.compute-1.amazonaws.com:5432/dehi5aeo5k42th'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


class UserData(db.Model):
    __tablename__ = 'Images'

    id = db.Column(db.Integer, primary_key=True)
    Url = db.Column(db.String(256))
    CreateDate = db.Column(db.DateTime)


if __name__ == '__main__':
    manager.run()
