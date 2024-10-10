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
  
  class Hero(Character):
    """ Hero class """
    def __init__(self, name, age, height, weight, life, level, special_ability) -> None:
      super().__init__(name, age, height, weight, life, level)
      self._special_ability = special_ability

    def get_special_ability(self):
      return self._special_ability

    def show_details(self):
      return super().show_details() + f"\nHabilidade Especial: {self.get_special_ability}\n"

