from flask import Flask
from .plant_suggest_endpoint import plant_suggestions_blueprint  # import the blueprint
from .app import my_plant_friend  # import the blueprint

app = Flask(__name__)
app.register_blueprint(plant_suggestions_blueprint)  # register the blueprint
app.register_blueprint(my_plant_friend)  # register the blueprint
app.config['DEBUG'] = True

if __name__ == '__main__':
    app.run()

