import chess.polyglot
import time
import heapq
from board import *
from utils import heap_item, tt_entry




class ai:
    def __init__(self, white, max_time = 20, max_depth = 2000):
        self.transposition_table = dict({})
        self.start = 0
        self.terminated = False
        self.white = white
        self.max_time = max_time
        self.max_depth = max_depth

    def alpha_beta_with_memory(self, state: Board, alpha=-(10 ** 10), beta=10 ** 10,  depth=4):
        if time.time() - self.start > self.max_time:
            self.terminated = True
            return [0, chess.Move.null()]

        hash = state.zobrist_hash
        write = False
        if hash in self.transposition_table:
            data = self.transposition_table[hash]
            if data.depth < depth:
                write = True
            else:
                if data.lower_bound >= beta:
                    return [data.lower_bound, data.move]
                if data.upper_bound <= alpha:
                    return [data.upper_bound, data.move]
                alpha = max(alpha, data.lower_bound)
                beta = min(beta, data.upper_bound)

        guess = 0
        best = chess.Move.null()
        if state.board.legal_moves.count() == 0:
            try:
                res = state.board.result()
                res = res.split('-')
                res = [float(i) for i in res]
                if res[0] == 1:
                    guess += (depth + 1) * 10 ** 7
                else:
                    guess += (-depth - 1) * (10 ** 7)
            except:
                guess = 0
            if not self.white:
                guess *= -1
        elif depth == 0:
            guess = int(state.score)
            """mobility = state.board.legal_moves.count()/1.5
            state.board.push(chess.Move.null())
            mobility -= state.board.legal_moves.count()/1.5
            if not state.board.turn:
                mobility *= -1
            guess += mobility"""
            guess = int(round(guess/10, 0))
            if not self.white:
                guess *= -1
            # state.board.pop()
        else:
            moves = [move for move in state.board.legal_moves]

            if (state.board.turn and self.white) or (not state.board.turn and not self.white):
                guess = -(10 ** 10)
                a = alpha

                scores = []
                for move in moves:
                    state.push(move)
                    if self.white:
                        scores.append(heap_item((-state.score, move)))
                    else:
                        scores.append(heap_item((state.score, move)))
                    state.pop()

                heapq.heapify(scores)
                rem = len(scores)

                while rem:
                    move = heapq.heappop(scores).data[1]
                    rem -= 1
                    if guess >= beta:
                        break
                    state.push(move)

                    val = self.alpha_beta_with_memory(state, a, beta, depth - 1)[0]
                    state.pop()

                    if val > guess:
                        guess = val
                        best = move
                        a = max(a, val)

            else:

                guess = (10 ** 10)
                b = beta

                scores = []
                for move in moves:
                    state.push(move)
                    if self.white:
                        scores.append(heap_item((state.score, move)))
                    else:
                        scores.append(heap_item((-state.score, move)))
                    state.pop()

                heapq.heapify(scores)
                rem = len(scores)

                while rem:
                    move = heapq.heappop(scores).data[1]
                    rem -= 1
                    if guess <= alpha:
                        break

                    state.push(move)
                    val = self.alpha_beta_with_memory(state, alpha, b, depth - 1)[0]
                    state.pop()

                    if val < guess:
                        guess = val
                        best = move
                        b = min(b, val)

        if not write:
            return [guess, best]

        if guess <= alpha:
            temp = tt_entry(-(10 ** 10), guess, best, depth)
            self.transposition_table[hash] = temp
            if len(self.transposition_table) > 10 ** 7:
                for key in self.transposition_table.keys():
                    self.transposition_table.pop(key)
                    break

        if alpha < guess < beta:
            temp = tt_entry(guess, guess, best, depth)
            self.transposition_table[hash] = temp
            if len(self.transposition_table) > 10 ** 7:
                for key in self.transposition_table.keys():
                    self.transposition_table.pop(key)
                    break

        if guess >= beta:
            temp = tt_entry(guess, 10 ** 10, best, depth)
            self.transposition_table[hash] = temp
            if len(self.transposition_table) > 10 ** 7:
                for key in self.transposition_table.keys():
                    self.transposition_table.pop(key)
                    break

        return [guess, best]


    def mtdf(self, state: Board, depth, guess):
        upper_bound = 10 ** 10

        moves = [move for move in state.board.legal_moves]
        move = moves[0]
        lower_bound = -(10 ** 10)

        while lower_bound < upper_bound :
            if time.time() - self.start > self.max_time:
                return move

            if guess == lower_bound:
                beta = guess + 1
            else:
                beta = guess

            val = self.alpha_beta_with_memory(state, beta - 1, beta, depth)

            guess = val[0]
            move = val[1]

            if guess < beta:
                upper_bound = guess
            else:
                lower_bound = guess

        return [move, guess]



    def get_move(self, state: Board):
        self.start = time.time()
        self.terminated = False
        move = chess.Move.null()

        cur = int(round(state.score/10, 0))
        if not self.white:
            cur *= -1

        guess_odd = 0
        guess_even = cur
        for depth in range(1, self.max_depth+1, 1):
            if depth <= 1:
                move = self.mtdf(state, 1, cur)
                guess_odd = move[1]
                move = move[0]
            else:
                state.push(move)
                state.pop()

                if depth % 2 == 1:
                    temp = self.mtdf(state, depth, guess_odd)
                    if self.terminated:
                        print("depth = ", depth - 1)
                        return move
                    move = temp[0]
                    guess_odd = temp[1]
                else:
                    temp = self.mtdf(state, depth, guess_even)
                    if self.terminated:
                        print ("depth = ", depth - 1)
                        return move
                    move = temp[0]
                    guess_even = temp[1]


            if time.time() - self.start > self.max_time:
                print("depth = ", depth)
                return move
        return move
