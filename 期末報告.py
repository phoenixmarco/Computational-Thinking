"print(\"哈囉!你好,這邊是幫你選擇三餐機器人，我是早餐機器人，很高興認識你\")\r\n", 
        "note = \"我只能接受很簡單的答案，請依提問回答，不然就會讀不出來!\"\r\n",  
        "print(note)\r\n",  
        "other = \"(貼心提醒:此機器人生性暴躁，請小心)\"\r\n",  
        "print(other)\r\n", 
        "name = input(\"請問你的大名是:\")\r\n",   
        "print(\"我叫\",name)\r\n",   
        "print(\"你好阿!\",name,)\r\n",    
        "answer = input(\"知道早餐要吃甚麼嗎:\")\r\n",   
        "if answer == \"知道\":\r\n", 
        "  print('那就不需要我囉，別來亂:)') \r\n",    
        "elif answer == \"不知道\":\r\n",  
        "  print(\"那你還知道甚麼?只好讓我來幫助你了\")\r\n",   
        "  answer = input(\"你會不會很餓:\")\r\n",    
        "if answer== \"會\":\r\n",   
        "  print(\"看來是食量很大的朋友呢\")\r\n", 
        "  answer = input(\"喜歡吃吐司，漢堡還是鐵板麵:\")\r\n", 
        "if answer== \"吐司\":\r\n",  
        "  print(\"真沒創意\")\r\n",    
        "  answer = input(\"那你喜歡甚麼口味的呢?巧克力，花生，奶酥\")\r\n",   
        "if answer== \"巧克力\":\r\n", 
        "  print(\"會變胖ㄟ!但你應該沒差!那今天就吃巧克力厚片吧!\")\r\n",    
        "elif answer == \"花生\" :\r\n",  
        "  print(\"會變胖ㄟ!但你應該沒差!那今天就吃花生厚片吧!\")\r\n", 
        "elif answer == \"奶酥\" :\r\n",  
        "  print(\"會變胖ㄟ!但你應該沒差!那今天就吃奶酥厚片吧!\")\r\n", 
        "elif answer == \"漢堡\" :\r\n",  
        "  print(\"看來你真的很餓呢\")\r\n",    
        "  answer = input(\"那妳喜歡甚麼口味的呢?卡拉雞，嫩切雞，里肌，\")\r\n", 
        "if answer== \"卡拉雞\":\r\n", 
        "  print(\"那今天就吃卡拉雞腿堡吧!肯德基歡迎你\")\r\n",  
        "elif answer == \"嫩切雞\" :\r\n", 
        "  print(\"那今天就吃嫩切雞腿堡吧!肯德基歡迎你\")\r\n",  
        "elif answer == \"里肌\" :\r\n",  
        "  print(\"聽起來很不可口，但看在你喜歡的份上就吃里肌漢堡吧!\")\r\n",   
        "elif answer == \"鐵板麵\" :\r\n", 
        "  print(\"哇!我也喜歡吃鐵板麵呢!\")\r\n",    
        "  answer = input(\"那妳喜歡甚麼口味的呢?胡椒，蘑菇，肉醬\")\r\n",    
        "if answer== \"胡椒\":\r\n",  
        "  print(\"好選擇!感覺就能吃很飽!那今天就吃胡椒鐵板麵吧!\")\r\n",    
        "elif answer == \"蘑菇\" :\r\n",  
        "  print(\"好選擇!感覺就能吃很飽!那今天就吃蘑菇鐵板麵吧!\")\r\n",    
        "elif answer== \"肉醬\":\r\n",    
        "  print(\"好選擇!感覺就能吃很飽!那今天就吃義大利肉醬麵吧!\")\r\n",   
        "elif answer == \"不會\":\r\n",   
        "  print(\"不要再假裝小鳥胃了!\")\r\n",  
        "  answer = input(\"好吧，喜歡吃吐司，蛋餅還是其他小東西:\")\r\n",    
        "  if answer== \"吐司\":\r\n",    
        "    print(\"哇!好沒創意\")\r\n",    
        "    answer = input(\"那妳喜歡甚麼口味的呢?巧克力，花生，奶酥\")\r\n", 
        "    if answer== \"巧克力\":\r\n", 
        "      print(\"小心會變胖!但你應該不在乎!那今天就吃巧克力薄片吧!\")\r\n",  
        "    elif answer == \"花生\" :\r\n",  
        "      print(\"小心會變胖!但你應該不在乎!那今天就吃花生薄片吧!\")\r\n",   
        "    elif answer == \"奶酥\" :\r\n",  
        "      print(\"小心會變胖!但你應該不在乎!那今天就吃奶酥厚片吧!\")\r\n",   
        "  if answer== \"蛋餅\":\r\n",    
        "    print(\"早餐店就是要吃蛋餅阿\")\r\n",    
        "    answer = input(\"那妳喜歡甚麼口味的呢?玉米，起司，火腿\")\r\n",  
        "    if answer== \"玉米\":\r\n",  
        "      print(\"好選擇!我的必點名單!那今天就吃玉米蛋餅吧!\")\r\n",  
        "    elif answer == \"起司\" :\r\n",  
        "      print(\"好選擇!融化起司最對味!那今天就吃火腿蛋餅吧!\")\r\n", 
        "    elif answer == \"火腿\" :\r\n",  
        "      print(\"好選擇!早餐店必吃!那今天就吃火腿蛋餅吧!\")\r\n",   
        "  if answer== \"其他炸物\":\r\n",  
        "    print(\"有夠不健康\")\r\n", 
        "    answer = input(\"那這三樣中挑一個你最喜歡的!薯餅，薯條，雞塊\")\r\n",   
        "    if answer== \"薯餅\":\r\n",  
        "      print(\"那今天就吃薯餅吧!但還是不要太常吃炸的喔!\")\r\n",   
        "    elif answer == \"薯條\" :\r\n",  
        "      print(\"那今天就吃薯條吧!但還是不要太常吃炸的喔!\")\r\n",   
        "    elif answer == \"雞塊\" :\r\n",  
        "      print(\"那今天就吃雞塊吧!但還是不要太常吃炸的喔!\")"    
      ],    
      "execution_count": 18,    
      "outputs": [  
        {   
          "output_type": "stream",  
          "text": [ 
            "哈囉!你好,這邊是幫你選擇三餐機器人，我是早餐機器人，很高興認識你\n",  
            "我只能接受很簡單的答案，請依提問回答，不然就會讀不出來!\n",   
            "(貼心提醒:此機器人生性暴躁，請小心)\n",    
            "請問你的大名是:嗨\n",  
            "我叫 嗨\n",   
            "你好阿! 嗨\n", 
            "知道早餐要吃甚麼嗎:不知道\n",  
            "那你還知道甚麼?只好讓我來幫助你了\n",  
            "你會不會很餓:不會\n",  
            "不要再假裝小鳥胃了!\n", 
            "好吧，喜歡吃吐司，蛋餅還是其他小東西:吐司\n",  
            "哇!好沒創意\n", 
            "那妳喜歡甚麼口味的呢?巧克力，花生，奶酥巧克力\n",    
            "小心會變胖!但你應該不在乎!那今天就吃巧克力薄片吧!\n"  
          ],    
          "name": "stdout"  
        }   
      ] 
    }   
  ] 
}