from flask import Flask, render_template, request, redirect, url_for, flash,session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
import random
from .models import Contact 


from models import db, Question, Option, Answer
from config import Config
app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/quiz')
def quiz():
    questions = Question.query.all()
    selected_questions = random.sample(questions, 15)
    session['selected_questions'] = [q.id for q in selected_questions]
    return render_template('quiz.html', questions=selected_questions)




@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    correct_answers = []  
    attempted_questions = set()  
    
    # Get the seected question IDs from the session
    selected_question_ids = session.get('selected_questions', [])
    
    for question_id, option_id in request.form.items():
        if question_id.isnumeric() and option_id.isnumeric():
            question_id = int(question_id)
            option_id = int(option_id)
            
            
            if question_id not in selected_question_ids:
                continue  

            correct_answer = Answer.query.filter_by(question_id=question_id).first()
            
            if correct_answer:
               
                question = Question.query.get(question_id)
                selected_option = Option.query.get(option_id)
                correct_option = Option.query.get(correct_answer.option_id)
                
               
                if correct_answer.option_id == option_id:
                    score += 1
                    correct_answers.append((question.question_text, selected_option.option_text, "Correct", correct_option.option_text))
                else:
                    correct_answers.append((question.question_text, selected_option.option_text, "Incorrect", correct_option.option_text))
                
                attempted_questions.add(question_id)  
            else:
                print(f"No correct answer found for Question ID: {question_id}")
    
   
    for question_id in selected_question_ids:
        if question_id not in attempted_questions:
            question = Question.query.get(question_id)
            correct_answer = Answer.query.filter_by(question_id=question_id).first()
            if correct_answer:
                correct_option = Option.query.get(correct_answer.option_id)
                correct_answers.append((question.question_text, "Unattempted", "Unattempted", correct_option.option_text))

    return render_template('result.html', score=score, correct_answers=correct_answers)




@app.route('/aboutUs')
def about_us():
    return render_template('aboutUs.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact_us():
    if request.method == 'POST':
        
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        
        new_contact = Contact(name=name, email=email, phone=phone, message=message)
        db.session.add(new_contact)
        db.session.commit()

        return render_template('contact_us.html', success=True)

    return render_template('contact_us.html', success=False)




if __name__ == '__main__':
    app.run(debug=True)
