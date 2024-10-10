import random
class Character:
  """ Character construct class """
  def __init__(self, name, age, height, weight, life, level) -> None:
    self._name = name
    self._age = age
    self._height = height
    self._weight = weight
    self._life = life
    self._level = level

  def get_name(self):
    return self._name
  
  def get_age(self):
    return self._age
  
  def get_height(self):
    return self._height
  
  def get_weight(self):
    return self._weight
  
  def get_life(self):
    return self._life
  
  def get_level(self):
    return self._level
  
  def show_details(self):
   return f"Nome: {self.get_name}\nIdade: {self.get_age}\nAltura: {self.get_height}\nPeso: {self.get_weight}\nVida: {self.get_life}\nNível: {self.get_level}"
  
  def receive_attack(self, damage):
    """ Receive attack method """
    self._life -= damage
    if self._life < 0:
      self._life = 0
    #   print(f"{self.get_name()} morreu!!!")
    # else:
    #   print(f"{self.get_name()} sofreu {damage} de dano, restam {self.get_life()} de vida")

    def attack(self, target):
      """ Attack method """
      damage = random.randint(self.get_level() * 4, self.get_level() * 8)
      target.receive_attack(damage)
      print(f"{self.get_name()} atacou o {target.get_name()} e causou {damage} de dano...")
  
  class Hero(Character):
    """ Hero class """
    def __init__(self, name, age, height, weight, life, level, special_ability) -> None:
      super().__init__(name, age, height, weight, life, level)
      self._special_ability = special_ability

    def get_special_ability(self):
      return self._special_ability

    def show_details(self):
      return super().show_details() + f"\nHabilidade Especial: {self.get_special_ability}\n"
    
    def spacial_attack(self, target):
      """ Special attack method """
      damage = random.randint(self.get_level() * 7, self.get_level() * 15)
      target.receive_attack(damage)
      print(f"{self.get_name()} atacou o {target.get_name()} com a habilidade especial {self.get_special_ability()} e causou {damage} de dano!!!")

  class Enemy(Character):
    """ Enemy class """
    def __init__ (self, name, age, height, weight, life, level, enemy_type) -> None:
      super().__init__(name, age, height, weight, life, level)
      self._enemy_type = enemy_type
    
    def get_enemy_type(self):
      return self._enemy_type
    
    def show_details(self):
      return super().show_details() + f"\nTipo do Inimigo: {self.get_enemy_type}\n"


