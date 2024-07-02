from flask import Flask, request, render_template, url_for
import random

app = Flask(__name__, template_folder='templates', static_folder='static')
random_number = random.randint(1, 10)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    user_guess = int(request.form['guess'])
    global random_number

    if user_guess == random_number:
        message = "Congratulations! You guessed the right number."
        random_number = random.randint(1, 10)  # Reset the random number after a correct guess
    else:
        message = f"Sorry, the correct number was {random_number}. Try again!"
        random_number = random.randint(1, 10)  # Reset the random number after an incorrect guess

    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
