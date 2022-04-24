from flask import Blueprint
from app.routes.athlete_route import bp_athlete
from app.routes.team_route import bp_team

bp_api = Blueprint("bp_api", __name__, url_prefix="/api")

bp_api.register_blueprint(bp_athlete)
bp_api.register_blueprint(bp_team)
