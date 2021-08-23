import time
from ArbeiterProto import Arbeit
from conf import mess
import random

messArbeiter = Arbeit()

def messArbeiterProcess(sessions):
    print("При спаме в личку группы, стаьте перед id минус")
    oId = input("Введите ID группы\пользователя: ")
    while(True):
        print("Отправка сообщения, 1-5 секунд")
        time.sleep(random.randint(1, 5))
        for s in sessions:
            s["vkApi"].messages.send(peer_id=oId, message=mess, random_id=random.randint(-2147483648, 2147483648))

messArbeiter.process = messArbeiterProcess
messArbeiter.desc = "Спамит в личные сообщения"
messArbeiter.name = "Насрать в личку хуеглоту"