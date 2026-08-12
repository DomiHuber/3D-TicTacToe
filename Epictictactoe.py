import sys
import time

import pygame as pg
from pygame.locals import *


def display(board, bigboard, show_tokens, memory, lastfield, normalcolor=(0, 0, 0), highlightcolor=(255, 0, 0), secondhighlightcolor=(255, 150, 150), centerx=350, centery=450, field=600, smallwidth=3, bigwidth=10):
    halfField = 81
    green = (0, 255, 0)
    lightgreen = (150, 255, 150)
    gray = (150, 150, 150)
    smallField = halfField / 3 * 2
    minihalfField = 20
    smallCenterx = [centerx - field / 3, centerx, centerx + field / 3]
    smallCentery = [centery - field / 3, centery, centery + field / 3]
    drawField(centerx, centery, field / 2, normalcolor, bigwidth)
    for i in range(3):
        for j in range(3):
            pg.draw.rect(screen, (255, 255, 255), pg.Rect(smallCenterx[i] - 94, smallCentery[j] - 94, 190, 190))
            x = [smallCenterx[i] - smallField, smallCenterx[i], smallCenterx[i] + smallField]
            y = [smallCentery[j] - smallField, smallCentery[j], smallCentery[j] + smallField]
            bigplayer = bigboard[i][j]
            show_token = show_tokens[i][j]
            if show_token <= 0 or (bigplayer != -1 and bigplayer !=1 and bigplayer != 3):
                if bigplayer == -1 or bigplayer == 1 or bigplayer == 3:
                    if show_token == 0:
                        color = green
                    else:
                        color = lightgreen
                elif memory == 1 and (i, j) == lastfield and bigplayer == 0:
                    color = gray
                else:
                    if bigplayer == 0:
                        color = normalcolor
                    elif bigplayer == 2:
                        color = highlightcolor
                    else:
                        color = secondhighlightcolor
                if memory == 0 or (bigplayer != 0 and bigplayer != 4) or (i, j) == lastfield:
                    drawField(smallCenterx[i], smallCentery[j], halfField, color, smallwidth)
                    for k in range(3):
                        for l in range(3):
                            player = board[i][j][k][l]
                            if player == 1:
                                pg.draw.polygon(screen, color, ((x[k] - minihalfField + 1, y[l] - minihalfField), (x[k] - minihalfField, y[l] - minihalfField + 1),
                                                                (x[k] + minihalfField - 1, y[l] + minihalfField), (x[k] + minihalfField, y[l] + minihalfField - 1)))
                                pg.draw.polygon(screen, color, ((x[k] - minihalfField + 1, y[l] + minihalfField), (x[k] - minihalfField, y[l] + minihalfField - 1),
                                                                (x[k] + minihalfField - 1, y[l] - minihalfField), (x[k] + minihalfField, y[l] - minihalfField + 1)))
                            elif player == -1:
                                pg.draw.circle(screen, color, (x[k], y[l]), minihalfField, smallwidth)
                            elif player == 10:
                                pg.draw.polygon(screen, gray, ((x[k] - minihalfField + 1, y[l] - minihalfField), (x[k] - minihalfField, y[l] - minihalfField + 1),
                                                                (x[k] + minihalfField - 1, y[l] + minihalfField), (x[k] + minihalfField, y[l] + minihalfField - 1)))
                                pg.draw.polygon(screen, gray, ((x[k] - minihalfField + 1, y[l] + minihalfField), (x[k] - minihalfField, y[l] + minihalfField - 1),
                                                                (x[k] + minihalfField - 1, y[l] - minihalfField), (x[k] + minihalfField, y[l] - minihalfField + 1)))
                            elif player == -10:
                                pg.draw.circle(screen, gray, (x[k], y[l]), minihalfField, smallwidth)
                elif memory == 1 and bigplayer == 4:
                    pg.draw.polygon(screen, secondhighlightcolor, ((smallCenterx[i] - halfField, smallCentery[j] - halfField),
                                                                   (smallCenterx[i] - halfField, smallCentery[j] + halfField),
                                                                   (smallCenterx[i] + halfField, smallCentery[j] + halfField),
                                                                   (smallCenterx[i] + halfField, smallCentery[j] - halfField)))
            else:
                if show_token == 1:
                    color = normalcolor
                else:
                    color = gray
                pg.draw.rect(screen, (255, 255, 255), pg.Rect(smallCenterx[i] - 94, smallCentery[j] - 94, 190, 190))
                if bigplayer == 1:
                    pg.draw.polygon(screen, color, ((smallCenterx[i] - halfField + 5, smallCentery[j] - halfField), (smallCenterx[i] - halfField, smallCentery[j] - halfField + 5),
                                                          (smallCenterx[i] + halfField - 5, smallCentery[j] + halfField), (smallCenterx[i] + halfField, smallCentery[j] + halfField - 5)))
                    pg.draw.polygon(screen, color, ((smallCenterx[i] - halfField + 5, smallCentery[j] + halfField), (smallCenterx[i] - halfField, smallCentery[j] + halfField - 5),
                                                          (smallCenterx[i] + halfField - 5, smallCentery[j] - halfField), (smallCenterx[i] + halfField, smallCentery[j] - halfField + 5)))
                elif bigplayer == -1:
                    pg.draw.circle(screen, color, (smallCenterx[i], smallCentery[j]), halfField, bigwidth)
                else:
                    label = myfont.render("Draw!", True, color)
                    screen.blit(label, (smallCenterx[i] - 40, smallCentery[j] - 23))

    pg.display.update()


def drawField(centerx, centery, halfField, gridColor, width):
    halfSmallField = halfField / 3
    pg.draw.line(screen, gridColor, (centerx - halfSmallField , centery + halfField), (centerx - halfSmallField, centery - halfField), width)
    pg.draw.line(screen, gridColor, (centerx + halfSmallField , centery + halfField), (centerx + halfSmallField, centery - halfField), width)
    pg.draw.line(screen, gridColor, (centerx - halfField , centery + halfSmallField), (centerx + halfField, centery + halfSmallField), width)
    pg.draw.line(screen, gridColor, (centerx - halfField , centery - halfSmallField), (centerx + halfField, centery - halfSmallField), width)


def get_coordinate(mouseposition, centerx=350, centery=450, field=600):
    x, y = mouseposition
    smallField = 81 / 3 * 2
    smallCenterx = [centerx - field / 3, centerx, centerx + field / 3]
    smallCentery = [centery - field / 3, centery, centery + field / 3]
    miniCenterx = []
    miniCentery = []
    for i in range(3):
        miniCenterx.extend([smallCenterx[i] - smallField, smallCenterx[i], smallCenterx[i] + smallField])
        miniCentery.extend([smallCentery[i] - smallField, smallCentery[i], smallCentery[i] + smallField])
    return min(miniCenterx, key=lambda a: abs(a - x)), min(miniCentery, key=lambda a: abs(a - y))


def get_indicies(x, y, coordinates):
    for i, a in enumerate(coordinates):
        for j, b in enumerate(a):
            for k, c in enumerate(b):
                if (x, y) in c:
                    return i, j, k, c.index((x, y))


def checkClickable(board, bigboard, mouseposition, coordinates, hand, player):
    smallwidth = 3
    color = (150, 150, 150)
    minihalfField = 20
    halfField = 81
    centerx = 350
    centery = 450
    field = 600
    smallCenterx = [centerx - field / 3, centerx, centerx + field / 3]
    smallCentery = [centery - field / 3, centery, centery + field / 3]
    x, y = get_coordinate(mouseposition) # Koordinaten der Feldmittelpunkte
    i, j, k, l = get_indicies(x, y, coordinates)
    for a in range(3):
        for b in range(3):
            if bigboard[a][b] == 4:
                bigboard[a][b] = 0
            elif bigboard[a][b] == 5:
                bigboard[a][b] = 2
    for a in range(3):
        for b in range(3):
            for c in range(3):
                for d in range(3):
                    if board[a][b][c][d] == -10 or board[a][b][c][d] == 10:
                        board[a][b][c][d] = 0
    if (bigboard[i][j] == 2 or bigboard[i][j] == 5) and board[i][j][k][l] == 0 and coordinates[i][j][k][l][0] - minihalfField <= mouseposition[0] and coordinates[i][j][k][l][0] + minihalfField >= mouseposition[0] and coordinates[i][j][k][l][1] - minihalfField <= mouseposition[1] and coordinates[i][j][k][l][1] + minihalfField >= mouseposition[1]:
        pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
        next_win = False
        board[i][j][k][l] = player
        if winner(board[i][j]) != 0:
            next_win = True
        board[i][j][k][l] = 0
        if next_win and i == k and j == l:
                for a in range(3):
                    for b in range(3):
                        if bigboard[a][b] == 0:
                            bigboard[a][b] = 4
        elif bigboard[k][l] == 0:
            bigboard[k][l] = 4
        elif bigboard[k][l] == 2:
            bigboard[k][l] = 5
        elif gamevariant == 1 or next_win:
            for a in range(3):
                for b in range(3):
                    if bigboard[a][b] == 0:
                        bigboard[a][b] = 4
                    elif gamevariant == 1 and bigboard[a][b] == 2:
                        bigboard[a][b] = 5
        else:
            bigboard[i][j] = 5
        '''for ii, a in enumerate(coordinates[i][j]):
            for jj, b in enumerate(a):
                if board[i][j][ii][jj] == 0:
                    pg.draw.polygon(screen, (255, 255, 255), (
                    (b[0] - minihalfField, b[1] - minihalfField), (b[0] - minihalfField, b[1] + minihalfField),
                    (b[0] + minihalfField, b[1] - minihalfField), (b[0] + minihalfField, b[1] + minihalfField)))
        if player == 1:
            pg.draw.polygon(screen, color, (
            (x - minihalfField + 1, y - minihalfField), (x - minihalfField, y - minihalfField + 1),
            (x + minihalfField - 1, y + minihalfField), (x + minihalfField, y + minihalfField - 1)))
            pg.draw.polygon(screen, color, (
            (x - minihalfField + 1, y + minihalfField), (x - minihalfField, y + minihalfField - 1),
            (x + minihalfField - 1, y - minihalfField), (x + minihalfField, y - minihalfField + 1)))
        elif player == -1:
            pg.draw.circle(screen, color, (x, y), minihalfField, smallwidth)
        pg.display.update()'''
        if player == 1:
            board[i][j][k][l] = 10
        elif player == -1:
            board[i][j][k][l] = -10
        return 1
    else:
        bigcoordinates = coordinates[i][j][1][1]
        if (bigboard[i][j] == -1 or bigboard[i][j] == 1 or bigboard[i][j] == 3) and mouseposition[0] >= bigcoordinates[0] - halfField and mouseposition[0] <= bigcoordinates[0] + halfField and mouseposition[1] >= bigcoordinates[1] - halfField and mouseposition[1] <= bigcoordinates[1] + halfField:
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
            return 2
    if not hand:
        pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
    return 0


def winner(smallboard):
    for i in range(3):
        if (smallboard[i][0] == 1 or smallboard[i][0] == -1) and smallboard[i][0] == smallboard[i][1] == smallboard[i][2]:
            return smallboard[i][0]
        if (smallboard[0][i] == 1 or smallboard[0][i] == -1) and smallboard[0][i] == smallboard[1][i] == smallboard[2][i]:
            return smallboard[0][i]
    if (smallboard[0][0] == 1 or smallboard[0][0] == -1) and smallboard[0][0] == smallboard[1][1] == smallboard[2][2]:
        return smallboard[0][0]
    if (smallboard[0][2] == 1 or smallboard[0][2] == -1) and smallboard[0][2] == smallboard[1][1] == smallboard[2][0]:
        return smallboard[0][2]

    for i in range(3):
        for j in range(3):
            if smallboard[i][j] == 0 or smallboard[i][j] == 2 or smallboard[i][j] == 4 or smallboard[i][j] == 5:
                return 0
    return 3


def evaluate(board, bigboard):
    values = [[0 for i in range(3)] for j in range(3)]
    score = 0
    for i, bigcolumn in enumerate(bigboard):
        player1 = 0
        player2 = 0
        draw = False
        for j, bigfield in enumerate(bigcolumn):
            if bigfield:
                if bigfield == 1:
                    player1 += 1
                elif bigfield == -1:
                    player2 -= 1
                elif bigfield == 3:
                    draw = True
                    break
        if not (player1 and player2 or draw):
            for j in range(3):
                values[i][j] += player1 - player2 + 1
            score += (player1 + player2) * 100
    for j in range(3):
        player1 = 0
        player2 = 0
        draw = False
        for i in range(3):
            if bigboard[i][j]:
                if bigboard[i][j] == 1:
                    player1 += 1
                elif bigboard[i][j] == -1:
                    player2 -= 1
                elif bigboard[i][j] == 3:
                    draw = True
                    break
        if not (player1 and player2 or draw):
            for i in range(3):
                values[i][j] += player1 - player2 + 1
            score += (player1 + player2) * 100
    player1 = 0
    player2 = 0
    draw = False
    for i in range(3):
        if bigboard[i][i]:
            if bigboard[i][i] == 1:
                player1 += 1
            elif bigboard[i][i] == -1:
                player2 -= 1
            elif bigboard[i][i] == 3:
                draw = True
                break
    if not (player1 and player2 or draw):
        for i in range(3):
            values[i][i] += player1 - player2 + 1
        score += (player1 + player2) * 100
    player1 = 0
    player2 = 0
    draw = False
    for i, j in [(0, 2), (1, 1), (2, 0)]:
        if bigboard[i][j]:
            if bigboard[i][j] == 1:
                player1 += 1
            elif bigboard[i][j] == -1:
                player2 -= 1
            elif bigboard[i][j] == 3:
                draw = True
                break
    if not (player1 and player2 or draw):
        for i, j in [(0, 2), (1, 1), (2, 0)]:
            values[i][j] += player1 - player2 + 1
        score += (player1 + player2) * 100

    for i in range(3):
        for j in range(3):
            if bigboard[i][j] == 0 or bigboard[i][j] == 2:
                value = values[i][j]
                miniboard = board[i][j]
                for column in miniboard:
                    player1 = 0
                    player2 = 0
                    for field in column:
                        if field == 1:
                            player1 += 1
                        elif field == -1:
                            player2 -= 1
                    if not (player1 and player2):
                        score += (player1 + player2) * value
                for l in range(3):
                    player1 = 0
                    player2 = 0
                    for k in range(3):
                        if miniboard[k][l] == 1:
                            player1 += 1
                        elif miniboard[k][l] == -1:
                            player2 -= 1
                    if not (player1 and player2):
                        score += (player1 + player2) * value
                player1 = 0
                player2 = 0
                for k in range(3):
                    if miniboard[k][k] == 1:
                        player1 += 1
                    elif miniboard[k][k] == -1:
                        player2 -= 1
                if not (player1 and player2):
                    score += (player1 + player2) * value
                player1 = 0
                player2 = 0
                for k, l in [(0, 2), (1, 1), (2, 0)]:
                    if miniboard[k][l] == 1:
                        player1 += 1
                    elif miniboard[k][l] == -1:
                        player2 -= 1
                if not (player1 and player2):
                    score += (player1 + player2) * value
    return score


def minimax(board, bigboard, player, alpha, beta, depth, allactive, gamevariant):
    nextallactive = False
    if depth == 0:
        return evaluate(board, bigboard)
    win = winner(bigboard)
    if win:
        if win == 3:
            return 0
        else:
            return win * 10000
    if player == 1:
        maxeval = -10001
        for i in range(3):
            for j in range(3):
                if bigboard[i][j] == 2:
                    for k in range(3):
                        for l in range(3):
                            if board[i][j][k][l] == 0:
                                board[i][j][k][l] = 1
                                oldbigboard = [row[:] for row in bigboard]
                                bigboard[i][j] = winner(board[i][j])
                                if allactive:
                                    for a in range(3):
                                        for b in range(3):
                                            if bigboard[a][b] == 2:
                                                bigboard[a][b] = 0
                                if bigboard[k][l] == 0:
                                    bigboard[k][l] = 2
                                elif gamevariant == 0 and bigboard[i][j] == 0:
                                    bigboard[i][j] = 2
                                else:
                                    nextallactive = True
                                    for a in range(3):
                                        for b in range(3):
                                            if bigboard[a][b] == 0:
                                                bigboard[a][b] = 2
                                eval = minimax(board, bigboard, -1, alpha, beta, depth - 1, nextallactive, gamevariant)
                                board[i][j][k][l] = 0
                                bigboard = oldbigboard
                                maxeval = max(eval, maxeval)
                                alpha = max(alpha, eval)
                                if beta <= alpha:
                                    return maxeval
                    if not allactive:
                        return maxeval
        return maxeval
    else:
        mineval = 10001
        for i in range(3):
            for j in range(3):
                if bigboard[i][j] == 2:
                    for k in range(3):
                        for l in range(3):
                            if board[i][j][k][l] == 0:
                                board[i][j][k][l] = -1
                                oldbigboard = [row[:] for row in bigboard]
                                bigboard[i][j] = winner(board[i][j])
                                if allactive:
                                    for a in range(3):
                                        for b in range(3):
                                            if bigboard[a][b] == 2:
                                                bigboard[a][b] = 0
                                if bigboard[k][l] == 0:
                                    bigboard[k][l] = 2
                                elif gamevariant == 0 and bigboard[i][j] == 0:
                                    bigboard[i][j] = 2
                                else:
                                    nextallactive = True
                                    for a in range(3):
                                        for b in range(3):
                                            if bigboard[a][b] == 0:
                                                bigboard[a][b] = 2
                                eval = minimax(board, bigboard, 1, alpha, beta, depth - 1, nextallactive, gamevariant)
                                board[i][j][k][l] = 0
                                bigboard = oldbigboard
                                mineval = min(eval, mineval)
                                beta = min(beta, eval)
                                if beta <= alpha:
                                    return mineval
                    if not allactive:
                        return mineval
        return mineval


def findmove(board, bigboard, player, depth, allactive, gamevariant):
    nextallactive = False
    if player == 1:
        maxeval = -10001
        bi, bj, bk, bl = 4, 4, 4, 4
        for i in range(3):
            for j in range(3):
                if bigboard[i][j] == 2:
                    for k in range(3):
                        for l in range(3):
                            if board[i][j][k][l] == 0:
                                board[i][j][k][l] = 1
                                oldbigboard = [row[:] for row in bigboard]
                                bigboard[i][j] = winner(board[i][j])
                                if allactive:
                                    for a in range(3):
                                        for b in range(3):
                                            if bigboard[a][b] == 2:
                                                bigboard[a][b] = 0
                                if bigboard[k][l] == 0:
                                    bigboard[k][l] = 2
                                elif gamevariant == 0 and bigboard[i][j] == 0:
                                    bigboard[i][j] = 2
                                else:
                                    nextallactive = True
                                    for a in range(3):
                                        for b in range(3):
                                            if bigboard[a][b] == 0:
                                                bigboard[a][b] = 2
                                eval = minimax(board, bigboard, -1, -10001, 10001, depth - 1, nextallactive, gamevariant)
                                board[i][j][k][l] = 0
                                bigboard = oldbigboard
                                if eval > maxeval:
                                    maxeval = eval
                                    bi, bj, bk, bl = i, j, k, l
                    if not allactive:
                        return bi, bj, bk, bl, bigboard
    else:
        mineval = 10001
        bi, bj, bk, bl = 4, 4, 4, 4
        for i in range(3):
            for j in range(3):
                if bigboard[i][j] == 2:
                    for k in range(3):
                        for l in range(3):
                            if board[i][j][k][l] == 0:
                                board[i][j][k][l] = -1
                                oldbigboard = [row[:] for row in bigboard]
                                bigboard[i][j] = winner(board[i][j])
                                if allactive:
                                    for a in range(3):
                                        for b in range(3):
                                            if bigboard[a][b] == 2:
                                                bigboard[a][b] = 0
                                if bigboard[k][l] == 0:
                                    bigboard[k][l] = 2
                                elif gamevariant == 0 and bigboard[i][j] == 0:
                                    bigboard[i][j] = 2
                                else:
                                    nextallactive = True
                                    for a in range(3):
                                        for b in range(3):
                                            if bigboard[a][b] == 0:
                                                bigboard[a][b] = 2
                                eval = minimax(board, bigboard, 1, -10001, 10001, depth - 1, nextallactive, gamevariant)
                                board[i][j][k][l] = 0
                                bigboard = oldbigboard
                                if eval < mineval:
                                    mineval = eval
                                    bi, bj, bk, bl = i, j, k, l
                    if not allactive:
                        return bi, bj, bk, bl, bigboard
    return bi, bj, bk, bl, bigboard


def Undo(board, bigboard, game_history, player, allactive, label, modus):
    if len(game_history) <= 1 or modus == 2 and len(game_history) <= 2:
        return board, bigboard, game_history, player, allactive, label
    i = game_history[-1][0]
    j = game_history[-1][1]
    k = game_history[-1][2]
    l = game_history[-1][3]
    allactive = game_history[-1][4]

    for a in range(3):
        for b in range(3):
            if bigboard[a][b] == 2:
                bigboard[a][b] = 0

    board[i][j][k][l] = 0
    bigboard[i][j] = 2
    if allactive:
        for a in range(3):
            for b in range(3):
                if bigboard[a][b] == 0:
                    bigboard[a][b] = 2

    if player == 1:
        player = -1
        label = myfont.render("It is O's turn", True, (0, 0, 0))
    else:
        player = 1
        label = myfont.render("It is X's turn", True, (0, 0, 0))
    game_history.pop()
    if (modus == 1 and player == -1) or (modus == 2 and player == 1):
        return Undo(board, bigboard, game_history, player, allactive, label, 0)
    return board, bigboard, game_history, player, allactive, label


def game(modus, depth, depth2, gamevariant, memory):
    undo_action = 0
    game_history = [(-1, -1, -1, -1, -1)]
    screen.fill((255, 255, 255))
    board = [[[[0 for i in range(3)] for j in range(3)] for k in range(3)] for l in range(3)]
    #0: no token, 1: X, -1: O, -10: no token, but O selects, 10: no token, but X selects
    bigboard = [[2 for i in range(3)] for j in range(3)]
    # -1, 1: player token, 2: active field, 3: draw, 4: selected and non-active, 5: selected and active
    show_tokens = [[1 for i in range(3)] for j in range(3)]
    #1: normal, 2: show but selected, 0: show not and unselected, -1: show not and selected, -3=0 3=1 but for changing mode (click problem)
    centerx = 350
    centery = 450
    player = 1
    allactive = True
    field = 600
    smallField = 54
    fps = 30
    coordinates = [[[[0 for i in range(3)] for j in range(3)] for k in range(3)] for l in range(3)]
    smallCenterx = [centerx - field / 3, centerx, centerx + field / 3]
    smallCentery = [centery - field / 3, centery, centery + field / 3]
    for i in range(3):
        for j in range(3):
            scx = [smallCenterx[i] - smallField, smallCenterx[i], smallCenterx[i] + smallField]
            scy = [smallCentery[j] - smallField, smallCentery[j], smallCentery[j] + smallField]
            for k in range(3):
                for l in range(3):
                    coordinates[i][j][k][l] = (scx[k], scy[l])

    if player == 1:
        label = myfont.render("It is X's turn", True, (0, 0, 0))
    else:
        label = myfont.render("It is O's turn", True, (0, 0, 0))
    pg.draw.rect(screen, (255, 255, 255), pg.Rect((700 - label.get_width()) / 2, 50, label.get_width(), label.get_height()))
    screen.blit(label, ((700 - label.get_width()) / 2, 50))
    back = myfont.render("< Menu", True, (0, 0, 0))
    screen.blit(back, (50, 50))
    undo = myfont.render("Undo", True, (0, 0, 0))
    if modus != 3:
        screen.blit(undo, (550, 50))

    end = False #0: no end, 1: X won, -1: O won, 3: draw, 2: dummy for getting back after game end
    first = True
    display(board, bigboard, show_tokens, memory, game_history[-1][0:2])
    time.sleep(0.5)
    while True:
        if end == 0 or end == 2:
            screen.blit(back, (50, 50))
            if modus != 3:
                screen.blit(undo, (550, 50))
            screen.blit(label, ((700 - label.get_width()) / 2, 50))
            display(board, bigboard, show_tokens, memory, game_history[-1][0:2])
        else:
            pg.display.update()
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
        mouseposition = pg.mouse.get_pos()
        mouse_presses = pg.mouse.get_pressed()
        for a in range(3):
            for b in range(3):
                if show_tokens[a][b] == -1:
                    show_tokens[a][b] = 0
                elif show_tokens[a][b] == 2:
                    show_tokens[a][b] = 1
        if end and end != 2:
            pg.draw.rect(screen, (255, 255, 255), pg.Rect(0, 0, 700, 100))
            if end == 1:
                label = myfont.render("X has won!", True, (0, 0, 0))
            elif end == -1:
                label = myfont.render("O has won!", True, (0, 0, 0))
            else:
                label = myfont.render("Draw!", True, (0, 0, 0))
            pg.draw.rect(screen, (220, 220, 220), pg.Rect(200, 300, 300, 300))
            pg.draw.rect(screen, (180, 180, 180), pg.Rect(250, 400, 200, 75))
            pg.draw.rect(screen, (180, 180, 180), pg.Rect(250, 500, 200, 75))
            new = myfont.render("New Game", True, (0, 0, 0))
            quit = myfont.render("Back to Game", True, (0, 0, 0))
            if 250 <= mouseposition[0] <= 450:
                if 400 <= mouseposition[1] <= 475:
                    pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
                    new = myfont.render("New Game", True, (255, 255, 255))
                    pg.draw.rect(screen, (100, 100, 100), pg.Rect(250, 400, 200, 75))
                    if mouse_presses[0]:
                        return 0
                elif 500 <= mouseposition[1] <= 575:
                    pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
                    quit = myfont.render("Back to Game", True, (255, 255, 255))
                    pg.draw.rect(screen, (100, 100, 100), pg.Rect(250, 500, 200, 75))
                    if mouse_presses[0]:
                        #pg.quit()
                        #sys.exit()
                        end = 2
                        if player == 1:
                            player = -1
                            label = myfont.render("It is O's turn", True, (0, 0, 0))
                        else:
                            player = 1
                            label = myfont.render("It is X's turn", True, (0, 0, 0))
                        continue
                else:
                    pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
            screen.blit(label, (200 + (300 - label.get_width()) / 2, 300 + (100 - label.get_height()) / 2))
            screen.blit(new, (250 + (200 - new.get_width()) / 2, 400 + (75 - new.get_height()) / 2))
            screen.blit(quit, (250 + (200 - quit.get_width()) / 2, 500 + (75 - quit.get_height()) / 2))
            continue
        if 50 <= mouseposition[0] <= 50 + back.get_width() and 50 <= mouseposition[1] <= 50 + back.get_height():
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
            back = myfont.render("< Menu", True, (255, 0, 0))
            hand = True
            if mouse_presses[0]:
                return 0
        else:
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
            hand = False
            back = myfont.render("< Menu", True, (0, 0, 0))

        if modus != 3:
            if 550 <= mouseposition[0] <= 550 + undo.get_width() and 50 <= mouseposition[1] <= 50 + undo.get_height():
                pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
                undo = myfont.render("Undo", True, (255, 0, 0))
                hand = True
                if mouse_presses[0] and undo_action == 0:
                    undo_action = 1
                    undo = myfont.render("Undo", True, (0, 0, 0))
                    continue
                elif undo_action == 1:
                    board, bigboard, game_history, player, allactive, label = Undo(board, bigboard, game_history,
                                                                                   player, allactive, label, modus)
                    undo_action = 2
                elif not mouse_presses[0]:
                    undo_action = 0
                    undo = myfont.render("Undo", True, (255, 0, 0))
            else:
                pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
                hand = False
                undo = myfont.render("Undo", True, (0, 0, 0))

        if end == 0 and ((modus == 1 and player == -1) or (modus == 2 and player == 1) or modus == 3):
            if (modus == 2 or modus == 3) and first:
                i, j, k, l = 1, 1, 1, 1
                first = False
            else:
                if modus == 3 and player == -1:
                    i, j, k, l, bigboard = findmove(board, bigboard, -1, depth2, allactive, gamevariant)
                else:
                    i, j, k, l, bigboard = findmove(board, bigboard, player, depth, allactive, gamevariant)
        else:
            x, y = get_coordinate(mouseposition)
            i, j, k, l = get_indicies(x, y, coordinates)
            clickable = checkClickable(board, bigboard, mouseposition, coordinates, hand, player) #0: no, 1: yes, small field, 2: yes, big field
            #display(board, bigboard, show_tokens)
            if  clickable == 0:
                FramePerSec.tick(fps)
                screen.fill((255, 255, 255))
                continue
            elif clickable == 2:
                if mouse_presses[0]:
                    if show_tokens[i][j] == 1 or show_tokens[i][j] == 2:
                        show_tokens[i][j] = -3
                    elif show_tokens[i][j] == 0 or show_tokens[i][j] == -1:
                        show_tokens[i][j] = 3
                else:
                    if show_tokens[i][j] == 1:
                        show_tokens[i][j] = 2
                    elif show_tokens[i][j] == 0:
                        show_tokens[i][j] = -1
                    elif show_tokens[i][j] == 3:
                        show_tokens[i][j]  = 2
                    elif show_tokens[i][j] == -3:
                        show_tokens[i][j] = -1
                screen.fill((255, 255, 255))
                continue
            elif not mouse_presses[0] or (i, j, k, l) == game_history[-1][:4]:
                FramePerSec.tick(fps)
                screen.fill((255, 255, 255))
                continue
        board[i][j][k][l] = player
        if allactive:
            game_history.append((i, j, k, l, 1))
        else:
            game_history.append((i, j, k, l, 0))
        win = winner(board[i][j])
        bigboard[i][j] = win
        if modus == 0 or (modus == 1 and player == 1) or (modus == 2 and player == -1):
            show_tokens[i][j] = 3

        end = 0
        if win:
            end = winner(bigboard)
            if end:
                for a in range(3):
                    for b in range(3):
                        if bigboard[a][b] == 2:
                            bigboard[a][b] = 0
                display(board, bigboard, show_tokens, memory, game_history[-1][0:2])
                continue
        if allactive:
            allactive = False
            for a in range(3):
                for b in range(3):
                    if bigboard[a][b] == 2:
                        bigboard[a][b] = 0
        if bigboard[k][l] == 0 or bigboard[k][l] == 4 or bigboard[k][l] == 5:
            bigboard[k][l] = 2
        elif gamevariant == 0 and bigboard[i][j] == 0:
            bigboard[i][j] = 2
        else:
            allactive = True
            for a in range(3):
                for b in range(3):
                    if bigboard[a][b] == 0 or bigboard[a][b] == 4:
                        bigboard[a][b] = 2
        #li, lj, lk, ll = i, j, k, l
        if player == 1:
            player = -1
            label = myfont.render("It is O's turn", True, (0, 0, 0))
        else:
            player = 1
            label = myfont.render("It is X's turn", True, (0, 0, 0))
        screen.fill((255, 255, 255))
        FramePerSec.tick(fps)


def menu_gamevariant():
    screen.fill((255, 255, 255))
    pg.draw.rect(screen, (180, 180, 180), pg.Rect(150, 150, 400, 100))
    pg.draw.rect(screen, (180, 180, 180), pg.Rect(150, 300, 400, 100))
    title = myfont.render("Select game variant", True, (0, 0, 0))
    modus0 = myfont.render("Remain in square", True, (0, 0, 0))
    modus1 = myfont.render("Free choice", True, (0, 0, 0))
    screen.blit(title, ((700 - title.get_width()) / 2, 50))
    screen.blit(modus0, (150 + (400 - modus0.get_width()) / 2, 150 + (100 - modus0.get_height()) / 2))
    screen.blit(modus1, (150 + (400 - modus1.get_width()) / 2, 300 + (100 - modus1.get_height()) / 2))
    pg.display.update()
    time.sleep(0.5)
    while True:
        screen.fill((255, 255, 255))
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
        pg.draw.rect(screen, (180, 180, 180), pg.Rect(150, 150, 400, 100))
        pg.draw.rect(screen, (180, 180, 180), pg.Rect(150, 300, 400, 100))
        title = myfont.render("Select game variant", True, (0, 0, 0))
        modus0 = myfont.render("Remain in square", True, (0, 0, 0))
        modus1 = myfont.render("Free choice", True, (0, 0, 0))
        mouse_presses = pg.mouse.get_pressed()
        mouseposition = pg.mouse.get_pos()
        if 150 <= mouseposition[0] <= 550:
            if 150 <= mouseposition[1] <= 250:
                pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
                pg.draw.rect(screen, (100, 100, 100), pg.Rect(150, 150, 400, 100))
                modus0 = myfont.render("Remain in square", True, (255, 255, 255))
                if mouse_presses[0]:
                    return 0
            elif 300 <= mouseposition[1] <= 400:
                pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
                pg.draw.rect(screen, (100, 100, 100), pg.Rect(150, 300, 400, 100))
                modus1 = myfont.render("Free choice", True, (255, 255, 255))
                if mouse_presses[0]:
                    return 1
            else:
                pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
        else:
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
        screen.blit(title, ((700 - title.get_width()) / 2, 50))
        screen.blit(modus0, (150 + (400 - modus0.get_width()) / 2, 150 + (100 - modus0.get_height()) / 2))
        screen.blit(modus1, (150 + (400 - modus1.get_width()) / 2, 300 + (100 - modus1.get_height()) / 2))
        pg.display.update()


def menu_memory():
    screen.fill((255, 255, 255))
    pg.draw.rect(screen, (180, 180, 180), pg.Rect(150, 150, 400, 100))
    pg.draw.rect(screen, (180, 180, 180), pg.Rect(150, 300, 400, 100))
    title = myfont.render("Select if you are insane", True, (0, 0, 0))
    modus0 = myfont.render("Normal mode", True, (0, 0, 0))
    modus1 = myfont.render("Memory", True, (0, 0, 0))
    screen.blit(title, ((700 - title.get_width()) / 2, 50))
    screen.blit(modus0, (150 + (400 - modus0.get_width()) / 2, 150 + (100 - modus0.get_height()) / 2))
    screen.blit(modus1, (150 + (400 - modus1.get_width()) / 2, 300 + (100 - modus1.get_height()) / 2))
    pg.display.update()
    time.sleep(0.5)
    while True:
        screen.fill((255, 255, 255))
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
        pg.draw.rect(screen, (180, 180, 180), pg.Rect(150, 150, 400, 100))
        pg.draw.rect(screen, (180, 180, 180), pg.Rect(150, 300, 400, 100))
        title = myfont.render("Select if you are insane", True, (0, 0, 0))
        modus0 = myfont.render("Normal mode", True, (0, 0, 0))
        modus1 = myfont.render("Memory", True, (0, 0, 0))
        mouse_presses = pg.mouse.get_pressed()
        mouseposition = pg.mouse.get_pos()
        if 150 <= mouseposition[0] <= 550:
            if 150 <= mouseposition[1] <= 250:
                pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
                pg.draw.rect(screen, (100, 100, 100), pg.Rect(150, 150, 400, 100))
                modus0 = myfont.render("Normal mode", True, (255, 255, 255))
                if mouse_presses[0]:
                    return 0
            elif 300 <= mouseposition[1] <= 400:
                pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
                pg.draw.rect(screen, (100, 100, 100), pg.Rect(150, 300, 400, 100))
                modus1 = myfont.render("Memory", True, (255, 255, 255))
                if mouse_presses[0]:
                    return 1
            else:
                pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
        else:
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
        screen.blit(title, ((700 - title.get_width()) / 2, 50))
        screen.blit(modus0, (150 + (400 - modus0.get_width()) / 2, 150 + (100 - modus0.get_height()) / 2))
        screen.blit(modus1, (150 + (400 - modus1.get_width()) / 2, 300 + (100 - modus1.get_height()) / 2))
        pg.display.update()


def menu():
    screen.fill((255, 255, 255))
    pg.draw.rect(screen, (180, 180, 180), pg.Rect(150, 150, 400, 100))
    pg.draw.rect(screen, (180, 180, 180), pg.Rect(150, 300, 400, 100))
    pg.draw.rect(screen, (180, 180, 180), pg.Rect(150, 450, 400, 100))
    pg.draw.rect(screen, (180, 180, 180), pg.Rect(150, 600, 400, 100))
    title = myfont.render("Select modus", True, (0, 0, 0))
    back = myfont.render("< Menu", True, (0, 0, 0))
    modus0 = myfont.render("Player vs. Player", True, (0, 0, 0))
    modus1 = myfont.render("Player vs. Computer", True, (0, 0, 0))
    modus2 = myfont.render("Computer vs. Player", True, (0, 0, 0))
    modus3 = myfont.render("Computer vs. Computer", True, (0, 0, 0))
    screen.blit(title, ((700 - title.get_width()) / 2, 50))
    screen.blit(back, (50, 50))
    screen.blit(modus0, (150 + (400 - modus0.get_width()) / 2, 150 + (100 - modus0.get_height()) / 2))
    screen.blit(modus1, (150 + (400 - modus1.get_width()) / 2, 300 + (100 - modus1.get_height()) / 2))
    screen.blit(modus2, (150 + (400 - modus2.get_width()) / 2, 450 + (100 - modus2.get_height()) / 2))
    screen.blit(modus3, (150 + (400 - modus3.get_width()) / 2, 600 + (100 - modus3.get_height()) / 2))
    pg.display.update()
    time.sleep(0.5)
    while True:
        screen.fill((255, 255, 255))
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
        pg.draw.rect(screen, (180, 180, 180), pg.Rect(150, 150, 400, 100))
        pg.draw.rect(screen, (180, 180, 180), pg.Rect(150, 300, 400, 100))
        pg.draw.rect(screen, (180, 180, 180), pg.Rect(150, 450, 400, 100))
        pg.draw.rect(screen, (180, 180, 180), pg.Rect(150, 600, 400, 100))
        title = myfont.render("Select modus", True, (0, 0, 0))
        back = myfont.render("< Menu", True, (0, 0, 0))
        modus0 = myfont.render("Player vs. Player", True, (0, 0, 0))
        modus1 = myfont.render("Player vs. Computer", True, (0, 0, 0))
        modus2 = myfont.render("Computer vs. Player", True, (0, 0, 0))
        modus3 = myfont.render("Computer vs. Computer", True, (0, 0, 0))
        mouse_presses = pg.mouse.get_pressed()
        mouseposition = pg.mouse.get_pos()
        if 50 <= mouseposition[0] <= 50 + back.get_width() and 50 <= mouseposition[1] <= 50 + back.get_height():
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
            back = myfont.render("< Menu", True, (255, 0, 0))
            if mouse_presses[0]:
                return -1
        elif 150 <= mouseposition[0] <= 550:
            if 150 <= mouseposition[1] <= 250:
                pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
                pg.draw.rect(screen, (100, 100, 100), pg.Rect(150, 150, 400, 100))
                modus0 = myfont.render("Player vs. Player", True, (255, 255, 255))
                if mouse_presses[0]:
                    return 0
            elif 300 <= mouseposition[1] <= 400:
                pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
                pg.draw.rect(screen, (100, 100, 100), pg.Rect(150, 300, 400, 100))
                modus1 = myfont.render("Player vs. Computer", True, (255, 255, 255))
                if mouse_presses[0]:
                    return 1
            elif 450 <= mouseposition[1] <= 550:
                pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
                pg.draw.rect(screen, (100, 100, 100), pg.Rect(150, 450, 400, 100))
                modus2 = myfont.render("Computer vs. Player", True, (255, 255, 255))
                if mouse_presses[0]:
                    return 2
            elif 600 <= mouseposition[1] <= 700:
                pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
                pg.draw.rect(screen, (100, 100, 100), pg.Rect(150, 600, 400, 100))
                modus3 = myfont.render("Computer vs. Computer", True, (255, 255, 255))
                if mouse_presses[0]:
                    return 3
            else:
                pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
        else:
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
        screen.blit(title, ((700 - title.get_width()) / 2, 50))
        screen.blit(back, (50, 50))
        screen.blit(modus0, (150 + (400 - modus0.get_width()) / 2, 150 + (100 - modus0.get_height()) / 2))
        screen.blit(modus1, (150 + (400 - modus1.get_width()) / 2, 300 + (100 - modus1.get_height()) / 2))
        screen.blit(modus2, (150 + (400 - modus2.get_width()) / 2, 450 + (100 - modus2.get_height()) / 2))
        screen.blit(modus3, (150 + (400 - modus3.get_width()) / 2, 600 + (100 - modus3.get_height()) / 2))
        pg.display.update()


def menu2(computer):
    screen.fill((255, 255, 255))
    pg.draw.rect(screen, (180, 180, 180), pg.Rect(150, 150, 175, 100))
    pg.draw.rect(screen, (180, 180, 180), pg.Rect(150, 300, 175, 100))
    pg.draw.rect(screen, (180, 180, 180), pg.Rect(150, 450, 175, 100))
    pg.draw.rect(screen, (180, 180, 180), pg.Rect(150, 600, 175, 100))
    pg.draw.rect(screen, (180, 180, 180), pg.Rect(375, 150, 175, 100))
    pg.draw.rect(screen, (180, 180, 180), pg.Rect(375, 300, 175, 100))
    pg.draw.rect(screen, (180, 180, 180), pg.Rect(375, 450, 175, 100))
    pg.draw.rect(screen, (180, 180, 180), pg.Rect(375, 600, 175, 100))
    if computer == 0:
        title = myfont.render("Select difficulty", True, (0, 0, 0))
    elif computer == 1:
        title = myfont.render("Select difficulty 1", True, (0, 0, 0))
    else:
        title = myfont.render("Select difficulty 2", True, (0, 0, 0))
    back = myfont.render("< Menu", True, (0, 0, 0))
    level1 = myfont.render("Super easy", True, (0, 0, 0))
    level2 = myfont.render("Easy", True, (0, 0, 0))
    level3 = myfont.render("Medium", True, (0, 0, 0))
    level4 = myfont.render("Advanced", True, (0, 0, 0))
    level5 = myfont.render("Hard", True, (0, 0, 0))
    level6 = myfont.render("Super hard", True, (0, 0, 0))
    level7 = myfont.render("Extreme", True, (0, 0, 0))
    level8 = myfont.render("Japanese", True, (0, 0, 0))
    screen.blit(title, ((700 - title.get_width()) / 2, 50))
    screen.blit(back, (50, 50))
    screen.blit(level1, (150 + (175 - level1.get_width()) / 2, 150 + (100 - level1.get_height()) / 2))
    screen.blit(level3, (150 + (175 - level3.get_width()) / 2, 300 + (100 - level3.get_height()) / 2))
    screen.blit(level5, (150 + (175 - level5.get_width()) / 2, 450 + (100 - level5.get_height()) / 2))
    screen.blit(level7, (150 + (175 - level7.get_width()) / 2, 600 + (100 - level7.get_height()) / 2))
    screen.blit(level2, (375 + (175 - level2.get_width()) / 2, 150 + (100 - level2.get_height()) / 2))
    screen.blit(level4, (375 + (175 - level4.get_width()) / 2, 300 + (100 - level4.get_height()) / 2))
    screen.blit(level6, (375 + (175 - level6.get_width()) / 2, 450 + (100 - level6.get_height()) / 2))
    screen.blit(level8, (375 + (175 - level8.get_width()) / 2, 600 + (100 - level8.get_height()) / 2))
    pg.display.update()
    time.sleep(0.5)
    while True:
        screen.fill((255, 255, 255))
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
        pg.draw.rect(screen, (180, 180, 180), pg.Rect(150, 150, 175, 100))
        pg.draw.rect(screen, (180, 180, 180), pg.Rect(150, 300, 175, 100))
        pg.draw.rect(screen, (180, 180, 180), pg.Rect(150, 450, 175, 100))
        pg.draw.rect(screen, (180, 180, 180), pg.Rect(150, 600, 175, 100))
        pg.draw.rect(screen, (180, 180, 180), pg.Rect(375, 150, 175, 100))
        pg.draw.rect(screen, (180, 180, 180), pg.Rect(375, 300, 175, 100))
        pg.draw.rect(screen, (180, 180, 180), pg.Rect(375, 450, 175, 100))
        pg.draw.rect(screen, (180, 180, 180), pg.Rect(375, 600, 175, 100))
        if computer == 0:
            title = myfont.render("Select difficulty", True, (0, 0, 0))
        elif computer == 1:
            title = myfont.render("Select difficulty 1", True, (0, 0, 0))
        elif computer == 1:
            title = myfont.render("Select difficulty 2", True, (0, 0, 0))
        back = myfont.render("< Menu", True, (0, 0, 0))
        level1 = myfont.render("Super easy", True, (0, 0, 0))
        level2 = myfont.render("Easy", True, (0, 0, 0))
        level3 = myfont.render("Medium", True, (0, 0, 0))
        level4 = myfont.render("Advanced", True, (0, 0, 0))
        level5 = myfont.render("Hard", True, (0, 0, 0))
        level6 = myfont.render("Super hard", True, (0, 0, 0))
        level7 = myfont.render("Extreme", True, (0, 0, 0))
        level8 = myfont.render("Japanese", True, (0, 0, 0))
        mouse_presses = pg.mouse.get_pressed()
        mouseposition = pg.mouse.get_pos()
        if 50 <= mouseposition[0] <= 50 + back.get_width() and 50 <= mouseposition[1] <= 50 + back.get_height():
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
            back = myfont.render("< Menu", True, (255, 0, 0))
            if mouse_presses[0]:
                return 0
        elif 150 <= mouseposition[0] <= 325:
            if 150 <= mouseposition[1] <= 250:
                pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
                pg.draw.rect(screen, (100, 100, 100), pg.Rect(150, 150, 175, 100))
                level1 = myfont.render("Super easy", True, (255, 255, 255))
                if mouse_presses[0]:
                    return 1
            elif 300 <= mouseposition[1] <= 400:
                pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
                pg.draw.rect(screen, (100, 100, 100), pg.Rect(150, 300, 175, 100))
                level3 = myfont.render("Medium", True, (255, 255, 255))
                if mouse_presses[0]:
                    return 3
            elif 450 <= mouseposition[1] <= 550:
                pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
                pg.draw.rect(screen, (100, 100, 100), pg.Rect(150, 450, 175, 100))
                level5 = myfont.render("Hard", True, (255, 255, 255))
                if mouse_presses[0]:
                    return 5
            elif 600 <= mouseposition[1] <= 700:
                pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
                pg.draw.rect(screen, (100, 100, 100), pg.Rect(150, 600, 175, 100))
                level7 = myfont.render("Extreme", True, (255, 255, 255))
                if mouse_presses[0]:
                    return 7
            else:
                pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
        elif 375 <= mouseposition[0] <= 550:
            if 150 <= mouseposition[1] <= 250:
                pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
                pg.draw.rect(screen, (100, 100, 100), pg.Rect(375, 150, 175, 100))
                level2 = myfont.render("Easy", True, (255, 255, 255))
                if mouse_presses[0]:
                    return 2
            elif 300 <= mouseposition[1] <= 400:
                pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
                pg.draw.rect(screen, (100, 100, 100), pg.Rect(375, 300, 175, 100))
                level4 = myfont.render("Advanced", True, (255, 255, 255))
                if mouse_presses[0]:
                    return 4
            elif 450 <= mouseposition[1] <= 550:
                pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
                pg.draw.rect(screen, (100, 100, 100), pg.Rect(375, 450, 175, 100))
                level6 = myfont.render("Super hard", True, (255, 255, 255))
                if mouse_presses[0]:
                    return 6
            elif 600 <= mouseposition[1] <= 700:
                pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
                pg.draw.rect(screen, (100, 100, 100), pg.Rect(375, 600, 175, 100))
                level8 = myfont.render("Japanese", True, (255, 255, 255))
                if mouse_presses[0]:
                    return 8
            else:
                pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
        else:
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
        screen.blit(title, ((700 - title.get_width()) / 2, 50))
        screen.blit(back, (50, 50))
        screen.blit(level1, (150 + (175 - level1.get_width()) / 2, 150 + (100 - level1.get_height()) / 2))
        screen.blit(level3, (150 + (175 - level3.get_width()) / 2, 300 + (100 - level3.get_height()) / 2))
        screen.blit(level5, (150 + (175 - level5.get_width()) / 2, 450 + (100 - level5.get_height()) / 2))
        screen.blit(level7, (150 + (175 - level7.get_width()) / 2, 600 + (100 - level7.get_height()) / 2))
        screen.blit(level2, (375 + (175 - level2.get_width()) / 2, 150 + (100 - level2.get_height()) / 2))
        screen.blit(level4, (375 + (175 - level4.get_width()) / 2, 300 + (100 - level4.get_height()) / 2))
        screen.blit(level6, (375 + (175 - level6.get_width()) / 2, 450 + (100 - level6.get_height()) / 2))
        screen.blit(level8, (375 + (175 - level8.get_width()) / 2, 600 + (100 - level8.get_height()) / 2))
        pg.display.update()


pg.init()
screen = pg.display.set_mode((700, 800))
FramePerSec = pg.time.Clock()
pg.display.set_caption("Tic Tac Toe")
myfont = pg.font.SysFont("Comic Sans MS", 30)

while True:
    gamevariant = menu_gamevariant()
    modus = menu()
    if modus == -1:
        continue
    memory = 0
    if modus != 3:
        memory = menu_memory()
        if memory == -1:
            continue
    depth = 0
    depth2 = 0
    if modus:
        if modus == 3:
            depth = menu2(1)
            if depth == 0:
                continue
            depth2 = menu2(2)
            if depth2 == 0:
                continue
        else:
            depth = menu2(0)
            if depth == 0:
                continue
    game(modus, depth, depth2, gamevariant, memory)