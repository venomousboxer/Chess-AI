from ai import *
import chess.engine

engine = chess.engine.SimpleEngine.popen_uci("stockfish")


if __name__ == '__main__':

    times = []
    wins = 0
    losses = 0
    draws = 0
    fens = ['8/8/5p2/1P1K1k2/8/2r5/8/7R w - - 0 0',
            '3k4/5ppp/2q5/3p2r1/8/1Q3P2/P4P1P/3R3K w - - 0 1',
            '4R3/1k6/1p2P1p1/p7/4r3/1P1r4/1K6/2R5 w - - 0 0',
            '5k2/R7/3K4/4p3/5P2/8/8/5r2 w - - 0 0',
            '5k2/1R6/4p1p1/1pr3Pp/7P/1K6/8/8 w - - 0 0']
    for i in range(5):
        board = Board(fen=fens[i])
        solver = ai(True, max_depth=6, max_time=5000)

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
                print(move, end=" ")
            else:
                start = time.time()
                move = solver.get_move(board)
                if len(board.board.move_stack) > 12:
                    times.append(time.time() - start)
                    print(sum(times) / len(times))
                board.push(move)
                print(move, end=" ")



            if board.board.is_game_over():
                if board.board.is_checkmate():
                    wins += 1
                else:
                    draws += 1
                break

            result = engine.play(board.board, chess.engine.Limit(depth=1, time=0.010))
            board.push(result.move)
            print(result.move)
            if board.board.is_game_over():
                if board.board.is_checkmate():
                    losses += 1
                else:
                    draws += 1
                break
    print(wins, " - ", draws, " - ", losses)
    print("avg time : ", sum(times) / len(times))
