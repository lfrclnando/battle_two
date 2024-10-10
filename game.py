import random
class Character:
  """ Character construct class """

  def __init__(self, name, age, height, weight, life, level) -> None:
    self.__name = name
    self.__age = age
    self.__height = height
    self.__weight = weight
    self.__life = life
    self.__level = level

  def get_name(self):
    return self.__name
  
  def get_age(self):
    return self.__age
  
  def get_height(self):
    return self.__height
  
  def get_weight(self):
    return self.__weight
  
  def get_life(self):
    return self.__life
  
  def get_level(self):
    return self.__level
  
  def show_details(self):
    return f"Nome: {self.get_name()}\nIdade: {self.get_age()}\nAltura: {self.get_height()}\nPeso: {self.get_weight()}\nVida: {self.get_life()}\nNível: {self.get_level()}"
  
  def receive_attack(self, damage):
    """ Receive attack method """
    self.__life -= damage
    if self.__life < 0:
      self.__life = 0

  def attack(self, target):
    """ Attack method """
    damage = random.randint(self.get_level() * 4, self.get_level() * 8)
    target.receive_attack(damage)
    print(f"{self.get_name()} atacou o {target.get_name()} e causou {damage} de dano...")
  
class Hero(Character):
  """ Hero class """

  def __init__(self, name, age, height, weight, life, level, special_ability) -> None:
    super().__init__(name, age, height, weight, life, level)
    self.__special_ability = special_ability

  def get_special_ability(self):
    return self.__special_ability

  def show_details(self):
    return super().show_details() + f"\nHabilidade Especial: {self.get_special_ability()}\n"
  
  def spacial_attack(self, target):
    """ Special attack method """
    damage = random.randint(self.get_level() * 7, self.get_level() * 15)
    target.receive_attack(damage)
    print(f"{self.get_name()} atacou o {target.get_name()} com a habilidade especial {self.get_special_ability()} e causou {damage} de dano!!!")

class Enemy(Character):
  """ Enemy class """

  def __init__ (self, name, age, height, weight, life, level, enemy_type) -> None:
    super().__init__(name, age, height, weight, life, level)
    self.__enemy_type = enemy_type
  
  def get_enemy_type(self):
    return self.__enemy_type
  
  def show_details(self):
    return super().show_details() + f"\nTipo do Inimigo: {self.get_enemy_type()}\n"
  
class Game:
  """ The game's orchestrator class """

  def __init__(self) -> None:
    self.hero = Hero(name="Cavaleiro da Luz", age=30, height=1.80, weight=90, life=300, level=15, special_ability="Super Força")
    self.enemy = Enemy(name="Dragão de Lava", age=300, height=250, weight=13000, life=500, level=20, enemy_type="Voador")
    
  def start(self):
    """ Method for managing the battle in turns """
    print("BEM-VINDO(A) A BATALHA DOS DOIS!!!")
    while self.hero.get_life() > 0 and self.enemy.get_life() > 0:
      print("Detalhes dos Personagens:")
      print(self.hero.show_details())
      print(self.enemy.show_details())

      input("\nPressione Enter para iniciar a batalha...")
      choose = input("Escolha (1 - Atacar ou 2 - Ataque Especial): ")

      if choose == "1":
        self.hero.attack(self.enemy)
      elif choose == "2":
        self.hero.spacial_attack(self.enemy)
      else:
        print("Escolha inválida. Tente novamente...")
      
      if self.enemy.get_life() > 0:
        self.enemy.attack(self.hero)

    if self.hero.get_life() > 0:
      print(f"\n{self.hero.get_name()} venceu a batalha!!!🎉 Parabéns🎆🎆")
    else:
      print(f"\n{self.enemy.get_name()} venceu a batalha!!! E você Perdeu 😿")

# Create game instance and start battle
game = Game()
game.start()
