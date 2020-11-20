import random

randomInt = random.randint(1, 10)

txt = ""
if randomInt <= 5:
    txt = str(randomInt) + "は５以下です"

print(txt)
