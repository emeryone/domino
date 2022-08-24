import flask
from flask import render_template, redirect
from data import db_session
from data.tournament import Tournament, problems_to_tournament
from data.problems import Problems
from data.tournament_form import TournamentForm
from data.add_problem_form import AddProblemForm
from flask_login import current_user
from flask_login import LoginManager, login_user, logout_user, login_required

blueprint = flask.Blueprint(
    'tournament_api',
    __name__,
    template_folder='templates'
)

@blueprint.route('/add_tournament', methods=['GET', 'POST'])
@login_required
def add_tournament():
    form = TournamentForm()
    if current_user.role > 0:
        db_sess = db_session.create_session()
        if form.validate_on_submit():
            tournament = Tournament()
            tournament.title = form.title.data
            tournament.level = form.level.data
            tournament.owner = current_user.id
            db_sess.add(tournament)
            db_sess.commit()
            line = '/show_problems/' + str(tournament.id) 
            return redirect(line)
        return render_template('tournament_form.html', title='Add tournament', form=form)
    return redirect('/')

@blueprint.route('/show_problems/<int:tourId>', methods=['GET', 'POST'])
@login_required
def show_problems(tourId):
    if current_user.role > 0:
        db_sess = db_session.create_session()
        #id_list = ('''SELECT problems FROM problems_to_tournament WHERE tournament = ?''', (tourId,))
        #problems = db_sess.query(Problems).filter(Problems.id.notin_(id_list))
        problems = db_sess.query(Problems).all()
        return render_template('show_problems.html', title='Add problems',
                               problems=problems, num=len(problems), tourId=tourId)
    return redirect('/')


@blueprint.route('/add/<int:tournament_id>/<int:problem_id>', methods=['GET', 'POST'])
@login_required
def add(tournament_id, problem_id):
    form = AddProblemForm()
    if form.validate_on_submit():
        statement = problems_to_tournament.insert().values(tournament=tournament_id, problems=problem_id, 
                                                           number=form.number.data)
        db_sess = db_session.create_session()
        db_sess.execute(statement)
        db_sess.commit()
        line = '/show_problems/' + str(tournament_id)
        return redirect(line)
    return render_template('add_problem_form.html', title='Add problem', form=form)