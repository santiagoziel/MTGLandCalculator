from flask import  render_template, url_for, redirect, flash, request
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.utils import secure_filename

import os
from collections import Counter

from dta_pkt import app, login_manager, bcrypt, db
from dta_pkt.forms import LogInForm,RegisterForm
from dta_pkt.models import User

from dta_pkt.utils.getColors import gen_color_identity
from dta_pkt.utils.goldfishGetDecks import get_list_of_decks
from dta_pkt.utils.goldfishCards import get_lands_list
from dta_pkt.utils.getDisplayInfo import gen_display_info


#if you try to enter a page that requires log in you will be redirected to login
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("home.html")

@app.route("/dashboard", methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template("dashboard.html", user = current_user)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))

@app.route('/display', methods = ['GET', 'POST'])
def save_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)

        f.save(app.config['UPLOAD_FOLDER'] + filename)

        colors, L, coloridentity, total_symbols = gen_color_identity(filename)
        print(colors, L)
        [print(f"{key}: {(colors[key]*L)/total_symbols}") for key in colors]
        print(coloridentity)
        list_of_decks = get_list_of_decks(coloridentity)
        #print(list_of_decks)
        land_list = []
        for deck in list_of_decks[0:2]:
            land_list.append(get_lands_list(deck))
        counter = Counter()
        for d in land_list:
            counter.update(d)

        display_info = gen_display_info(counter.most_common(5))
        #print(display_info)
        os.remove(app.config['UPLOAD_FOLDER'] + filename)
        return render_template("display.html", display_info = display_info)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LogInForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                flash('You were successfully logged in')
                return redirect(url_for("dashboard"))
    return render_template("login.html", form = form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username = form.username.data, password= hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("register.html", form = form)
