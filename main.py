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
    self.current_health += heal

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


  def special_attack(self, enemy):
    print('Agent ' + self.name + ' used ' + self.moves[3])
    
    if enemy.element == 'Grass':
      print('That was very effective.')
      damage = random.randint(35, 50)
    elif enemy.element == 'Water':
      print('That was very ineffective.')
      damage = random.randint(-5, 10)
    else:
      random.randint(10, 30)

    print('It dealt ' + str(damage) + ' damage.')
    enemy.current_health -= damage
  

  def move_info(self):
    print('\n' + self.name + 'Moves: ')
    print('.. ' + self.moves[0] + ' ..')
    print('\t an efficient attack...')
    print('\tguaranteed to do damage with 15 to 25 points.')
    
    print('.. ' + self.moves[1] + ' ..')
    print('\t a risky attack...')
    print('\tcould deal damage up to 50 points.')
    
    print('.. ' + self.moves[2] + ' ..')
    print('\t a healing move...')
    print('\tguaranteed to heal between 15 to 25 points.')
    
    print('.. ' + self.moves[3] + ' ..')
    print('\t a fire based attack...')
    print('\tguaranteed to do damage to Grass type Agent.')


class Water(Synkrusis):
  def __init__(self, name, element, health, speed):
    super().__init__(self, name, element, health, speed)
    moves = ['Bite', 'Splash', 'Dive', 'Water Cannon']


  def special_attack(self, enemy):
    print('Agent ' + self.name + ' used ' + self.moves[3])
    
    if enemy.element == 'Fire':
      print('That was very effective.')
      damage = random.randint(35, 50)
    elif enemy.element == 'Grass':
      print('That was very ineffective.')
      damage = random.randint(-5, 10)
    else:
      random.randint(10, 30)

    print('It dealt ' + str(damage) + ' damage.')
    enemy.current_health -= damage


  def move_info(self):
    print('\n' + self.name + 'Moves: ')
    print('.. ' + self.moves[0] + ' ..')
    print('\t an efficient attack...')
    print('\tguaranteed to do damage with 15 to 25 points.')
    
    print('.. ' + self.moves[1] + ' ..')
    print('\t a risky attack...')
    print('\tcould deal damage up to 50 points.')
    
    print('.. ' + self.moves[2] + ' ..')
    print('\t a healing move...')
    print('\tguaranteed to heal between 15 to 25 points.')
    
    print('.. ' + self.moves[3] + ' ..')
    print('\t a fire based attack...')
    print('\tguaranteed to do damage to Fire type Agent.')


class Grass():
  pass


class Game():
  pass