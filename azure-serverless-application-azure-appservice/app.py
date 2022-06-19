from flask import Flask, render_template, abort
import os

app = Flask(__name__)



def load_db():
    imageList = [ x for x in os.listdir('static') if os.path.isfile('static/'+x)]
    return imageList

db = load_db()

@app.route("/")
def welcome():
    return render_template(
        "welcome.html",
        cards=db
    )


@app.route('/card/<int:index>')
def card_view(index):
    try:
        card = db[index]
        return render_template("card.html",
                               card=card,
                               index=index,
                               max_index=len(db)-1)
    except IndexError:
        abort(404)





if __name__ == '__main__' :
    app.run()