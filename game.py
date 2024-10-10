class Character:
  """ Character construct class """
  def __init__(self, name, age, height, weight, life, level) -> None:
    self._name = name
    self._age = age
    self._height = height
    self.weight = weight
    self.life = life
    self.level = level

  def get_name(self):
    return self._name
  
  def get_age(self):
    return self._age
  
  def get_height(self):
    return self._height
  
  def get_weight(self):
    return self.weight
  
  def get_life(self):
    return self.life
  
  def get_level(self):
    return self.level
  
  def show_details(self):
   return f"Nome: {self._name}\nIdade: {self._age}\nAltura: {self._height}\nPeso: {self.weight}\nVida: {self.life}\nNível: {self.level}"
  

