from flask import render_template, request

from app import app, db
from app.models import Feedback
from app.send_mail import send_email

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        game = request.form['game']
        rating = request.form['rating']
        comments = request.form['comments']
        # print(customer, game, rating, comments)
        if customer == '' or game == '':
            return render_template('index.html', message='Please, enter all fields')

        # if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
        if Feedback.query.filter_by(customer=customer).count()==0:
            data = Feedback(customer,game,rating,comments)
            db.session.add(data)
            db.session.commit()
            send_email(customer,game,rating,comments)

            return render_template('success.html')

        return render_template('index.html', message='You have already submitted feedback')