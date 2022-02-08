import package.login as login
import package.path as path
import package.encrypt as encrypt


def insertUser():
    login.readUser()
    uname = login.getUsername()
    print("Sign up to this system")
    while (True):
        username = input("Username > ")
        if (checkFormat(username, 1) and checkLegitimacy(username, mode="username") and checkIn(username, uname, 1)):
            password = input("Password > ")
            if (checkFormat(password, 2) and checkLegitimacy(password, mode="password")):
                newline = "".join([username.ljust(15, " "), password.ljust(20, " "), "1\n"])
                with open(path.url_user, "a", encoding="UTF-8") as file_user:
                    file_user.write(encrypt.ency(newline))
                    file_user.flush()
                login.readUser()
                print("Sign up success\n")
                break
        con = input("Enter 1 to continue; 2 to break > ")
        if (con == "2"):
            print()
            break


def deleteUser():
    while (True):
        uname = login.getUsername()
        showUser()
        username = input("Delete user where username > ")
        if (checkIn(username, uname, 2)):
            confirm = input("Delete really ?  1:yes  2:no > ")
            if (confirm == "1"):
                with open(path.url_user, "r+", encoding="UTF-8") as file_user:
                    read = file_user.readlines()
                    line = -1
                    while (True):
                        line += 1
                        str = encrypt.decy(read[line])
                        arr = str.split()
                        if (arr[0] == username):
                            read.pop(line)
                            break
                with open(path.url_user, "w+", encoding="UTF-8") as file_user:
                    file_user.writelines(read)
                login.readUser()
                print("User delete success")
        con = input("Enter 1 to continue; 2 to break > ")
        if (con == "2"):
            print()
            break


def updateUser():
    while (True):
        old_pw = input("Please input your old password > ")
        if (old_pw == login.password):
            new_pw = input("New password > ")
            if (checkFormat(new_pw, 2) and checkLegitimacy(new_pw, mode="password")):
                with open(path.url_user, "r", encoding="UTF-8") as file_user:
                    read = file_user.readlines()
                unlen = 15
                pwlen = 20
                lelen = 1
                user: login.User
                user = login.user.get(login.username)
                text = encrypt.decy(read[user.line - 1])
                arr = text.split()
                arr[1] = new_pw
                newline = "".join([arr[0].ljust(unlen, " "), arr[1].ljust(pwlen, " "), arr[2].ljust(lelen, " "), "\n"])
                read[user.line - 1] = encrypt.ency(newline)
                with open(path.url_user, "w+", encoding="UTF-8") as file_user:
                    file_user.writelines(read)
                    file_user.flush()
                login.readUser()
                print("Password changed success")
        else:
            print("Old passwords do not match")
        con = input("Enter 1 to continue; 2 to break > ")
        if (con == "2"):
            print()
            break


def editUser():
    while (True):
        uname = login.getUsername()
        print("Current Account List".center(36, "-"))
        print("Username       Password        level")
        print("-" * 36)
        for item in uname:
            user: login.User = login.user.get(item)
            print("".join([user.username.ljust(15, " "), user.password.ljust(20, " "), str(user.level)]))
        print("-" * 36)
        username = input("Update user where username > ")
        if (checkIn(username, uname, 2)):
            unlen = 15
            pwlen = 20
            lelen = 1
            user = login.user.get(username)
            line = user.line
            err = 0
            with open(path.url_user, "r", encoding="UTF-8") as file_user:
                read = file_user.readlines()
            text = encrypt.decy(read[line - 1])
            arr = text.split()
            cho = input("Update ? Username:1  Password:2  level:3 > ")
            if (cho in ["1", "2", "3"]):
                new = input("Input new value > ")
                if (checkFormat(new, int(cho))):
                    if (cho == "1" and checkIn(new, uname, 1) and checkLegitimacy(new, mode="username")):
                        arr[0] = new
                    elif (cho == "2" and checkLegitimacy(new, mode="password")):
                        arr[1] = new
                    elif (cho == "3" and checkLegitimacy(new, mode="level")):
                        arr[2] = new
                    else:
                        err = 1
                else:
                    err = 1
            else:
                err = 1
                print("Parameter does not exist")
            if (err == 0):
                newline = "".join([arr[0].ljust(unlen, " "), arr[1].ljust(pwlen, " "), arr[2].ljust(lelen, " "), "\n"])
                read[line - 1] = encrypt.ency(newline)
                with open(path.url_user, "w+", encoding="UTF-8") as file_user:
                    file_user.writelines(read)
                    file_user.flush()
                login.readUser()
                print("Account edit success")
        con = input("Enter 1 to continue; 2 to break > ")
        if (con == "2"):
            print()
            break


def showUser():
    uname = login.getUsername()
    print("Account List".center(36, "-"))
    print("Username       Password        level")
    print("-" * 36)
    for item in uname:
        user: login.User = login.user.get(item)
        print("".join([user.username.ljust(15, " "), user.password.ljust(20, " "), str(user.level)]))
    print("-" * 36)


def checkFormat(strin: str, mode: int) -> bool:
    if (mode == 1):
        length = 10
        target = "Username"
    elif (mode == 2):
        length = 15
        target = "Password"
    elif (mode == 3):
        length = 1
        target = "Level"
    else:
        print("Error: Mode invalid")
        return False

    if (strin != ""):
        if (strin.find(" ") == -1):
            if (strin.__len__() <= length):
                return True
            else:
                print(" ".join([target, "too long, MAX:", str(length)]))
                return False
        else:
            print("Cannot contain Spaces")
            return False
    else:
        print("{0} cannot be empty".format(target))
        return False


def checkLegitimacy(strin: str, mode: str = "username") -> bool:
    if (mode == "username"):
        err = 0
        for char in strin:
            if (char.isalnum() or char == "_"):
                if (is_chinese(char)):
                    err = 1
            else:
                err = 2
        if (err == 0):
            return True
        else:
            if (err == 1):
                print("Username cannot contain chinese")
            if (err == 2):
                print("Username can contain only alphanumeric underscores")
            return False
    elif (mode == "password"):
        err = 0
        for char in strin:
            if (char.isalnum() or char == "_"):
                if (is_chinese(char)):
                    err = 1
            else:
                err = 2
        if (err == 0):
            return True
        else:
            if (err == 1):
                print("Password cannot contain chinese")
            if (err == 2):
                print("Password can contain only alphanumeric underscores")
            return False
    elif (mode == "level"):
        if (strin.isdecimal()):
            if (int(strin) >= 1 and int(strin) <= 3):
                return True
            else:
                print("Level must between 1 and 3")
                return False
        else:
            print("Level can contain only digital")
            return False
    else:
        print("Error: Illegal mode")
        return False


def checkIn(strin: str, listin: list, mode: int) -> bool:
    if (mode == 1):
        if (strin not in listin):
            return True
        else:
            print("Username already exists")
            return False
    elif (mode == 2):
        if (strin in listin):
            return True
        else:
            print("Username not exist")
            return False
    else:
        print("Error: Mode invalid")
        return False


def is_chinese(char) -> bool:
    if (char >= u'\u4e00' and char <= u'\u9fa5'):
        return True
    else:
        return False
