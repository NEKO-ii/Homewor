# SSMS_cmd 主程序入口
import package.login as login
import package.user as user
import package.student as stu
import package.encrypt as encrypt
import package.imexport as imex
import time

version: str = "V1.2"
uptime: str = "2022.02.08"

encrypt.initFernet()

operation = [["Query Score"], ["Show Student Info", "Student Info Sort", "Update Student Score", "Insert Student", "Delete Student", "Edit Student Info", "Import Student", "Export Student"],
             ["Show All Account", "Insert Account", "Delete Account", "Edit Account"], ["Change Password", "Logout"]]
functions = {
    "11": stu.queryScore,
    "21": stu.showStuInfo,
    "22": stu.stuInfoSort,
    "23": stu.updateStuScore,
    "24": stu.insertStu,
    "25": stu.deleteStu,
    "26": stu.editStuInfo,
    "27": imex.impStu,
    "28": imex.expStu,
    "31": user.showUser,
    "32": user.insertUser,
    "33": user.deleteUser,
    "34": user.editUser,
    "41": user.updateUser
}
enable = []

lock: int = 0
level: int = 0
exit: int = 0

print(F"SEV:{version}  Build on {uptime}")
print("Student Score Management System\n")
print("=========== Welcome ===========\n")

while (True):
    if (exit == 1):
        print("\nSystem Exit")
        time.sleep(1)
        break

    enable.clear()
    cho_f1 = input("Login or Sign up ? Login:1  Sign up:2  Exit:other > ")
    if (cho_f1 == "1"):
        lock = login.login()
        level = login.getLevel()
    elif (cho_f1 == "2"):
        user.insertUser()
        lock = login.login()
        level = login.getLevel()
    else:
        print("\nSystem Exit")
        time.sleep(1)
        break

    if (lock == 1):
        while (True):
            print()
            print("OPERATING INSTRUCTIONS".center(35, "-"))
            if (level > 3):
                level = 3
            for i in range(level):
                num = 0
                for item in operation[i]:
                    num += 1
                    enable.append("".join([str(i + 1), str(num)]))
                    print("".join([item.ljust(30, " "), " : ", str(i + 1), str(num)]))
                print()
            num = 0
            for item in operation[3]:
                num += 1
                enable.append("".join(["4", str(num)]))
                print("".join([item.ljust(30, " "), " : 4", str(num)]))
            print("-" * 35)

            cho_f2 = input("Choose operation > ")
            print()
            if (cho_f2 == "42"):
                break
            elif (cho_f2 not in functions or cho_f2 not in enable):
                print("Operation not exist")
            else:
                functions.get(cho_f2)()

            con = input("Enter 1 to continue other operation; 2 to exit > ")
            if (con == "2"):
                exit = 1
                print()
                break
    else:
        print("\nSystem Exit")
        time.sleep(1)
        break
