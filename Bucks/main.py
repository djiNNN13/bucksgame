import time
import game_bucks

game = game_bucks.Bucks()
game.AddPlayer("Игрок 1")
game.AddPlayer("Игрок 2")
game.AddPlayer("Игрок 3")
game.Start()

while game.isPlaying:
    time.sleep(1)