from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user/<username>')
def user(username):
    users = {
        "dat" : {
            "name": "Pham Tien Dat",
            "age": 25,
            "hobbies": "game",
        },
        "hoang" : {
            "name": "Pham Dinh Hoang",
            "age": 23,
            "hobbies": "girls",
        },
        "linh" : {
            "name" : "Nguyen Khanh Linh",
            "age" : 27,
            "hobbies" : "eat",
        }
    }

    return render_template('serious_ex2.html', username=username,
                            users=users)

if __name__ == '__main__':
  app.run(debug=True)
 