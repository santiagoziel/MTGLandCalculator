from flask import  render_template, request
from werkzeug.utils import secure_filename

import os, random, pickle, re
from collections import Counter

from dta_pkt import app, r
from dta_pkt.forms import deckUploadForm
from dta_pkt.socket_events import socketio

from dta_pkt.utils.getColors import gen_color_identity
from dta_pkt.utils.goldfishGetDecks import get_list_of_decks
from dta_pkt.utils.goldfishCards import get_lands_list
from dta_pkt.utils.getDisplayInfo import gen_display_info

@app.route("/", methods=['GET', 'POST'])
def dashboard():
    form = deckUploadForm()
    if form.validate_on_submit():
        id = random.randint(1,100000)
        filename = secure_filename(form.file.data.filename)
        form.file.data.save(app.config['UPLOAD_FOLDER'] + filename)
        #gen an id numner
        #here in reality in puting stuff into the db unde rthe id
        socketio.emit("updateBar", {"status" :5, "message": "Getting Color identity"})
        colors, lands, coloridentity = gen_color_identity(filename)
        socketio.emit("updateBar", {"status" :15, "message": "Getting Similar Decks"})
        list_of_decks = get_list_of_decks(coloridentity)
        socketio.emit("updateBar", {"status" :25, "message": "Scraping Similar decks"})
        land_list = []
        for i, deck in enumerate(list_of_decks[0:5], 1):
            land_list.append(get_lands_list(deck))
            socketio.emit("updateBar", {"status" :25 + ( i * 10), "message": f"Decks scraped {i} out of 5"})
        counter = Counter()
        for d in land_list:
            counter.update(d)
        socketio.emit("updateBar", {"status" :85, "message": "Rendering Info"})
        display_info = gen_display_info(counter.most_common(6))
        os.remove(app.config['UPLOAD_FOLDER'] + filename)

        deck = {"Name": filename, "display_info" : pickle.dumps(display_info), "colors" : pickle.dumps(colors), "lands" : pickle.dumps(lands)}
        r.hmset(id, deck)
        socketio.emit("updateBar", {"status" :100, "message": "All Done"})
        #plus the id number
        return f"/display/{id}"
    return render_template("dashboard.html", form = form)


@app.route('/display/<id>', methods = ['GET', 'POST'])
def display(id):
    deck = r.hgetall(id)
    #if i want users to be able to re check their decks i just remove this line
    r.delete(id)

    name = re.sub('[-_]',' ',deck[b'Name'].decode("utf-8")[:-4])
    name = re.sub('Deck', '', name)
    display_info = pickle.loads(deck[b'display_info'])
    colors = pickle.loads(deck[b'colors'])
    lands = pickle.loads(deck[b'lands'])
    return render_template("display.html", name = name, display_info = display_info, colors = colors, lands = lands)
