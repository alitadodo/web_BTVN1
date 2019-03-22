from flask import Flask, render_template
app = Flask(__name__)


@app.route('/calculated-BMI/<int:height>/<int:weight>')
def calculatedBMI(height, weight):
    BMI = (weight/((height*height)/10000))


    return render_template('serious_ex1.html',
                                        BMI=BMI)

if __name__ == '__main__':
  app.run(debug=True)
 