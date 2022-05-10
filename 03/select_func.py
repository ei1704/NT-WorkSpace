# 関数を辞書で渡し、実行する
from cProfile import run


def func1():
    print("Hello")


def func2():
    print("Goodbye")


# 一般的なmainの記述
if __name__ == "__main__":
    # execute only if run as a script
    run_list = {'a': func1, 'b': func2}

    while True:
        print('a=>Hello,b=>Goodbye')
        print('どちらを実行しますか？：',end="")

        input_str = input()
        if input_str == "":
            break
        elif input_str not in run_list:
            print("どちらかを選択してください。")
            continue
        else:
            run_list[input_str]()
        