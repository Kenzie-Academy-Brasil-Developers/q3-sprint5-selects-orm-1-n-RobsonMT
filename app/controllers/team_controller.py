from http import HTTPStatus
from flask import jsonify, request
from sqlalchemy.orm.session import Session
from app.configs.database import db
from app.models.team_model import TeamModel
from flask_sqlalchemy import BaseQuery, Pagination


def get_by_query():
    session: Session = db.session
    base_query: BaseQuery = session.query(TeamModel)

    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 1, type=int)

    teams: Pagination = base_query.order_by(TeamModel.id).paginate(
        page=page, per_page=per_page
    )

    return jsonify(teams.items), HTTPStatus.OK


def get_by_limit(limit):
    session: Session = db.session

    teams = session.query(TeamModel).limit(limit=limit).all()

    return jsonify(teams), HTTPStatus.OK


def get_by_name(name: str):
    session: Session = db.session

    search = "%{}%".format(name)

    teams = session.query(TeamModel).filter(TeamModel.team_name.ilike(search)).all()

    return jsonify(teams), HTTPStatus.OK
