from app.models import *
from app import app, db
import random

jockeys_name = [
    'Николай Иванов',
    'Антон Горшанов',
    'Алексей Ложкин',
    'Олег Ломакин',
    'Олег Нефедов',
    'Олег Безушко',
    'Олег Холомин',
    'Андрей Казаков',
    'Андрей Глазков',
    'Андрей Цискин',
    'Надежда Шпагина',
    'Павел Кулажко',
    'Денис Юркин',
    'Владимир Набоков',
    'Евгений Ухов',
    'Сергей Востриков',
    'Игорь Вологжин',
    'Екатерина Туисова',
    'Антон Карпов',
    'Антон Никоноров',
    'Максим Шинкевич',
    'Максим Иванов',
    'Вадим Чернышев',
    'Алексей Волжев',
    'Владимир Мороз',
    'Дмитрий Дмитриев',
    'Вадим Алексеев',
    'Иван Прокофьев',
    'Егор Дутов',
    'Карп Антонов',
    'Александр Кондратьев',
    'Александр Гребенюк',
    'Денис Вадимов',
    'Иван Непомнящих',
]

horse_name = [
    'Собчак',
    'Глаша',
    'Звездочка',
    'Мила',
    'Аннушка',
    'Соловей',
    'Ветер',
    'Воздух',
    'Течение',
    'Вояка',
    'Войка',
    'Алешка',
    'Алекса',
    'Алиса',
    'Маша',
    'Миша',
    'Максим',
    'Женек',
    'Воевода',
    'Царек',
    'Плотва',
    'Кантарелла',
    'Ссуда',
    'Мисса',
    'Луана',
    'Жизель',
    'Антиша',
    'Понтий',
    'Проша',
    'Прося',
    'Вася',
    'Ванек',
    'Иаша',
    'Канделаки',
]

owner_name = [
    'Босс Качалки'
    'Александр Пистолетов',
    'Михаил Лазушко',
    'Дмитрий Бердников',
    'Владимир Путим',
    'Кузьма Дмитриев',
    'Алексей Михалков',
    'Михаил Алексеев',
]

address = [
    'Москва, Ленина 22',
    'Москва, 3-я улица Строителей, 17',
    'Раменки, Васильева 33',
    'Мытищи, 4-й квартал 33к1',
    'Реутов, Пушкина 3',
    'Видное, Советская 99',
    'Богородское, Крылова 43',
    'Москва, Артюхиной 30'
]

placee = [
    'GYM',
    'TSUM',
    'Мытищи',
    'Красная площадь',
    'Московский Ипподром',
    'МЦК',
    'Нагатинский затон',
    'Крылатское',
    'Владимирова',
    'Дмитровка',
    'Первомайский'
]

competition_name = [
    'Дракар',
    'Лошадиный бой',
    'Гон-камикадзе',
    'Каминг хорс',
    'Хорс раннинг',
    'Лошадиная сила',
    'Жокей на мыло',
    'Мило-Лошадь',
    'Гонка и вино',
]

for i in range(30):
    jockeys = Jockeys(
        name=jockeys_name[random.randint(0, (len(jockeys_name)-1))],
        age = random.randint(18,32),
        address = address[random.randint(0, (len(address)-1))],
        rating = random.randint(2,10)
    )
    db.session.add(jockeys)
    db.session.commit()

for i in range(10):
    owners = Owners(
        name=owner_name[random.randint(0, (len(owner_name)-1))],
        address = address[random.randint(0, (len(address)-1))],
        telephone = random.randint(10000,99999)
    )
    db.session.add(owners)
    db.session.commit()

for i in range(30):
    horses = Horses(
        name=horse_name[random.randint(0, (len(horse_name)-1))],
        age = random.randint(3,13),
        owner_id = random.randint(1,10)
    )
    db.session.add(horses)
    db.session.commit()

for i in range(10):
    competition = Competition (
        name = competition_name[random.randint(0, (len(competition_name)-1))],
        place = placee[random.randint(0, (len(placee)-1))],
        timeplace = random.randint(2018,2021)
    )
    db.session.add(competition)
    db.session.commit()
    for pla in range(1,7):
        competitionDetail = CompetitionDetail(
        winner_place = pla,
        id_jockey = random.randint(1,30),
        id_horse = random.randint(1,30),
        id_competition = i
        )
        
        db.session.add(competitionDetail)
        db.session.commit()