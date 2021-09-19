from app import app
from model.model import Model
from flask import render_template, request
# from forms.form import Parameters_Form


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/prediction', methods=['post'])
def prediction():
    model = Model()
    age, gender = request.form.values()

    if gender == 'Male':
        sex_female, sex_male = 0, 1
    elif gender == 'Female':
        sex_female, sex_male = 1, 0
    else:
        return None

    pred = model.predict(age, sex_female, sex_male)
    if pred == 1:
        result = 'SURVIVE :)'
    elif pred == 0:
        result = 'DIE :('

    predict_message = 'According to your parameters you would ' + result

    return render_template('index.html', predict_message=predict_message)
