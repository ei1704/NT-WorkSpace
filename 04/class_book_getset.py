class Book:
    def __init__(self,val):
      self.set_val(val)
      self.set_discounts(0)
      type(self).tax = 10

    def get_val(self):
      return self.__value
    
    def set_val(self,val):
      if val <= 0:
        raise ValueError("本体価格は正の整数で指定してください")
      self.__value = val

    def get_discounts(self):
      return self.__discounts

    def set_discounts(self,val):
      if val < 0 or 100 < val:
        raise ValueError("値引き率は0-100で指定してください")
      self.__discounts = val

    def price(self):
      return int((self.get_val() - self.get_val() * (self.get_discounts() * 0.01)) * (1 + type(self).tax * 0.01))

#main
b1 = Book(1000)     # 定価1000円の本
print(f'現在の値引率：{b1.get_discounts()}%')
b1.set_discounts(10)   # 値引率 10%
print(f'現在の値引率：{b1.get_discounts()}%')
print(f'販売価格：{b1.price()}')
print('-='*30)

b2 = Book(2000)     # 定価2000円の本
print(f'現在の値引率：{b2.get_discounts()}%')
b2.set_discounts(10)  # 値引率 -10%
print(f'現在の値引率：{b2.get_discounts()}%')
print(f'販売価格：{b2.price()}')