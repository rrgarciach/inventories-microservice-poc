import os

from flask_sqlalchemy import SQLAlchemy

POSTGRES = {
'user': os.environ['POSTGRES_USER'],
'pw': os.environ['POSTGRES_PASSWORD'],
'db': os.environ['POSTGRES_DB'],
'host': os.environ['POSTGRES_HOST'],
'port': '5432',
}

def create_connection(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
    %(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    return db
