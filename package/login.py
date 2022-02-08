import package.path as path
import package.encrypt as encrypt
import time
import sys

user: dict = {}
uname: list = []
level: int = 0
username: str
password: str


def login() -> int:
    print("Login system: ")
    readUser()

    num = 0
    while (True):
        num += 1
        if (num > 5):
            print("Five login failures, System exit")
            return 0

        un = input("Username > ")
        pw = input("Password > ")

        if (un in uname):
            u = user.get(un)
            if (pw == u.password):
                global level
                global username
                global password
                level = u.level
                username = un
                password = pw
                print()
                print("Today:{0} {1} Welcome {2}  :)".format(time.strftime("%Y-%m-%d"), time.strftime("%H:%M:%S"), un))
                time.sleep(1)
                return 1
            else:
                print("Wrong password")
        else:
            print("Username not exist")

        con = input("Enter 1 to continue; 2 to break > ")
        if (con == "2"):
            print()
            return 0


class User:
    username: str
    password: str
    level: int
    line: int

    def __init__(self, username, password, level, line) -> None:
        self.username = username
        self.password = password
        self.level = level
        self.line = line


def readUser():
    with open(path.url_user, "r", encoding="UTF-8") as file_user:
        userlist = file_user.readlines()
    line = 0
    global uname
    global user
    user.clear()
    uname.clear()
    try:
        for item in userlist:
            line += 1
            text = encrypt.decy(item)
            arr = text.split()
            uname.append(arr[0])
            user[arr[0]] = User(arr[0], arr[1], int(arr[2]), line)
    except Exception as e:
        print("Error: User file damaged")
        sys.exit()


def getLevel() -> int:
    global level
    return level


def getUsername() -> list:
    global uname
    return uname
