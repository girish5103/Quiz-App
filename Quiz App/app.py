from flask import Flask, render_template, jsonify

app = Flask(__name__)

questions = [
    {
        'question': 'Which famous palace is located in Mysore?',
        'answers': [
            {'text': 'Hawa Mahal', 'correct': False},
            {'text': 'Amber Palace', 'correct': False},
            {'text': 'Mysore Palace', 'correct': True},
            {'text': 'City Palace', 'correct': False}
        ]
    },
    {
        'question': 'What is the name of the traditional sweet dish from Mysore?',
        'answers': [
            {'text': 'Gulab Jamun', 'correct': False},
            {'text': 'Mysore Pak', 'correct': True},
            {'text': 'Jalebi', 'correct': False},
            {'text': 'Rasgulla', 'correct': False}
        ]
    },
    {
        'question': 'Which famous festival of Karnataka is celebrated grandly in Mysore?',
        'answers': [
            {'text': 'Hampi Festival', 'correct': False},
            {'text': 'Ugadi', 'correct': False},
            {'text': 'Makar Sankranti', 'correct': False},
            {'text': 'Dasara', 'correct': True}
        ]
    },
    {
        'question': 'What is the name of the hill located near Mysore which offers a panoramic view of the city?',
        'answers': [
            {'text': 'Nandi Hills', 'correct': False},
            {'text': 'Chamundi Hills', 'correct': True},
            {'text': 'Talakadu Hills', 'correct': False},
            {'text': 'Bilikal Rangaswamy Betta', 'correct': False}
        ]
    },
    {
        'question': 'Which famous university is located in Mysore?',
        'answers': [
            {'text': 'Jawaharlal Nehru University', 'correct': False},
            {'text': 'Banaras Hindu University', 'correct': False},
            {'text': 'University of Mysore', 'correct': True},
            {'text': 'Aligarh Muslim University', 'correct': False}
        ]
    },
    # Add more questions as needed
]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/questions', methods=['GET'])
def get_questions():
    return jsonify(questions)

if __name__ == '__main__':
    app.run(debug=True)
