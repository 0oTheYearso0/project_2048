"""
    遊戲核心邏輯控制器
"""
import random

from model import LocationModel


class GameCoreController:
    def __init__(self):
        self.__list_merge = None
        self.__map = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.__list_empty_location = []

    @property
    def map(self):
        return self.__map

    def __zero_to_end(self):
        """
            零元素移動到末尾
            思路：從後向前依次判斷，如果是零元素，則刪除後追加零。
        """
        for i in range(len(self.__list_merge) - 1, -1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    def __merge(self):
        """
            合併
            思路： 將零元素後移
                  判斷如果相鄰且相同則合併
        """
        self.__zero_to_end()
        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i] *= 2
                del self.__list_merge[i + 1]
                self.__list_merge.append(0)

    def move_left(self):
        """
            向左移動
            思路：將每行（一維列表）賦值給全局變量self.list_merge
                 再通過merge函數操作數據
        """
        for line in self.__map:
            self.__list_merge = line
            self.__merge()

    def move_right(self):
        """
            向右移動
            思路：將每行（反向切片）賦值給全局變量self.list_merge
                 再通過merge函數操作數據
                 再對self.list_merge（反向切片）
        """
        for line in self.__map:
            # 因為切片，所以創建了新列表
            self.__list_merge = line[::-1]
            self.__merge()  # 操作的是新列表
            line[::-1] = self.__list_merge

    def __square_matrix_transpose(self):
        for c in range(len(self.__map) - 1):
            for r in range(c + 1, len(self.__map)):
                self.__map[r][c], self.__map[c][r] = self.__map[c][r], self.__map[r][c]

    def move_up(self):
        """
            思想：方陣轉置
                 調用向左移動
                 方陣轉置
        """
        self.__square_matrix_transpose()
        self.move_left()
        self.__square_matrix_transpose()

    def move_down(self):
        """
            思想：方陣轉置
                 調用向右移動
                 方陣轉置
        """
        self.__square_matrix_transpose()
        self.move_right()
        self.__square_matrix_transpose()

    def generate_new_number(self):
        # 選擇位置
        self.__calculate_empty_location()
        if len(self.__list_empty_location) == 0:
            return
        loc = random.choice(self.__list_empty_location)
        # 計算數字
        # self.__map[loc[0]][loc[1]] = self.__select_random_number()
        self.__map[loc.r][loc.c] = self.__select_random_number()

    def __select_random_number(self):
        return 2 if random.randint(1, 10) > 1 else 4

    def __calculate_empty_location(self):
        self.__list_empty_location.clear()
        for r in range(len(self.__map)):
            for c in range(len(self.__map[r])):
                if self.__map[r][c] == 0:
                    # self.__list_empty_location.append((r, c))
                    self.__list_empty_location.append(LocationModel(r, c))

    def is_game_over(self):
        if len(self.__list_empty_location) > 0:
            return False
        for r in range(len(self.__map)):
            for c in range(len(self.__map[r]) - 1):
                if self.map[r][c] == self.__map[r][c + 1] or self.map[c][r] == self.__map[c+1][r]:
                    return False
        # for r in range(len(self.__map)):
        #     for c in range(len(self.__map[r])-1):
        #         if self.map[r][c] == self.__map[r][c+1]:
        #             return False
        #
        # for c in range(len(self.__map[0])):
        #     for r in range(len(self.__map)-1):
        #         if self.map[r][c] == self.__map[r+1][c]:
        #             return False
        return True
