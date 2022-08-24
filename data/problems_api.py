import flask
from flask import render_template, redirect
from data import db_session
from data.problems import Problems
from data.problems_form import ProblemsForm
from data.answer_form import AnswerForm
from flask_login import current_user
from flask_login import LoginManager, login_user, logout_user, login_required

blueprint = flask.Blueprint(
    'problems_api',
    __name__,
    template_folder='templates'
)

@blueprint.route('/add_problem', methods=['GET', 'POST'])
@login_required
def add_problem():
    form = ProblemsForm()
    if current_user.role > 0:
        if form.validate_on_submit():
            db_sess = db_session.create_session()
            problem = Problems()
            problem.text = form.text.data
            problem.level = int(form.level.data)
            problem.difficulty = int(form.difficulty.data)
            problem.answer = form.answer.data
            problem.comment = form.comment.data
            problem.owner = current_user.id
            db_sess.add(problem)
            db_sess.commit()
            return redirect('/')
        return render_template('problems_form.html', title='Add problem',
                               form=form)
    return redirect('/')

@blueprint.route('/show_problems', methods=['GET', 'POST'])
@login_required
def show_problems():
    db_sess = db_session.create_session()
    problems = db_sess.query(Problems).all()
    return render_template('show_problems.html', title='Show problems',
                           problems=problems, num=len(problems))

@blueprint.route('/<int:problem_id>', methods=['GET', 'POST'])
@login_required
def problem_answer(problem_id):
    form = AnswerForm()
    db_sess = db_session.create_session()
    problem = db_sess.query(Problems).filter(Problems.id == problem_id).first()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('answer_form.html', title='Answer',
                           problem=problem, form = form)
