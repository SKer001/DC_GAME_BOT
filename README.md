# DC_GAME_BOT
## The bot for the cat!!!
>2023/09/14 更
*****
* [作者](#author)
* [機器人](#bot)
* [目前功能](#command)
* [目前BUG](#error)
* [未來功能](#for_updata)
* [Code說明](#code)
*****
<h2 id="author">關於我</h2>

嗨嗨，我是幽靈yurei，是一名就學中的高三生，平時**極**熱愛打遊戲，也喜歡寫寫程式(不過現在比較會的也只有python😅)

<h2 id="bot">關於機器人</h2>

機器人的由來就只是我單純的興趣，有一部分是因為看到discord上面有許多充滿可玩性的機器人，所以我寫了這個機器人，來挑戰自我，看看能不能寫出有功能性且有可玩性的機器人，喵!!

<h2 id="command">目前功能(指令前綴為^，所有指令皆可用/指令)</h2>

* 食物系統
  * 可以隨機選擇你要吃的食物
  * 添加食物到bot的資料庫裡
  * 查看資料庫裡的食物選項有哪些

* 公會系統
  * 登記公會(機器人一般來說一進服會自動登記，此功能為手動登記，會覆蓋已登記內容)

* 雜項
  * (slash)查詢個人資料(開發為測試斜線指令)
  * bot高階指令(為開發者所用，一般人使用會返回“你沒資格”)

<h2 id="error">目前已知錯誤</h2>

_OPENAI的api要錢qwq_

<h2 id="for_updata">開發、持續更新(如果我有新想法🤧)</h2>
完成➝O

半完成➝\
還沒做➝X

- [\\] 食物系統
- [O] 指令紀錄系統
- 遊戲系統
  - [X] RPG系統
  - [\\] 卡牌對戰系統
  - [X] 金錢系統
- [O] 定時系統
- [X] AI聊天系統
*****
[![Run on Repl.it](https://replit.com/badge/github/SKer001/DC_GAME_BOT)](https://replit.com/new/github/SKer001/DC_GAME_BOT)

<h1 id="code">Code說明</h1>

- [基本建立](#basic_setup)
  - [建立Bot](#create_bot)

*****

<h2 id="basic_setup">基本建立</h2>

`有關於創建一個DC機器人，在這邊就不做講解了，此文件指說明程式碼的部分`

* <h3 id="create_bot">建立Bot</h3>

1. 先引入discord以及discord.ext的commands模組

1. 設定Intents，並把一些要用的權限打開

1. 創建Bot變數並定義為commands.Bot

```ruby
#1
import discord                  
from discord.ext import commands

#2 打開權限才可以讓有些程式碼正常運作
intents = discord.Intents.default()
intents.members = True             
intents.message_content = True     
intents.messages = True            
intents.guilds = True    

#3 bot事變數名(可更換)，Bot裡要輸入一個必要參數[command_prefix]，另一個重要參數是intents，就是第二步的intents
bot = commands.Bot(command_prefix='^',intents=intents)

#4
```
