from flask import  render_template, request
from werkzeug.utils import secure_filename

from collections import Counter

from dta_pkt import app, r
from dta_pkt.forms import deckUploadForm
from dta_pkt.socket_events import socketio

from dta_pkt.utils.getColors import gen_color_identity
from dta_pkt.utils.goldfishGetDecks import get_list_of_decks
from dta_pkt.utils.goldfishCards import get_lands_list
from dta_pkt.utils.getDisplayInfo import gen_display_info

import os, random, pickle

@app.route("/", methods=['GET', 'POST'])
def dashboard():
    form = deckUploadForm()
    if form.validate_on_submit():
        id = random.randint(0,100000)
        print("##########################")
        print(id)
        print("##########################")
        filename = secure_filename(form.file.data.filename)
        form.file.data.save(app.config['UPLOAD_FOLDER'] + filename)
        #gen an id numner
        #here in reality in puting stuff into the db unde rthe id
        colors, lands, coloridentity = gen_color_identity(filename)
        socketio.emit("updateBar", 25)
        list_of_decks = get_list_of_decks(coloridentity)
        socketio.emit("updateBar", 50)
        land_list = []
        for deck in list_of_decks[0:4]:
            land_list.append(get_lands_list(deck))
        counter = Counter()
        for d in land_list:
            counter.update(d)
        socketio.emit("updateBar", 75)
        display_info = gen_display_info(counter.most_common(6))
        os.remove(app.config['UPLOAD_FOLDER'] + filename)

        deck = {"display_info" : pickle.dumps(display_info), "colors" : pickle.dumps(colors), "lands" : pickle.dumps(lands)}
        r.hmset(id, deck)
        socketio.emit("updateBar", 100)
        #plus the id number
        return f"/display/{id}"
    return render_template("dashboard.html", form = form)


@app.route('/display/<id>', methods = ['GET', 'POST'])
def display(id):
    deck = r.hgetall(id)
    #if i want users to be able to re check their decks i just remove this line
    r.delete(id)
    display_info = pickle.loads(deck[b'display_info'])
    colors = pickle.loads(deck[b'colors'])
    lands = pickle.loads(deck[b'lands'])
    return render_template("display.html", display_info = display_info, colors = colors, lands = lands)
