from flask import Flask
from plant_suggest_endpoint import plant_suggestions
from app import my_plant_friend_blueprint  # import the blueprint
from user_main import user_blueprint

app = Flask(__name__)
app.register_blueprint(plant_suggestions)  # register the blueprint
app.register_blueprint(my_plant_friend_blueprint)  # register the blueprint
app.register_blueprint(user_blueprint)  # register the blueprint


app.config['DEBUG'] = True

if __name__ == '__main__':
    app.run()
