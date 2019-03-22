from flask import Flask
app = Flask(__name__)


@app.route('/calculated-BMI/<int:height>/<int:weight>')
def calculatedBMI(height, weight):
    BMI = (weight/((height*height)/10000))
    if BMI < 16:""
        return "Severly underweight"
    elif BMI < 18.5:
        return "Underweight"
    elif BMI < 25:
        return "Nomal"
    elif BMI <30:
        return "Overweight"
    else:
        return "Obese"

if __name__ == '__main__':
  app.run(debug=True)
 