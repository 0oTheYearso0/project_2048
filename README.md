1. 將2048核心算法定義到核心類GameCoreController中，
   作為實例成員
   
2. 產生新數字
   -- 隨機位置（計算出所有空位置，隨機選擇一個）
   -- 2(90%) 或者 4(10%)

3. 判斷遊戲是否結束
   -- 如果有空位置，遊戲不能結束
   -- 如果橫向/縱向可以移動，遊戲不能結束
   -- 以上條件不滿足，遊戲結束

4. 創建控制台遊戲視圖GameConsoleView
   遊戲開始時，產生2個新數字，繪製界面，
   遊戲邏輯，獲取玩家輸入wsad移動地圖，產生新數字，判斷遊戲是否結束
   