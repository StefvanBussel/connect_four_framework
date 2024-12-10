from appJar.appjar import *
from connect_four_board import connect_four_board as cf_board
from connect_four_move import connect_four_move
from connect_four_player import connect_four_player
from LuizaStefAI import connect_four_player as cf_player


vari = cf_player.get_move(cf_player, board= cf_board)
print(vari)

'''def kleur():
  kleur = "rood"#app.addLabelEntry("Welke kleur kies je? (rood/groen/roze)", 2, 0 ,7) 
  if kleur == "rood":
    kleur == "R"
  elif kleur == "groen":
    kleur == "G"
  else:
    kleur == "P"
  return kleur

def beginSpel():
  for x in range (1, 7) : 
    for i in range (0, 7) :
      app.addImage("zwarte bol" + str(x) + str(i), "zwarteBol.gif", x, i)
def rood():
  for x in range (1, 7) : 
    for i in range (0, 7) :
      if cf_board.board_deepcopy(connect_four_player)
def groen():
  for x in range (1, 7) : 
    for i in range (0, 7) :
      app.setImage("groene bol" + str(x) + str(i), "groeneBol.gif", x, i)
def roze():
  for x in range (1, 7) : 
    for i in range (0, 7) :
      app.setImage("roze bol" + str(x) + str(i), "rozeBol.gif", x, i)

app = gui("Grid", "400x500")
app.setBg("blue")
app.setFg("white")
app.addLabel("titel", "Connect four", 0, 0, 7)
app.addButton("Begin spel", beginSpel)

app.go()'''

