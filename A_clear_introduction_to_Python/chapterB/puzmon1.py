'''
作成日: XXXX年YY月ZZ日
作成者: 松田
'''
# インポート
# グローバル変数の宣言

# 関数宣言
def do_battle(monster):
    print(f'{monster}が現れた!')
    print(f'{monster}を倒した!')
    return 1

def go_dungeon(name):
    print(f'{name}はダンジョンに到達した')
    is_win =do_battle('スライム')
    is_win =do_battle('ゴブリン')
    is_win =do_battle('オオコウモリ')
    is_win =do_battle('ウェアウルフ')
    is_win =do_battle('ドラゴン')
    print(f'{name}はダンジョンに制覇した')

def main():
    name = input('プレイヤー名を入力してください>')
    if name == '':
        print('エラー:プレイヤー名を入力してください')
        return
    print('*** Puzzle & Monsters ***')
    go_dungeon(name)
    print('*** GAME CLEARED!! ***')
    print('倒したモンスターの数=5')



# main関数の呼び出し
main()
