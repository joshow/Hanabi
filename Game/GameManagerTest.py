from Game.GameElements import Hint as Hint
from Game.GameElements import Card as Card
from Game.GameElements import Action as Action
from Game.GameElements import PlayerDeck as PlayerDeck
from Game.GameManager import GameManager as GameManager
import random


def initRandomCards():
    colors = ["R", "G", "B", "W", "Y"]
    counts = [3, 2, 2, 2, 1]
    cards = []

    for color in colors:
        for i in range(5):
            for j in range(counts[i]):
                cards.append(Card(color, i + 1))

    random.shuffle(cards)
    return cards


def initCards(number=0):
    if number is 1:
        return [Card("Y", 3), Card("R", 4), Card("G", 1), Card("R", 5), Card("G", 1), Card("W", 4), Card("W", 4), Card("Y", 4), Card("W", 3), Card("W", 1), Card("R", 4), Card("Y", 1), Card("G", 1), Card("B", 4), Card("B", 5), Card("R", 3), Card("Y", 4), Card("B", 4), Card("W", 2), Card("W", 1), Card("B", 3), Card("B", 3), Card("B", 1), Card("R", 2), Card("Y", 3), Card("R", 2), Card("G", 3), Card("B", 1), Card("R", 3), Card("Y", 1), Card("W", 3), Card("G", 4), Card("Y", 2), Card("B", 2), Card("R", 1), Card("G", 3), Card("W", 2), Card("R", 1), Card("Y", 5), Card("G", 4), Card("R", 1), Card("B", 1), Card("Y", 1), Card("G", 2), Card("G", 2), Card("W", 5), Card("G", 5), Card("Y", 2), Card("B", 2), Card("W", 1)]
    if number is 2:
        return [Card("R", 5), Card("G", 4), Card("B", 3), Card("B", 5), Card("G", 1), Card("B", 1), Card("W", 4), Card("W", 1), Card("Y", 2), Card("G", 1), Card("G", 2), Card("W", 5), Card("R", 3), Card("Y", 1), Card("G", 2), Card("Y", 4), Card("W", 1), Card("B", 2), Card("W", 2), Card("W", 1), Card("B", 1), Card("Y", 4), Card("R", 2), Card("B", 3), Card("G", 3), Card("R", 1), Card("Y", 3), Card("W", 3), Card("R", 3), Card("B", 4), Card("R", 1), Card("Y", 1), Card("G", 4), Card("B", 1), Card("G", 3), Card("G", 5), Card("B", 2), Card("Y", 5), Card("G", 1), Card("W", 2), Card("R", 1), Card("B", 4), Card("R", 2), Card("Y", 1), Card("W", 4), Card("Y", 3), Card("Y", 2), Card("R", 4), Card("W", 3), Card("R", 4)]
    if number is 3:
        return [Card("W", 4), Card("Y", 4), Card("W", 3), Card("Y", 5), Card("G", 1), Card("B", 1), Card("Y", 2), Card("Y", 3), Card("B", 3), Card("R", 4), Card("B", 1), Card("W", 1), Card("B", 3), Card("W", 2), Card("B", 5), Card("B", 4), Card("R", 2), Card("R", 4), Card("G", 1), Card("R", 1), Card("W", 1), Card("R", 5), Card("Y", 3), Card("Y", 4), Card("W", 3), Card("R", 1), Card("R", 1), Card("R", 3), Card("G", 2), Card("W", 2), Card("G", 2), Card("G", 3), Card("R", 2), Card("Y", 1), Card("Y", 1), Card("B", 1), Card("Y", 1), Card("Y", 2), Card("B", 2), Card("W", 4), Card("B", 2), Card("W", 5), Card("G", 3), Card("R", 3), Card("G", 5), Card("B", 4), Card("G", 4), Card("G", 1), Card("G", 4), Card("W", 1)]
    if number is 4:
        return [Card("G", 3), Card("Y", 2), Card("B", 3), Card("R", 4), Card("R", 3), Card("G", 2), Card("R", 3), Card("W", 5), Card("W", 1), Card("Y", 3), Card("B", 3), Card("G", 2), Card("Y", 1), Card("W", 1), Card("R", 1), Card("G", 4), Card("R", 1), Card("W", 3), Card("Y", 4), Card("B", 4), Card("W", 4), Card("W", 4), Card("G", 1), Card("Y", 1), Card("B", 2), Card("G", 3), Card("W", 2), Card("W", 2), Card("B", 1), Card("Y", 5), Card("R", 2), Card("R", 2), Card("W", 1), Card("B", 1), Card("R", 1), Card("Y", 3), Card("G", 5), Card("R", 5), Card("Y", 4), Card("G", 1), Card("B", 1), Card("B", 4), Card("W", 3), Card("G", 4), Card("Y", 1), Card("R", 4), Card("Y", 2), Card("B", 5), Card("G", 1), Card("B", 2)]
    if number is 5:
        return [Card("R", 1), Card("B", 2), Card("R", 3), Card("R", 2), Card("R", 4), Card("R", 4), Card("G", 3), Card("W", 5), Card("Y", 3), Card("B", 3), Card("B", 3), Card("B", 1), Card("G", 3), Card("R", 2), Card("R", 1), Card("B", 5), Card("Y", 1), Card("Y", 2), Card("B", 4), Card("G", 5), Card("G", 1), Card("G", 1), Card("G", 4), Card("W", 1), Card("W", 2), Card("W", 1), Card("G", 2), Card("R", 1), Card("R", 3), Card("R", 5), Card("B", 1), Card("W", 3), Card("Y", 2), Card("W", 2), Card("G", 4), Card("W", 4), Card("Y", 1), Card("B", 2), Card("G", 1), Card("W", 3), Card("Y", 1), Card("Y", 3), Card("G", 2), Card("Y", 4), Card("B", 1), Card("W", 4), Card("W", 1), Card("B", 4), Card("Y", 4), Card("Y", 5)]
    return initRandomCards()


def printBoard(gameManager: GameManager):
    print()
    print("======================================================================")

    print("Hint Token: %d      Life Token: %d" % (gameManager.getHintToken(), gameManager.getLifeToken()))
    print("                                 Played              Discarded")

    playedCards = gameManager.getPlayedCards("R")
    discardedCards = gameManager.getDiscardedCards("R")
    print(" No         %2s|%2s|%2s|%2s          %-20s%s" % (0, 1, 2, 3, playedCards, discardedCards))

    colors = ["G", "B", "W", "Y"]
    for i in range(gameManager.getPlayerCount()):
        marker = " "
        if i is gameManager.getCurrentPlayerIndex():
            marker = ">"

        playerDeckString = str(gameManager.getPlayerDeck(i))
        playedCards = gameManager.getPlayedCards(colors[i])
        discardedCards = gameManager.getDiscardedCards(colors[i])

        print("%sPlayer %d - %s          %-20s%s" % (marker, i, playerDeckString, playedCards, discardedCards))
    print()


def nextTurn(gameManager: GameManager):
    gameManager.nextTurn()
    printBoard(gameManager)


def testGame1():
    gm = GameManager(initCards(5), 0, 2)
    gm.distributeCards()
    printBoard(gm)
    gm.doAction(Action(3, Hint(1), 3))

    nextTurn(gm)
    gm.doAction(Action(1, 2))

    nextTurn(gm)
    gm.doAction(Action(1, 3))

    nextTurn(gm)
    gm.doAction(Action(3, Hint(1), 2))

    nextTurn(gm)
    gm.doAction(Action(3, Hint(5), 3))

    nextTurn(gm)
    gm.doAction(Action(3, Hint("B"), 1))

    nextTurn(gm)
    gm.doAction(Action(3, Hint(2), 1))

    nextTurn(gm)
    gm.doAction(Action(1, 0))

    nextTurn(gm)
    gm.doAction(Action(1, 3))

    nextTurn(gm)
    gm.doAction(Action(2, 0))

    nextTurn(gm)
    gm.doAction(Action(2, 0))

    nextTurn(gm)
    gm.doAction(Action(3, Hint(1), 3))

    nextTurn(gm)
    gm.doAction(Action(3, Hint(2), 1))

    nextTurn(gm)
    gm.doAction(Action(1, 2))

    nextTurn(gm)
    gm.doAction(Action(1, 1))

    nextTurn(gm)
    gm.doAction(Action(1, 3))

    nextTurn(gm)
    gm.doAction(Action(2, 1))

    nextTurn(gm)
    gm.doAction(Action(1, 0))

    nextTurn(gm)
    gm.doAction(Action(1, 0))


testGame1()