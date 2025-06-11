import random

class Synkrusis():
  def __init__(self, name, element, health, speed):
    self.name = name.title()
    self.element = element
    self.current_health = health
    self.max_health = health
    self.speed = speed
    self.is_alive = True

    
  def light_attack(self, enemy):
    damage = random.randint(15, 25)
    print('Agent ' + self.name + ' used ' + self.moves[0] + '.')
    print('It dealt ' + str(damage) + ' damage.')
    enemy.current_health -= damage


  def heavy_attack(self, enemy):
    damage = random.randint(0, 50)
    print('Agent ' + self.name + ' used ' + self.moves[1] + '.')
    if damage < 10:
      print('The attack missed.')
    else:  
      print('It dealt ' + str(damage) + ' damage.')
      enemy.current_health -= damage


  def restore():
    pass


  def faint():
    pass


  def show_stats():
    pass


class Fire():
  pass


class Water():
  pass


class Grass():
  pass


class Game():
  pass