from flask import Blueprint
from app.controllers import team_controller


bp_team = Blueprint("bp_team", __name__, url_prefix="/teams")


# Suas rotas aqui
bp_team.get("")(team_controller.get_by_query)
bp_team.get("/by_limit/<int:limit>")(team_controller.get_by_limit)
bp_team.get("/by_name/<name>")(team_controller.get_by_name)
