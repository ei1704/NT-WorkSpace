def out_csvdata(**kwargs):
    '''辞書型のデータをCSVで出力する
    
    Breakfast,Lunch,Dinnerの順に出力する
    '''
    keys = ['B','L','D']
    list_meals=[]
    for k in keys:
        if kwargs.get(k) == None:
            list_meals.append('-')
        else:
            list_meals.append(kwargs[k])

    print(list_meals)
# main
eat = {}
while True:
    menu = input("朝⾷(B) 昼⾷(L) ⼣⾷(D)と⾷べたものを⼊⼒してください：")
    if menu == '':
        break
    token, menu = menu.split(',')
    if token in ['B', 'L', 'D']:
        eat[token] = menu
    else:
        print('記号が間違っています。登録しません')
        continue

out_csvdata(**eat)
