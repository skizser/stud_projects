# -*- coding: utf-8 -*-
from flask import Flask, render_template, url_for, request, redirect
from app import app, db
from app.models import Competition, Horses, Jockeys, Owners, CompetitionDetail

@app.route('/')
@app.route('/home')
@app.route('/competition')
def index():
    competition = Competition.query.order_by(Competition.id.asc()).all()
    return render_template("index.html", competition=competition)

@app.route('/horses')  # все плюхи с лошадями : отображение, детально, удаление, редактирование
def horses():
    horses = Horses.query.order_by(Horses.id.asc()).all()
    owners = Owners.query.order_by(Owners.id.asc()).all()
    return render_template("horses.html", horses=horses, owners=owners)

@app.route('/horses/<int:id>')  # посмотреть детально лошадь
def horse_detail(id):
    horse = Horses.query.get(id)
    competitionDetail = CompetitionDetail.query.filter_by(id_horse=horse.id).all()
    owners = Owners.query.order_by(Owners.id.asc()).all()
    jockeys = Jockeys.query.order_by(Jockeys.id.asc()).all()
    competition = Competition.query.order_by(Competition.id.asc()).all()

    return render_template("horse_detail.html", horse=horse, competitionDetail=competitionDetail, owners=owners, jockeys=jockeys, competition=competition)

@app.route('/horses/<int:id>/del')  # удалить лошадь
def horse_delete(id):
    horse = Horses.query.get_or_404(id)

    try:
        db.session.delete(horse)
        db.session.commit()
        return redirect('/horses')
    except:
        return "При удалении лошади произошла ошибка"

@app.route('/horses/<int:id>/update', methods=['POST', 'GET'])  # редактировать лошадь
def horse_update(id):
    horse = Horses.query.get(id)
    owners = Owners.query.order_by(Owners.id.asc()).all()
    if request.method == "POST":
        horse.name = request.form['name']
        horse.age = request.form['age']
        owners = request.form['id_owner']


        try:
            db.session.commit()
            return redirect('/horses')
        except:
            return "При редактировании лошади произошла ошибка"
    else:
        return render_template("horse_update.html", horse=horse, owners=owners)

@app.route('/create-horses', methods=['POST', 'GET'])  # добавить лошадь
def create_horses():
    if request.method == "POST":
        name = request.form['name']
        age = request.form['age']
        id_owner = request.form['id_owner']
        horse = Horses( name=name, age=age, owner_id=id_owner)

        try:
            db.session.add(horse)
            db.session.commit()
            return redirect('/horses')
        except:
            return "При добавление лошади произошла ошибка"
    else:
        owners = Owners.query.order_by(Owners.id.asc()).all()
        return render_template("create-horses.html", owners=owners)

@app.route('/jockeys')  # все плюхи с жокеями : отображение, детально, удаление, редактирование
def jockeys():
    jockeys = Jockeys.query.order_by(Jockeys.id.asc()).all()
    return render_template("jockeys.html", jockeys=jockeys)

@app.route('/jockeys/<int:id>') # детально
def jockeys_detail(id):
    jockey = Jockeys.query.get(id)
    competitionDetail = CompetitionDetail.query.filter_by(id_jockey=jockey.id).all()
    horses = Horses.query.order_by(Horses.id.asc()).all()
    competition = Competition.query.order_by(Competition.id.asc()).all()

    return render_template("jockeys_detail.html", horses=horses, competitionDetail=competitionDetail, jockey=jockey, competition=competition)


@app.route('/jockeys/<int:id>/del')  # удалить жакея
def jockeys_delete(id):
    jockey = Jockeys.query.get_or_404(id)

    try:
        db.session.delete(jockey)
        db.session.commit()
        return redirect('/jockeys')
    except:
        return "При удалении жокея произошла ошибка"

@app.route('/jockeys/<int:id>/update', methods=['POST', 'GET'])  # редактировать жакея
def jockey_update(id):
    jockey = Jockeys.query.get(id)
    if request.method == "POST":
        jockey.name = request.form['name']
        jockey.age = request.form['age']
        jockey.address = request.form['address']
        jockey.rating = request.form['rating']

        try:
            db.session.commit()
            return redirect('/jockeys')
        except:
            return "При редактировании жокея произошла ошибка"
    else:
        return render_template("jockeys_update.html", jockey=jockey)

@app.route('/create-jockeys', methods=['POST', 'GET'])  # добавить жокея
def create_jockeys():
    if request.method == "POST":
        name = request.form['name']
        age = request.form['age']
        address = request.form['address']
        rating = request.form['rating']

        jockeys = Jockeys( name=name, age=age, address=address, rating=rating)

        try:
            db.session.add(jockeys)
            db.session.commit()
            return redirect('/jockeys')
        except:
            return "При добавление жокея произошла ошибка"
    else:
        return render_template("create-jockeys.html")


@app.route('/owner') # все плюхи с владельцами : отображение, детально, удаление, редактирование
def owner():
    owner = Owners.query.order_by(Owners.id.asc()).all()
    return render_template("owner.html", owner=owner)

@app.route('/owner/<int:id>') # детально
def owner_detail(id):
        owner = Owners.query.get(id)
        horses = Horses.query.filter_by(owner_id=owner.id).all()
        return render_template("owner_detail.html", owner=owner, horses=horses)

@app.route('/owner/<int:id>/del')  # удалить владельца
def owner_delete(id):
    owner = Owners.query.get_or_404(id)

    try:
        db.session.delete(owner)
        db.session.commit()
        return redirect('/owner')
    except:
        return "При удалении владельца произошла ошибка"

@app.route('/owner/<int:id>/update', methods=['POST', 'GET'])  # редактировать владельца
def owner_update(id):
    owner = Owners.query.get(id)
    if request.method == "POST":
        owner.name = request.form['name']
        owner.address = request.form['address']
        owner.telephone = request.form['telephone']


        try:
            db.session.commit()
            return redirect('/owner')
        except:
            return "При редактировании владельца произошла ошибка"
    else:
        return render_template("owner_update.html", owner=owner)



@app.route('/create-owners', methods=['POST', 'GET'])  # добавить владельца лошади
def create_owners():
    if request.method == "POST":
        name = request.form['name']
        address = request.form['address']
        telephone = request.form['telephone']

        owner = Owners( name=name, address=address, telephone=telephone)

        try:
            db.session.add(owner)
            db.session.commit()
            return redirect('/owner')
        except:
            return "При добавление владельца лошади произошла ошибка"
    else:
        return render_template("create-owners.html")


@app.route('/create-competition', methods=['POST', 'GET'])  # добавить соревнование
def create_competition():
    if request.method == "POST":
        name = request.form['name']
        place = request.form['place']
        timeplace = request.form['timeplace']

        competition = Competition( name=name, place = place, timeplace = timeplace)
        db.session.add(competition)
        db.session.commit()
        for pla in range(1,7):
            winner_place = pla
            jockey = 'jockey_' + str(pla)
            horse = 'horse_' + str(pla)
            id_jockey = request.form[jockey]
            id_horse = request.form[horse]
            id_competition = Competition.query.order_by(Competition.id.desc()).first()
            competitionDetail = CompetitionDetail (winner_place=winner_place, id_competition=id_competition.id, id_horse=id_horse, id_jockey=id_jockey)
            db.session.add(competitionDetail)
            db.session.commit()
        return redirect('/competition')
    else:
        jockeys = Jockeys.query.order_by(Jockeys.id.asc()).all()
        horses = Horses.query.order_by(Horses.id.asc()).all()
        
        return render_template("create-competition.html", jockeys=jockeys, horses=horses)


@app.route('/competition/<int:id>') # детально
def competition_detail(id):
        competition = Competition.query.get(id)
        id_global = CompetitionDetail.query.filter_by(id_competition=competition.id).all()
        jockey = Jockeys.query.order_by(Jockeys.id.asc()).all()
        horse = Horses.query.order_by(Horses.id.asc()).all()

        return render_template("competition_detail.html", competition=competition, id_global=id_global, jockey=jockey, horse=horse)


@app.route('/competition/<int:id>/del')  # удалить соревнование
def comperition_delete(id):
    competition = Competition.query.get_or_404(id)

    try:
        db.session.delete(competition)
        db.session.commit()
        return redirect('/competition')
    except:
        return "При удалении соревнования произошла ошибка"


@app.route('/competition/<int:id>/update', methods=['POST', 'GET'])  # редактировать лошадь
def competition_update(id):
    competition = Competition.query.get(id)
    competitionDetail = CompetitionDetail.query.filter_by(id_competition=competition.id).all()
    if request.method == "POST":
        competition.name = request.form['name']
        competition.place = request.form['place']
        competition.timeplace = request.form['timeplace']
        count = 1
        for competition in competitionDetail:
            competition.winner_place = pla
            jockey = 'jockey_' + str(count)
            horse = 'horse_' + str(count)
            competition.id_jockey = request.form[jockey]
            competition.id_horse = request.form[horse]
            count += 1
        try:
            db.session.commit()
            return redirect('/competition')
        except:
            return "При редактировании соревнования произошла ошибка"
    else:
        jockeys = Jockeys.query.order_by(Jockeys.id.asc()).all()
        horses = Horses.query.order_by(Horses.id.asc()).all()
        return render_template("competition_update.html", competition=competition, jockeys=jockeys, horses=horses)