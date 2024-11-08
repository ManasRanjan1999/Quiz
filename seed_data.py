import json
from app import db, Question, Option, Answer, app  
with open('data.json', 'r') as file:
    questions_data = json.load(file)

def seed_data():
    with app.app_context():
        for question_data in questions_data:
            question_text = question_data['question']
            question = Question(question_text=question_text)
  
            db.session.add(question)
            db.session.commit()  
            
           
            options = question_data['options']
            correct_option_text = question_data['correct_option']
            correct_option = None

            for key, option_text in options.items():
               
                option = Option(question_id=question.id, option_text=option_text)
                db.session.add(option)
                
               
                if option_text == correct_option_text:
                    correct_option = option

            db.session.commit()  

            if correct_option:
                answer = Answer(question_id=question.id, option_id=correct_option.id)
                db.session.add(answer)

        db.session.commit()

if __name__ == '__main__':
    seed_data()
    print("Data seeded successfully!")
