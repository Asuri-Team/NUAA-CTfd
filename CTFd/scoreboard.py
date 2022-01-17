from flask import Blueprint, render_template

from CTFd.utils import config
from CTFd.utils.config.visibility import scores_visible
from CTFd.utils.decorators.visibility import check_score_visibility
from CTFd.utils.helpers import get_infos
from CTFd.utils.scores import get_standings
from CTFd.utils.user import is_admin
from CTFd.cache import clear_config, clear_standings
scoreboard = Blueprint("scoreboard", __name__)


@scoreboard.route("/scoreboard")
@check_score_visibility
def listing():
    infos = get_infos()

    if config.is_scoreboard_frozen():
        infos.append("Scoreboard has been frozen")

    if is_admin() is True and scores_visible() is False:
        infos.append("Scores are not currently visible to users")
    clear_standings()
    standings = get_standings()
    return render_template("scoreboard.html", standings=standings, infos=infos)

@scoreboard.route("/scoreboard/1")
@check_score_visibility
def listing1():
    infos = get_infos()
    
    if config.is_scoreboard_frozen():
        infos.append("Scoreboard has been frozen")

    if is_admin() is True and scores_visible() is False:
        infos.append("Scores are not currently visible to users")
    clear_standings()
    standings = get_standings(None, False, request=1)
    return render_template(
        "scoreboard.html",
        standings=standings,
        infos=infos
    )


@scoreboard.route("/scoreboard/2")
@check_score_visibility
def listing2():
    infos = get_infos()
    if config.is_scoreboard_frozen():
        infos.append("Scoreboard has been frozen")
    if is_admin() is True and scores_visible() is False:
        infos.append("Scores are not currently visible to users")
    clear_standings()
    standings = get_standings(None, False, request=2)
    return render_template(
        "scoreboard.html",
        standings=standings,
        infos=infos
    )


