from random import randint

print('数当てゲームを始めます。3桁の数を当ててください!')

answer = []
for i in range(3):
    answer.append(randint(0, 9))

con = 1
while con == 1:

    prediction = []
    for i in range(3):
        n = int(input(f'{i+1}桁目の予想を入力(0~9) >>'))
        prediction.append(n)

    print(prediction)

    hit = 0
    blow = 0
    for n in range(3):
        if prediction[n] == answer[n]:
            hit += 1
        else:
            for m in range(3):
                if prediction[n] == answer[m]:
                    blow += 1
                    break

    print(f'{hit}ヒット! {blow}ボール!')

    if hit == 3:
        print('正解です!')
    else:
        con = int(input('続けますか? 1:続ける 2:終了 >>'))




    