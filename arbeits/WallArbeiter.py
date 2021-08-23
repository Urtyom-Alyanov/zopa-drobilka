import random
import time
from ArbeiterProto import Arbeit
from conf import mess

wallArbeiter = Arbeit()

def wallArbeiterProcess(sessions):
    print("При спаме на стену группы, стаьте перед id минус")
    oId = input("Введите ID группы\пользователя: ")
    while(True):
        print("Отправка сообщения, 1-5 секунд")
        time.sleep(random.randint(1, 5))
        for s in sessions:
            s["vkApi"].wall.post(owner_id=oId, message=mess)

wallArbeiter.process = wallArbeiterProcess
wallArbeiter.desc = "Спамит на стену группы\пользователя"
wallArbeiter.name = "Насрать на стену группы\пользователя"