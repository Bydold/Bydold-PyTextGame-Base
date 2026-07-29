#设置根目录
import sys,subprocess
from pathlib import Path
from datetime import datetime
root = Path(__file__).parent.parent
sys.path.append(str(root))

#继承数据
lang=sys.argv[2]
if lang == "zh_CN":
    import Localisation.zh_CN
    l=Localisation.zh_CN
else:
    import Localisation.en_US
    l=Localisation.en_US

#清屏
subprocess.run('cls', shell=True)

#开始新游戏
if sys.argv[1] == "ng":
    save_name = str(datetime.now().strftime("%Y-%m-%d_%H-%M"))
    save_path = Path("Saves/" + save_name + ".txt")
    save_path.parent.mkdir(parents=True, exist_ok=True)
    with open(save_path, "w", encoding="utf-8") as f:
        f.write(sys.argv[3])
    print(l.sol_created+save_name)

#读取游戏