from flask import Flask, render_template, request, redirect, url_for
from ai import *
import time
import string
import secrets


def gen_id():
    res = ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(10))
    return res

class game_state:
    def __init__(self, id, white=False, max_dep=2000, max_t=20):# user plays white if true
        self.index = id
        self.id = gen_id()
        self.board = Board()
        self.play_white = white # true if user plays white
        self.user = white # true if it is users turn
        self.book_move = True
        self.start_time = time.time()
        self.ai = ai(not white, max_t, max_dep)

    def is_over(self):
        if time.time() - self.start_time > 180*60:
            return True
        return False


app = Flask(__name__)
app.config['SECRET_KEY'] = 'adsnaskjdnaskjdn'
reader = chess.polyglot.open_reader("ProDeo.bin")

games = []
valid = dict({})
ind = dict({})

depths = [0, 3, 4, 5, 5, 5, 8, 50, 10, 50, 50]
times = [0, 1, 2, 5, 10, 20, 20, 20, 60, 60, 200]

@app.route('/', methods=['GET', 'POST'])
def start():
    if request.method == 'GET':
        return render_template('home.html')

    white = False
    if request.form['colour'] == 'white':
        white = True

    max_dep = depths[int(request.form['level'])]
    max_t = times[int(request.form['level'])]

    if len(games) < 10:
        game = game_state(len(games), white, max_dep, max_t)
        valid[game.id] = True
        ind[game.id] = len(games)
        games.append(game)
        return redirect(url_for('index', game_id = game.id))
    else:
        for i in range(10):
            if games[i].is_over():
                valid[games[i].id] = False
                game = game_state(i, white, max_dep, max_t)
                valid[game.id] = True
                ind[game.id] = i
                games[i].append(game)
                return redirect(url_for('index', game_id = game.id))
        return "SERVER BUSY !!!"



@app.route('/game/<game_id>', methods=['GET', 'POST'])
def index(game_id):
    if game_id not in valid.keys():
        return "Game not found", 404
    if not valid[game_id]:
        return "GAME IS OVER"

    i = ind[game_id]
    if request.method == 'GET':
        if games[i].board.board.is_game_over():
            return render_template('index.html', fen=str(games[i].board.board.fen()), white=games[i].play_white, message=str(games[i].board.board.result()))

        if games[i].user:
            print(1)
            print(games[i].board, games[i].board.score)
            return render_template('index.html', fen=str(games[i].board.board.fen()), white=games[i].play_white)
        print (2)
        print(games[i].board, games[i].board.score)

        if games[i].book_move:
            entries = reader.find_all(games[i].board.board, minimum_weight=100)
            if sum(1 for entry in entries) == 0:
                games[i].book_move = False
        if games[i].book_move:
            move = reader.find(games[i].board.board).move
            games[i].board.push(move)
        else:
            move = games[i].ai.get_move(games[i].board)
            games[i].board.push(move)

        games[i].user = True
        return redirect(url_for('index', game_id=game_id))

    if request.method == 'POST':
        if games[i].user:
            print (request.form)
            print (request.form['move'])
            print(3)
            print(games[i].board, games[i].board.score)
            move = str(request.form['move'])
            try:
                move = games[i].board.board.parse_san(move)
            except:
                return redirect(url_for('index', game_id=game_id))

            games[i].board.push(move)
            games[i].user = False

            return redirect(url_for('index', game_id=game_id))
        else:
            print (4)
            return redirect(url_for('index', game_id=game_id))


if __name__ == '__main__':
    app.run(debug=True)