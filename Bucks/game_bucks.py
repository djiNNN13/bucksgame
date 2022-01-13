import render
import random
import time

class Bucks:
    def __init__(self):
        self.players = []
        self.rounds = 0
        self.isPlaying = False
        self.ActivePlayer = -1
        self.bucks = 0
        self.Ids = 0
        self.Render = render.Render()
        while self.Render.isRunning == False:
            time.sleep(1)

    def WaitPushButton(self):
        self.Render.isWaitButton = True
        while(self.Render.isWaitButton):
            time.sleep(1)

    def UpdateScore(self):
        string = ""
        for i, v in enumerate(self.players):
            if(self.players[i][i]["bucks"] == 15):
                string += self.players[i][i]["name"]+" - выиграл!\n"
            else:
                string += self.players[i][i]["name"]+" - "+str(self.players[i][i]["bucks"])+" баксов\n"
        self.Render.StringScores = string

    def ShowCube(self, Cube, Nominal):
        if(Cube == "t"):
            self.Render.CubeTop.ChangeSprite("cube_"+str(Nominal)+".png")
            self.Render.CubeTop.Show(True)
            return
        if(Cube == "l"):
            self.Render.CubeLeft.ChangeSprite("cube_"+str(Nominal)+".png")
            self.Render.CubeLeft.Show(True)
            return
        if(Cube == "r"):
            self.Render.CubeRight.ChangeSprite("cube_"+str(Nominal)+".png")
            self.Render.CubeRight.Show(True)
            return

    def HideBoard(self):
        self.Render.CubeTop.Show(False)
        self.Render.CubeLeft.Show(False)
        self.Render.CubeRight.Show(False)

    def AddPlayer(self, name):
        self.players.append({self.Ids: {"name":name,"score":0, "bucks":0, "isStarted":False}})
        self.Ids += 1

    def Start(self):
        self.UpdateScore()
        for i, v in enumerate(self.players):
            self.Render.StringWhoPushing = "Начало игры. Бросает - " + self.players[i][i]["name"]
            self.WaitPushButton()
            self.players[i][i]["score"] = random.randint(1,6)
            self.ShowCube("t", self.players[i][i]["score"])
        IdMax = 0
        Max = 0
        for i, v in enumerate(self.players):
            if(self.players[i][i]["score"] > Max):
                Max = self.players[i][i]["score"]
                IdMax = i
        self.players[IdMax][IdMax]["isStarted"] = True
        self.ActivePlayer = IdMax
        IdMin = 0
        Min = 228
        for i, v in enumerate(self.players):
            if(self.players[i][i]["score"] < Min):
                Min = self.players[i][i]["score"]
                IdMin = i
        self.Render.StringWhoPushing = "Игрок " + self.players[i][i]["name"] + " кидает номинал бакса"
        self.bucks = random.randint(1,6)
        self.WaitPushButton()
        self.ShowCube("t", self.bucks)

        self.Render.NominalBucks = "Номинал бакса - " + str(self.bucks)
        self.rounds = 1
        self.isPlaying = True
        self.HideBoard()
        time.sleep(2)
        self.StartRound()

    def CheckLooser(self):
        LooserPlayer = -1
        for i, v in enumerate(self.players):
            if(self.players[i][i]["bucks"] != 15):
                if(LooserPlayer == -1):
                    LooserPlayer = i
                else:
                    return
        self.isPlaying = False
        self.Render.isRunning = False

    def StepRoundPlayer(self, player):
        started = self.players[player][player]["bucks"]
        steps = [random.randint(1,6), random.randint(1,6), random.randint(1,6)]
        self.WaitPushButton()
        self.ShowCube("t", steps[0])
        self.WaitPushButton()
        self.ShowCube("l", steps[1])
        self.WaitPushButton()
        self.ShowCube("r", steps[2])
        for i in steps:
            if(i == self.bucks):
                self.players[player][player]["bucks"] += 1
        if(steps[0] == steps[1] == steps[2]):
            self.players[player][player]["bucks"] += 5
        if((steps[0] == self.bucks) and (steps[1] == self.bucks) and (steps[2] == self.bucks)):
            self.players[player][player]["bucks"] = 15
        if(self.players[player][player]["bucks"] > 15):
            self.players[player][player]["bucks"] = started
        time.sleep(1.5)
        self.HideBoard()
        self.UpdateScore()
        

    def StartRound(self):
        self.Render.StringWhoPushing = "Сейчас ходит - "+self.players[self.ActivePlayer][self.ActivePlayer]["name"]
        self.StepRoundPlayer(self.ActivePlayer)
        
        for i, v in enumerate(self.players):
            if(i == self.ActivePlayer):
                continue
            self.Render.StringWhoPushing = "Сейчас ходит - "+self.players[i][i]["name"]
            self.StepRoundPlayer(i)
        self.NextStep()

    def NextStep(self):
        for i, v in enumerate(self.players):
            if(self.players[i][i]["bucks"] == 15):
                continue
            self.Render.StringWhoPushing = "Сейчас ходит - "+self.players[i][i]["name"]
            self.StepRoundPlayer(i)
        self.CheckLooser()
        self.NextStep()