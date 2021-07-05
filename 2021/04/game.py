"""Game file

Author: chunyang.feng@17zuoye.com

Date: 2021/4/26 17:09

Desc:
    2021/4/26 17:09 add file.
"""
import random
import time


class FingerGame:
    def __init__(self):
        self._name = ""
        self._score = 0
        self._win = 0
        self._lose = 0
        self._draw = 0
        self._total = 0
        self._reward = 2
        self._punish = 1
        self._mapper = {
            1: "剪刀",
            2: "石头",
            3: "布",
        }

    @staticmethod
    def get_input():
        user_input = input()
        return user_input

    @staticmethod
    def generate_number():
        number = random.randint(1, 3)
        return number

    def _clear(self):
        self._score = 0
        self._win = 0
        self._draw = 0
        self._lose = 0
        self._total = 0
        print("您游戏信息已经清零，即将开始新游戏...")

    def _set_name(self):
        name = input("开始游戏前，请为您起一个响亮的名字：\n")
        self._name = name

    @staticmethod
    def _game_desc():
        print("=" * 30)
        print("石头剪刀布\n\t\t1 开始游戏\n\t\t2 结束游戏\n\t\t3 查看得分\n\t\t4 重新开始\n")
        print("=" * 30)

    def _game_process(self):
        self._game_desc()
        select = int(input("请选择："))
        while True:
            if select == 1:
                self.start()
            elif select == 2:
                print("即将退出游戏，欢迎下次光临！\n")
                time.sleep(2)
                break
            elif select == 3:
                self._info()
            elif select == 4:
                self._clear()
                self.start()
            else:
                print("无效的选择")

    def _has_win(self):
        print(f"恭喜你，你赢了！获得 {self._reward} 分，再接再厉！")
        self._score += self._reward
        self._win += 1

    def _has_draw(self):
        print("平局！\n")
        self._draw += 1

    def _has_lose(self):
        print(f"很遗憾，你输了！扣掉 {self._punish} 分，继续加油！")
        self._lose += 1
        self._score -= self._punish

    def _info(self):
        print(f"亲爱的玩家 {self._name}，您本次游戏共获得 {self._score} 分，一共进行了 {self._total} 场游戏，赢了 {self._win} 次，"
              f"输了 {self._lose} 次，平局 {self._draw} 次")

    def _detail(self):
        print(f"第 {self._total} 局游戏，当前 {self._score} 分，赢了 {self._win} 次，输了 {self._lose} 次，平局 {self._draw} 次\n")

    def start(self):
        print("现在开始进行剪刀石头布的游戏，1表示剪刀，2表示石头，3表示布，0表示退出游戏返回主菜单\n")
        while True:
            punch = int(input("请出拳："))
            if punch == 0:
                break

            player_punch = self._mapper.get(punch)
            if player_punch is None:
                print("你出了一个奇怪的动作，本次游戏视为你弃权\n")
                self._has_lose()
            else:
                ai_punch = self.generate_number()
                print(f"你出了 {player_punch},电脑出了 {self._mapper.get(ai_punch)}\n")

                result = punch - ai_punch
                if result == 1 or result == -2:
                    self._has_win()
                elif result == 0:
                    self._has_draw()
                else:
                    self._has_lose()
                self._total += 1
                self._detail()

    def main(self):
        try:
            self._set_name()
            self._game_process()
        except ValueError:
            self._game_process()


if __name__ == '__main__':
    game = FingerGame()
    game.main()





