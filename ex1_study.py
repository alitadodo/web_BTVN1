from flask import Flask, render_template
app = Flask(__name__)

@app.route('/about-me')
def aboutme():
    info = {
        "name": "Dat",
        "worK": "Unemployment",
        "school": "HANU",
        "hobbies": "Game",
    }
    return render_template("ex1_study.html",
                            info=info)


if __name__ == '__main__':
  app.run(debug=True)
 

