#设置根目录
import sys
from pathlib import Path
root = Path(__file__).parent.parent
sys.path.append(str(root))

#获取系统语言
import time,subprocess
import locale
lang = locale.getdefaultlocale()
if lang[0] == "zh_CN":
    import Localisation.zh_CN
    l=Localisation.zh_CN
else:
    import Localisation.en_US
    l=Localisation.en_US

#定义：开始新游戏
def NewGame():
    while True:
        subprocess.run('cls', shell=True)
        print(l.startmenu_newgame1)
        if "debug" not in locals():
            debug = "0"
        print("debug="+debug)
        print(l.startmenu_newgame2)
        selection = input(l.startmenu_select)
        if selection == "1":
            debug = input("debug=")
        elif selection == "0":
            subprocess.Popen(["python", "Parts/save_or_load.py", "ng", lang[0], debug])
            exit()
            break
        else:
            print(l.startmenu_invalid)
            time.sleep(1)

#定义：加载游戏
def LoadGame():
    while True:
        subprocess.run('cls', shell=True)
        print(l.startmenu_loadgame1)
        saved_files = [file.name for file in Path('Saves').rglob("*.*")]
        for index in range(len(saved_files)):
          print("["+str(index)+"]"+saved_files[index])
        print(l.startmenu_loadgame2)
        select = input(l.startmenu_select)
        if select.isdigit():
            if 0 <= int(select) <= len(saved_files):
                selection = saved_files[int(select)]
                try:
                    with open("Saves/"+selection,"r", encoding="utf-8") as f:
                        list=f.readlines()
                except IOError:
                    print(l.startmenu_invalid)
                    time.sleep(1)
                else:
                    subprocess.Popen(["python", "Parts/save_or_load.py", "lg", lang[0], selection])
                    exit()
                    break
            else:
                        print(l.startmenu_invalid)
                        time.sleep(1)
        else:
            print(l.startmenu_invalid)
            time.sleep(1)
    

#展示开始界面
while True:
    subprocess.run('cls', shell=True)
    print(l.startmenu_startmenu)
    selection = input(l.startmenu_select)
    if selection == "1":
        NewGame()
        break
    elif selection == "2":
        if not Path("Saves").exists():
            print(l.startmenu_loadinvalid)
            time.sleep(1)
        else:
            if any(Path("Saves").iterdir()):
                LoadGame()
                break
            else:
                print(l.startmenu_loadinvalid)
                time.sleep(1)
    elif selection == "0":
        print(l.startmenu_quit)
        time.sleep(0.5)
        exit()
    else:
        print(l.startmenu_invalid)

