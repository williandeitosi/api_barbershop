from flask import Flask
from models.model import initialize_database
from controllers.schedule_controller import hour_bp


app = Flask(__name__)
app.register_blueprint(hour_bp)

initialize_database()
app.run(debug=True)
