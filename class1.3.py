from class1 import game
class game2(game):

    def __init__(self,player='new',score=0,level=1,life=100):
      game.__init__(game,player,level,score)
      self.life_=life
    def show (self):
          game.show(game)
          print('life:',self.life_)
alaa=game2(player='allaa',score=10,level=2,life=200)

game.change_level(game,5)
alaa.show()
