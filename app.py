from flask import Flask
from sharedstate import db, loaded_modules
import json


# Scan modules and load them and do other stuffs


app = Flask(__name__)

with open("econf.json", "r") as ecf:
    site_config = json.load(ecf)
db_uri = "{db}://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}".format(
        db=site_config["db"]["db"],
        db_user=site_config["db"]["db_user"],
        db_pass=site_config["db"]["db_pass"],
        db_host=site_config["db"]["db_host"],
        db_port=site_config["db"]["db_port"],
        db_name=site_config["db"]["db_name"],
    )
app.config['DEBUG'] = site_config["server"]["flask_debug"]
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.sqlite"  # db_uri
with app.app_context():
    db.init_app(app)
    db.create_all()

if __name__ == '__main__':
    app.run()
