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


  def restore(self):
    heal = random.randint(15, 25)
    print('Agent ' + self.name + ' used ' + self.moves[2] + '.')
    print('It healed ' + str(heal) + ' health.')
    self.current += heal

    if self.current_health > self.max_health:
      self.current_health = self.max_health


  def faint(self):
    if self.current_health <= 0:
      self.is_alive = False
      print('Agent' + self.name + ' is unconscious.')
      print('Press Enter to continue.')


  def show_stats(self):
    print('\nAgent: ' + self.name)
    print('Element Type: ' + self.element)
    print('Health: ' + str(self.current_health) + '/' + str(self.max_health))
    print('Speed: ' + str(self.speed))

class Fire(Synkrusis):
  def __init__(self, name, element, health, speed):
    super().__init__(self, name, element, health, speed)
    moves = ['Scratch', 'Ember', 'Light', 'Fire Blast']


  def special_attack():
    

  
  def move_info():
    pass


class Water():
  pass


class Grass():
  pass


class Game():
  pass