class Hero:
    name = '松田'
    hp = 100
    def sleep(self, hours):
        print(f'{self.name}は{hours}時間寝た!')
        self.hp += hours

# ゲーム開始
print('スッキリファンタジーXII ~金色の理想郷~')
h = Hero()
h.sleep(3)
print(f'{h.name}のHPは現在{h.hp}です')