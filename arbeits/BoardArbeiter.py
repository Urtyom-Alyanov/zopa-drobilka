import random
import time
from ArbeiterProto import Arbeit
from conf import mess

boardArbeiter = Arbeit()

def boardArbeiterProcess(sessions):
    gId = input("Введите ID группы: ")
    bId = input("Введите ID обсуждения: ")
    while(True):
        print("Отправка сообщения, 1-5 секунд")
        time.sleep(random.randint(1, 5))
        for s in sessions:
            s["vkApi"].board.createComment(group_id=gId, topic_id=bId, message=mess)

boardArbeiter.process = boardArbeiterProcess
boardArbeiter.desc = "Спамит на обсуждения группы"
boardArbeiter.name = "Насрать в обсуждения группы"