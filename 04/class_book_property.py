class Book:
    def __init__(self,val):
      self.val = val
      self.discounts = 0
      type(self).tax = 10

    @property
    def val(self):
      return self.__value
    
    @val.setter
    def val(self,val):
      if val <= 0:
        raise ValueError("本体価格は正の整数で指定してください")
      self.__value = val

    @property
    def discounts(self):
      return self.__discounts

    @discounts.setter
    def discounts(self,val):
      if val < 0 or 100 < val:
        raise ValueError("値引き率は0-100で指定してください")
      self.__discounts = val

    def price(self):
      return int((self.val - self.val * (self.discounts * 0.01)) * (1 + type(self).tax * 0.01))

#main
b1 = Book(1000)
print(f'現在の値引率：{b1.discounts}%')
b1.discounts = 10
print(f'現在の値引率：{b1.discounts}%')
print(f'販売価格：{b1.price()}')

b2 = Book(2000)
print(f'現在の値引率：{b1.discounts}%')
b1.discounts = -10
print(f'現在の値引率：{b1.discounts}%')
print(f'販売価格：{b1.price()}')