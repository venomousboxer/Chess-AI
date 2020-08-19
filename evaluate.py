import chess
import copy

pawn_table_white = [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0],
    [1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0],
    [0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5],
    [0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0],
    [0.5, -0.5, -1.0, 0.0, 0.0, -1.0, -0.5, 0.5],
    [0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
]
pawn_table_black = copy.deepcopy(pawn_table_white)
pawn_table_white.reverse()

knight_table_white = [
    [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
    [-4.0, -2.0, 0.0, 0.0, 0.0, 0.0, -2.0, -4.0],
    [-3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0, -3.0],
    [-3.0, 0.5, 1.5, 2.0, 2.0, 1.5, 0.5, -3.0],
    [-3.0, 0.0, 1.5, 2.0, 2.0, 1.5, 0.0, -3.0],
    [-3.0, 0.5, 1.0, 1.5, 1.5, 1.0, 0.5, -3.0],
    [-4.0, -2.0, 0.0, 0.5, 0.5, 0.0, -2.0, -4.0],
    [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]
]
knight_table_black = copy.deepcopy(knight_table_white)
knight_table_white.reverse()

bishop_table_white = [
    [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
    [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0],
    [-1.0, 0.0, 0.5, 1.0, 1.0, 0.5, 0.0, -1.0],
    [-1.0, 0.5, 0.5, 1.0, 1.0, 0.5, 0.5, -1.0],
    [-1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, -1.0],
    [-1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0],
    [-1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5, -1.0],
    [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]
]
bishop_table_black = copy.deepcopy(bishop_table_white)
bishop_table_white.reverse()

rook_table_white = [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5],
    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
    [0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0]
]
rook_table_black = copy.deepcopy(rook_table_white)
rook_table_white.reverse()

queen_table_white = [
    [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
    [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0],
    [-1.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0],
    [-0.5, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5],
    [0.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5],
    [-1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0],
    [-1.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, -1.0],
    [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]
]
queen_table_black = copy.deepcopy(queen_table_white)
queen_table_white.reverse()

king_table_white = [

    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
    [-1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
    [1.0, 1.0, -0.5, -1.0, -1.0, -1.0, 1.0, 1.0],
    [2.0, 3.0, 1.5, -1.0, 0.0, -1.0, 3.0, 2.0]
]
king_table_black = copy.deepcopy(king_table_white)
king_table_white.reverse()

king_endgame_table_white = [
    [-5.0, -4.0, -3.0, -2.0, -2.0, -3.0, -4.0, -5.0],
    [-3.0, -2.0, -1.0, 0.0, 0.0, -1.0, -2.0, -3.0],
    [-3.0, -1.0, 2.0, 3.0, 3.0, 2.0, -1.0, -3.0],
    [-3.0, -1.0, 3.0, 4.0, 4.0, 3.0, -1.0, -3.0],
    [-3.0, -1.0, 3.0, 4.0, 4.0, 3.0, -1.0, -3.0],
    [-3.0, -1.0, 2.0, 3.0, 3.0, 2.0, -1.0, -3.0],
    [-3.0, -3.0, 0.0, 0.0, 0.0, 0.0, -3.0, -3.0],
    [-5.0, -3.0, -3.0, -3.0, -3.0, -3.0, -3.0, -5.0]
]

king_endgame_table_black = copy.deepcopy(king_endgame_table_white)
king_endgame_table_white.reverse()


def eval(state: chess.Board, debug=False):
    value = {chess.PAWN: 100, chess.KNIGHT: 325, chess.BISHOP: 350, chess.ROOK: 525, chess.QUEEN: 950, chess.KING: 200}

    doubled_pawns = 0
    white_pawns = set({})
    white_pawn_files = [0 for i in range(8)]
    black_pawns = set({})
    black_pawn_files = [0 for i in range(8)]

    for i in range(8):
        b = 0
        w = 0
        for j in range(8):
            if str(state.piece_at(8 * j + i)) == 'P':
                white_pawn_files[i] = 1
                w += 1
                white_pawns.add(j * 8 + i)
            elif str(state.piece_at(8 * j + i)) == 'p':
                black_pawn_files[i] = 1
                black_pawns.add(j * 8 + i)
                b += 1
        if w > 1:
            doubled_pawns += w - 1
        if b > 1:
            doubled_pawns -= b - 1

    w_safe = set({})
    b_safe = set({})

    null_added = False

    if not state.turn:
        null_added = True
        state.push(chess.Move.null())

    for move in state.pseudo_legal_moves:
        if int(move.from_square) in white_pawns:
            w_safe.add(int(move.from_square))

    if null_added:
        state.pop()
        null_added = False
    else:
        state.push(chess.Move.null())
        null_added = True

    for move in state.pseudo_legal_moves:
        if int(move.from_square) in black_pawns:
            b_safe.add(int(move.from_square))
    if null_added:
        state.pop()

    blocked_pawns = len(white_pawns) - len(w_safe) - (len(black_pawns) - len(b_safe))

    isolated_pawns = 0

    for pawn in white_pawns:
        file = chess.square_file(pawn)
        iso = 0
        if file > 0:
            if white_pawn_files[file - 1] != 0:
                iso += 1

        if file < 7:
            if white_pawn_files[file + 1] != 0:
                iso += 1
        if iso == 0:
            isolated_pawns += 1

    for pawn in black_pawns:
        file = chess.square_file(pawn)
        iso = 0
        if file > 0:
            if black_pawn_files[file - 1] != 0:
                iso += 1

        if file < 7:
            if black_pawn_files[file + 1] != 0:
                iso += 1
        if iso == 0:
            isolated_pawns -= 1

    score_kings = 0
    score_kings_end = 0
    score_queens = 0
    score_rook = 0
    score_bishop_knight = 0
    score_pawn = 0
    material_score = 0

    pieces = state.piece_map()

    qb = 0
    qw = 0
    opb = 0
    opw = 0

    for square, piece in pieces.items():
        file = chess.square_file(square)
        rank = chess.square_rank(square)
        if piece.color == chess.WHITE:
            if piece.piece_type == chess.PAWN:
                score_pawn += pawn_table_white[rank][file]
                material_score += value[chess.PAWN]
            elif piece.piece_type == chess.KNIGHT:
                score_bishop_knight += knight_table_white[rank][file]
                material_score += value[chess.KNIGHT]
                opw += 1
            elif piece.piece_type == chess.BISHOP:
                score_bishop_knight += bishop_table_white[rank][file]
                material_score += value[chess.BISHOP]
                opw += 1
            elif piece.piece_type == chess.ROOK:
                score_rook += rook_table_white[rank][file]
                material_score += value[chess.ROOK]
                opw += 1
            elif piece.piece_type == chess.QUEEN:
                score_queens += queen_table_white[rank][file]
                material_score += value[chess.QUEEN]
                qw += 1
            elif piece.piece_type == chess.KING:
                score_kings += king_table_white[rank][file]
                score_kings_end += king_endgame_table_white[rank][file]
        else:
            if piece.piece_type == chess.PAWN:
                score_pawn -= pawn_table_black[rank][file]
                material_score -= value[chess.PAWN]
            elif piece.piece_type == chess.KNIGHT:
                score_bishop_knight -= knight_table_black[rank][file]
                material_score -= value[chess.KNIGHT]
                opb += 1
            elif piece.piece_type == chess.BISHOP:
                score_bishop_knight -= bishop_table_black[rank][file]
                material_score -= value[chess.BISHOP]
                opb += 1
            elif piece.piece_type == chess.ROOK:
                score_rook -= rook_table_black[rank][file]
                material_score -= value[chess.ROOK]
                opb += 1
            elif piece.piece_type == chess.QUEEN:
                score_queens -= queen_table_black[rank][file]
                material_score -= value[chess.QUEEN]
                qb += 1
            elif piece.piece_type == chess.KING:
                score_kings -= king_table_black[rank][file]
                score_kings_end -= king_endgame_table_black[rank][file]

    score_mobility = state.legal_moves.count()
    state.push(chess.Move.null())
    score_mobility -= state.legal_moves.count()
    state.pop()

    if not state.turn:
        score_mobility *= -1

    position_score = score_queens + score_rook + score_bishop_knight + score_pawn

    if qb + qw == 0 or (qb == 1 and qw == 1 and opb == 0 and opw == 0):
        position_score += score_kings_end
    else:
        position_score += score_kings

    score = 10 * position_score + \
            score_mobility + \
            material_score + \
            - 15 * (doubled_pawns + 0.5 * isolated_pawns + 0.5 * blocked_pawns)

    return score


def eval_light(state: chess.Board):
    value = {chess.PAWN: 100, chess.KNIGHT: 325, chess.BISHOP: 350, chess.ROOK: 525, chess.QUEEN: 950, chess.KING: 200}

    score_kings = 0
    score_kings_end = 0
    score_queens = 0
    score_rook = 0
    score_bishop_knight = 0
    score_pawn = 0
    material_score = 0

    pieces = state.piece_map()

    qb = 0
    qw = 0
    opb = 0
    opw = 0

    for square, piece in pieces.items():
        file = chess.square_file(square)
        rank = chess.square_rank(square)
        if piece.color == chess.WHITE:
            if piece.piece_type == chess.PAWN:
                score_pawn += pawn_table_white[rank][file]
                material_score += value[chess.PAWN]
            elif piece.piece_type == chess.KNIGHT:
                score_bishop_knight += knight_table_white[rank][file]
                material_score += value[chess.KNIGHT]
                opw += 1
            elif piece.piece_type == chess.BISHOP:
                score_bishop_knight += bishop_table_white[rank][file]
                material_score += value[chess.BISHOP]
                opw += 1
            elif piece.piece_type == chess.ROOK:
                score_rook += rook_table_white[rank][file]
                material_score += value[chess.ROOK]
                opw += 1
            elif piece.piece_type == chess.QUEEN:
                score_queens += queen_table_white[rank][file]
                material_score += value[chess.QUEEN]
                qw += 1
            elif piece.piece_type == chess.KING:
                score_kings += king_table_white[rank][file]
                score_kings_end += king_endgame_table_white[rank][file]
        else:
            if piece.piece_type == chess.PAWN:
                score_pawn -= pawn_table_black[rank][file]
                material_score -= value[chess.PAWN]
            elif piece.piece_type == chess.KNIGHT:
                score_bishop_knight -= knight_table_black[rank][file]
                material_score -= value[chess.KNIGHT]
                opb += 1
            elif piece.piece_type == chess.BISHOP:
                score_bishop_knight -= bishop_table_black[rank][file]
                material_score -= value[chess.BISHOP]
                opb += 1
            elif piece.piece_type == chess.ROOK:
                score_rook -= rook_table_black[rank][file]
                material_score -= value[chess.ROOK]
                opb += 1
            elif piece.piece_type == chess.QUEEN:
                score_queens -= queen_table_black[rank][file]
                material_score -= value[chess.QUEEN]
                qb += 1
            elif piece.piece_type == chess.KING:
                score_kings -= king_table_black[rank][file]
                score_kings_end -= king_endgame_table_black[rank][file]

    position_score = score_queens + score_rook + score_bishop_knight + score_pawn

    if qb + qw == 0 or (qb == 1 and qw == 1 and opb == 0 and opw == 0):
        position_score += score_kings_end
    else:
        position_score += score_kings
    score = 10 * position_score + material_score

    return score
