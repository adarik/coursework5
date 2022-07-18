from flask import Flask, render_template, request, redirect, url_for
from arena import Arena
from utils import get_data_for_choosing, get_unit_from_form

app = Flask(__name__)

heroes = {}

arena = Arena()


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/choose-hero/', methods=["GET", "POST"])
def chose_hero():
    if request.method == 'GET':
        return render_template(
            'hero_choosing.html',
            result=get_data_for_choosing(hero=True)
        )
    if request.method == "POST":
        player = get_unit_from_form(hero=True)
        heroes['player'] = player
        print(player.hp)
        return redirect(url_for('choose_enemy'))


@app.route('/choose-enemy/', methods=["GET", "POST"])
def choose_enemy():
    if request.method == "GET":
        return render_template('hero_choosing.html',
                               result=get_data_for_choosing())
    if request.method == "POST":
        enemy = get_unit_from_form()
        heroes['enemy'] = enemy
        return redirect(url_for("start_fight"))


@app.route('/fight/')
def start_fight():
    arena.start_game(player=heroes.get('player'), enemy=heroes.get('enemy'))
    return render_template('fight.html', heroes=heroes, result='Бой начат!')


@app.route("/fight/hit")
def hit():
    if arena.game_is_running:
        result = arena.player_hit()
        return render_template('fight.html', heroes=heroes, result=result)
    else:
        return render_template('fight.html', heroes=heroes, result=arena.battle_result)


@app.route('/fight/use-skill')
def use_skill():
    if arena.game_is_running:
        result = arena.player_use_skill()
        return render_template('fight.html', heroes=heroes, result=result)
    else:
        return render_template('fight.html', heroes=heroes, result=arena.battle_result)


@app.route("/fight/pass-turn")
def pass_turn():
    if arena.game_is_running:
        result = arena.next_turn()
        return render_template('fight.html', heroes=heroes, result=result)
    else:
        return render_template('fight.html', heroes=heroes, result=arena.battle_result)


@app.route("/fight/end-fight")
def end_fight():
    return render_template("index.html", heroes=heroes)


if __name__ == "__main__":
    app.run()
