"""
    遊戲界面邏輯模塊
"""
import os

from bll import GameCoreController


class GameConsoleView:
    """
        控制台界面類
    """

    def __init__(self):
        self.__controller = GameCoreController()

    def __start(self):
        self.__controller.generate_new_number()
        self.__controller.generate_new_number()
        self.__draw_map()

    def main(self):
        self.__start()
        self.__update()

    def __draw_map(self):
        # os.system("clear")
        for line in self.__controller.map:
            for item in line:
                print(item, end="\t")
            print()

    def __update(self):
        while True:
            self.__move_map_for_input()
            self.__controller.generate_new_number()
            self.__draw_map()
            if self.__controller.is_game_over():
                print("遊戲結束")

    def __move_map_for_input(self):
        direction = input("請輸入方向：")
        if direction == "w":
            self.__controller.move_up()
        elif direction == "a":
            self.__controller.move_left()
        elif direction == "s":
            self.__controller.move_down()
        elif direction == "d":
            self.__controller.move_right()
        else:
            print("請輸入正確的方向")