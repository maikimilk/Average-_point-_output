# 入力された平均点を計算するプログラム
score = [0] * 1000
# 入力部
def inNUm(num, i):
    score[i] = num

# 演算部
def ave(i):
    add = 0
    for i in range(0, i):
        add = score[i] + add

    return add / (i + 1)


# 表示部
def view(i):
    for i in range(0, i):
        print("入力されたスコアを表示する")
        print("score =" + str(score[i]))

# main
print("平均スコアを計算します。")
print("三桁までの整数を入力してEnterキーを押してください。")
print("終了時は -1 と入力してください。")

c = 0

while True:
    num = int(input("score = "))

    if 0 <= num <= 100:
        inNUm(num, c)
        c = c + 1
    elif num == -1:
        re = ave(c)
        print("全てのスコアの平均は :", re)
        print("入力を終了します")
        break
    else:
        print("0~100の整数を入力してください")
