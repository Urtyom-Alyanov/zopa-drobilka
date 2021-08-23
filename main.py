import os, sys, importlib
import requests
from conf import getSession
from ArbeiterProto import arbeits_list

# {"vks": vk_session, "vkApi": vk, "token": {"token": str, "info": profileT}}
# 
# 
# 

class AuthException(Exception):
    def __init__(self, text):
        self.txt = text

# Validating tokens
def validate(tokens):
    validTokens = requests.post("https://zopa-anal.herokuapp.com/token_validate", json={
        "tokens": tokens
    }).json()
    if "err" in validTokens.keys():
        raise AuthException("Tokens is not valid")
    return validTokens

def fileParse():
    tokens = []
    file = open("token.txt", "r")
    for string in file:
        if string != "":
            if string[0:1] != "//":
                tokens.append(string)
    file.close()
    return tokens

def getValidTokens():
    tokens = fileParse()
    if len(tokens) == 0:
        raise AuthException("Tokens is not valid")
    return validate(tokens)["tokens"]

def auth():
    sessions = []
    tokens = getValidTokens()
    for token in tokens:
        sessions.append(getSession(token))
    return sessions

# Arbeits
def getArbeits():
    files = os.listdir(sys.path[0] + "\\arbeits")
    modules = filter(lambda x: x.endswith('.py'), files)
    for m in modules:
        importlib.import_module("arbeits." + m[0:-3])

def getArbeitNum():
    try:
        arbeit_num = int(input("Введите номер: ")) - 1
        if arbeit_num == -1:
            quit()
        return arbeit_num
    except ValueError as ve:
        print("Введите число")
        getArbeitNum()

def main():
    try:
        getArbeits()
        sessions = auth()
        for s in sessions:
            print(f"Пользователь {s['token']['info']['first_name']} {s['token']['info']['last_name']} (id{s['token']['info']['id']}) - Авторизирован")
        print("0 - Выйти из терминала")
        for a in range(len(arbeits_list)):
            print(f"{a + 1} - {arbeits_list[a].name} - {arbeits_list[a].desc}")
        anum = getArbeitNum()
        arbeits_list[anum].process(sessions)
    except AuthException as a:
        print(a.txt)
        return 0

if __name__ == "__main__":
    main()