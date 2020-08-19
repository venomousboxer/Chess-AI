from evaluate import *
from hasher import *

class Board:
    value = {chess.PAWN: 100, chess.KNIGHT: 325, chess.BISHOP: 350, chess.ROOK: 525, chess.QUEEN: 950, chess.KING: 200}
    hasher = Hasher()

    def __init__(self, fen=None):
        if fen is not None:
            self.board = chess.Board(fen=fen)
            self.score = eval_light(self.board)
            self.qw, self.qb, self.opw, self.opb = 0, 0, 0, 0
            for square, piece in self.board.piece_map().items():
                if piece.color:
                    if piece.piece_type == chess.QUEEN:
                        self.qw += 1
                    elif piece.piece_type != chess.PAWN and piece.piece_type != chess.KING:
                        self.opw += 1
                else:
                    if piece.piece_type == chess.QUEEN:
                        self.qb += 1
                    elif piece.piece_type != chess.PAWN and piece.piece_type != chess.KING:
                        self.opb += 1

        else:
            self.board = chess.Board()
            self.score = 0
            self.qw = 1
            self.qb = 1
            self.opw = 6
            self.opb = 6

        self.score_stack = [self.score]
        self.position_hash = Board.hasher.get_pos_hash(self.board)
        self.position_hash_stack = [self.position_hash]
        self.zobrist_hash = Board.hasher.update_hash(self.board, self.position_hash)
        self.zobrist_hash_stack = [self.zobrist_hash]

    def push(self, move:chess.Move):
        # update position hash
        position_hash_delta = Board.hasher.updated_position_hash(board=self.board, move=move)
        self.position_hash ^= position_hash_delta
        self.position_hash_stack.append(self.position_hash)

        # update score
        delta = 0
        from_file = chess.square_file(move.from_square)
        from_rank = chess.square_rank(move.from_square)
        to_file = chess.square_file(move.to_square)
        to_rank = chess.square_rank(move.to_square)
        piece = self.board.piece_at(move.from_square)
        if self.board.turn:
            if piece.piece_type == chess.PAWN:
                delta += pawn_table_white[to_rank][to_file] - pawn_table_white[from_rank][from_file]
            if piece.piece_type == chess.KNIGHT:
                delta += knight_table_white[to_rank][to_file] - knight_table_white[from_rank][from_file]
            if piece.piece_type == chess.BISHOP:
                delta += bishop_table_white[to_rank][to_file] - bishop_table_white[from_rank][from_file]
            if piece.piece_type == chess.ROOK:
                delta += rook_table_white[to_rank][to_file] - rook_table_white[from_rank][from_file]
            if piece.piece_type == chess.QUEEN:
                delta += queen_table_white[to_rank][to_file] - queen_table_white[from_rank][from_file]
            if piece.piece_type == chess.KING:
                if self.qb + self.qw == 0 or (self.qb == 1 and self.qw == 1 and self.opb == 0 and self.opw == 0):
                    delta += king_endgame_table_white[to_rank][to_file] - king_endgame_table_white[from_rank][from_file]
                else:
                    delta += king_table_white[to_rank][to_file] - king_table_white[from_rank][from_file]

            delta *= 10
            if self.board.piece_at(move.to_square) is not None:
                piece = self.board.piece_at(move.to_square).piece_type
                delta += Board.value[piece]
                if piece == chess.QUEEN:
                    self.qb -= 1
                elif piece != chess.PAWN:
                    self.opb -= 1

            if move.promotion:
                delta += Board.value[move.promotion]
                if move.promotion == chess.QUEEN:
                    self.qw += 1
                elif move.promotion in [chess.KNIGHT, chess.BISHOP, chess.ROOK]:
                    self.opw += 1

        else:
            if piece.piece_type == chess.PAWN:
                delta -= pawn_table_black[to_rank][to_file] - pawn_table_black[from_rank][from_file]
            if piece.piece_type == chess.KNIGHT:
                delta -= knight_table_black[to_rank][to_file] - knight_table_black[from_rank][from_file]
            if piece.piece_type == chess.BISHOP:
                delta -= bishop_table_black[to_rank][to_file] - bishop_table_black[from_rank][from_file]
            if piece.piece_type == chess.ROOK:
                delta -= rook_table_black[to_rank][to_file] - rook_table_black[from_rank][from_file]
            if piece.piece_type == chess.QUEEN:
                delta -= queen_table_black[to_rank][to_file] - queen_table_black[from_rank][from_file]
            if piece.piece_type == chess.KING:
                if self.qb + self.qw == 0 or (self.qb == 1 and self.qw == 1 and self.opb == 0 and self.opw == 0):
                    delta -= king_endgame_table_black[to_rank][to_file] - king_endgame_table_black[from_rank][from_file]
                else:
                    delta -= king_table_black[to_rank][to_file] - king_table_black[from_rank][from_file]

            delta *= 10
            if self.board.piece_at(move.to_square) is not None:
                piece = self.board.piece_at(move.to_square).piece_type
                delta -= Board.value[piece]
                if piece == chess.QUEEN:
                    self.qw -= 1
                elif piece != chess.PAWN and piece != chess.KING:
                    self.opw -= 1

            if move.promotion:
                delta -= Board.value[move.promotion]
                if move.promotion == chess.QUEEN:
                    self.qb += 1
                elif move.promotion in [chess.KNIGHT, chess.BISHOP, chess.ROOK]:
                    self.opb += 1

        self.board.push(move)
        self.score += delta
        self.score_stack.append(self.score)

        self.zobrist_hash = Board.hasher.update_hash(self.board, self.position_hash)
        self.zobrist_hash_stack.append(self.zobrist_hash)

    def pop(self):
        self.board.pop()

        self.position_hash_stack.pop()
        self.position_hash = self.position_hash_stack[-1]

        self.zobrist_hash_stack.pop()
        self.zobrist_hash = self.zobrist_hash_stack[-1]

        self.score_stack.pop()
        self.score = self.score_stack[-1]

    def __repr__(self):
        res = "\n"
        uni_pieces = {'R': '♜', 'N': '♞', 'B': '♝', 'Q': '♛', 'K': '♚', 'P': '♟',
                      'r': '♖', 'n': '♘', 'b': '♗', 'q': '♕', 'k': '♔', 'p': '♙', None: '·'}

        for i in range(8):
            res += (" " + str(8 - i) + " ")
            for j in range(8):
                square = (7 - i) * 8 + j
                if self.board.piece_at(square) is None:
                    res += uni_pieces[None] + " "
                else:
                    res += uni_pieces[str(self.board.piece_at(square))] + " "
            res += "\n"
        res += "   a b c d e f g h \n\n"
        return res

