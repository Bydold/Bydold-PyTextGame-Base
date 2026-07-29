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
debug = sys.argv[3]

#游戏过程
print(debug)