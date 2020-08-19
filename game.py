from ai import *

if __name__ == "__main__":

    board = Board()
    solver = ai(True)
    if board.board.is_game_over():
        print(board.board.result())
        exit(0)

    print(board)

    book_move = True
    reader = chess.polyglot.open_reader("ProDeo.bin")

    while True:
        print("Thinking ...\n")
        if book_move:
            entries = reader.find_all(board.board, minimum_weight=200)
            if sum(1 for entry in entries) == 0:
                book_move = False
        if book_move:
            move = reader.find(board.board).move
            print(move)
            board.push(move)
        else:

            start = time.time()

            move = solver.get_move(board)
            print(move)
            board.push(move)

        print (board)

        if board.board.is_game_over():
            print(board.board.result())
            break

        ok = False
        print("""Enter Move in uci notation (from_square)(to_square)(Q/B/R/N if pawn promotion). \n
To move from e2 to e4, enter 'e2e4'.\n
To promote pawn at a7 to queen, enter 'a7a8Q'.\n
To quit enter 'resign'\n""")
        while not ok:
            st = input()
            if st == "resign":
                break
            try:
                #move = board.board.parse_san(st)
                move = chess.Move.from_uci(st)
                if board.board.is_legal(move):
                    board.push(move)
                    ok = True
                else:
                    raise ValueError
            except:
                print ("error")

        if board.board.is_game_over():
            print(board.board.result())
            break
        print(board)
        print()

