import time
from ArbeiterProto import Arbeit
from conf import mess
import random

messArbeiter = Arbeit()

def messArbeiterProcess(sessions):
    oId = int(input("Введите ID беседы: "))
    while(True):
        print("Отправка сообщения, 1-5 секунд")
        time.sleep(random.randint(1, 5))
        for s in sessions:
            s["vkApi"].messages.send(peer_id=oId + 2000000000, message=mess, random_id=random.randint(-2147483648, 2147483648))

messArbeiter.process = messArbeiterProcess
messArbeiter.desc = "Спамит в беседу"
messArbeiter.name = "Насрать в свинотред"