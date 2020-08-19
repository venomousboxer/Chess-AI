import random
from ai import *

if __name__ == '__main__':
    random.seed(37)
    times = []
    for i in range(10):
        board = Board()
        solver = ai(True, max_depth=5, max_time=5000)
        book_move = True
        reader = chess.polyglot.open_reader("ProDeo.bin")

        while True:
            if book_move:
                entries = reader.find_all(board.board, minimum_weight=200)
                if sum(1 for entry in entries) == 0:
                    book_move = False
            if book_move:
                move = reader.find(board.board).move
                board.push(move)
            else:
                start = time.time()
                move = solver.get_move(board)
                times.append(time.time() - start)
                print (sum(times)/len(times))
                board.push(move)


            if board.board.is_game_over():
                break

            moves = [move for move in board.board.legal_moves]
            board.push(random.choice(moves))

            if board.board.is_game_over():
                break
    print("avg time : ", sum(times) / len(times))
