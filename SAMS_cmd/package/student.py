import sys
import package.path as path

stuno: list = []
stuname: list = []
student: dict = {}
len: dict = {"sno": 15, "name": 10, "age": 10, "clas": 10, "score": 10, "line": 57}


def queryScore():
    global stuno
    global student
    readStudent()
    while (True):
        sno = input("Query score where student no > ")
        if (checkIn(sno, stuno, "student no", mode="in")):
            stu: Student
            stu = student.get(sno)
            print("\nStudent:{0}  SNO:{1}  Score:{2}\n".format(stu.name, stu.sno, stu.score))
        con = input("Enter 1 to continue; 2 to break > ")
        if (con == "2"):
            print()
            break


def showStuInfo():
    global stuno
    global student
    global len
    readStudent()
    print("STUDENT LIST".center(len.get("line") - 2, "-"))
    print("".join(["SNO".ljust(len.get("sno"), " "), "NAME".ljust(len.get("name"), " "), "AGE".ljust(len.get("age"), " "), "CLASS".ljust(len.get("clas"), " "), "SCORE".rjust(len.get("score"), " ")]))
    print("-" * (len.get("line") - 2))
    num = 0
    for no in stuno:
        num += 1
        stu: Student
        stu = student.get(no)
        print("".join([
            stu.sno.ljust(len.get("sno"), " "),
            strJust(stu.name, len.get("name"), just="left", fill=" "),
            str(stu.age).ljust(len.get("age"), " "),
            strJust(stu.clas, len.get("clas"), just="left", fill=" "),
            str(stu.score).rjust(len.get("score"), " ")
        ]))
    print("-" * (len.get("line") - 2))
    print("Total student population: ", num)


def stuInfoSort():
    global stuno
    global student
    global len
    readStudent()
    while (True):
        b = input("Sorting based on ?  StudentNo:1  Score:2 > ")
        s = input("Sorting as ?  Descending:1  Ascending:2 > ")
        lock: int = 0
        sort: bool = False
        if (b == "1"):
            if (s == "1"):
                sort = True
            elif (s == "2"):
                pass
            else:
                print("Invalid parameter")
                lock == 1
            if (lock == 0):
                print("STUDENT LIST SORTED".center(len.get("line") - 2, "-"))
                print("".join(["SNO".ljust(len.get("sno"), " "), "NAME".ljust(len.get("name"), " "), "AGE".ljust(len.get("age"), " "), "CLASS".ljust(len.get("clas"), " "), "SCORE".rjust(len.get("score"), " ")]))
                print("-" * (len.get("line") - 2))
                s_stuno = sorted(stuno, reverse=sort)
                for sno in s_stuno:
                    stu: Student
                    stu = student.get(sno)
                    print("".join([
                        stu.sno.ljust(len.get("sno"), " "),
                        strJust(stu.name, len.get("name"), just="left", fill=" "),
                        str(stu.age).ljust(len.get("age"), " "),
                        strJust(stu.clas, len.get("clas"), just="left", fill=" "),
                        str(stu.score).rjust(len.get("score"), " ")
                    ]))
                print("-" * (len.get("line") - 2))

        elif (b == "2"):
            if (s == "1"):
                sort = True
            elif (s == "2"):
                pass
            else:
                print("Invalid parameter")
                lock == 1
            if (lock == 0):
                print("STUDENT LIST SORTED".center(len.get("line") - 2, "-"))
                print("".join(["SNO".ljust(len.get("sno"), " "), "NAME".ljust(len.get("name"), " "), "AGE".ljust(len.get("age"), " "), "CLASS".ljust(len.get("clas"), " "), "SCORE".rjust(len.get("score"), " ")]))
                print("-" * (len.get("line") - 2))
                stulist: list
                stulist = student.values()
                sno_score: dict = {}
                score: list = []
                for stu in stulist:
                    sno_score[str(stu.score)] = stu.sno
                    score.append(stu.score)
                s_score = sorted(score, reverse=sort)
                for s in s_score:
                    sno = sno_score.get(str(s))
                    stu: Student
                    stu = student.get(sno)
                    print("".join([
                        stu.sno.ljust(len.get("sno"), " "),
                        strJust(stu.name, len.get("name"), just="left", fill=" "),
                        str(stu.age).ljust(len.get("age"), " "),
                        stu.clas.ljust(len.get("clas"), " "),
                        str(stu.score).rjust(len.get("score"), " ")
                    ]))
                print("-" * (len.get("line") - 2))
        else:
            print("Invalid parameter")
        con = input("Enter 1 to continue; 2 to break > ")
        if (con == "2"):
            print()
            break


def updateStuScore():
    global stuno
    global student
    global len
    readStudent()
    while (True):
        sno = input("Update score where student no > ")
        if (checkIn(sno, stuno, "student no", mode="in")):
            new_score = input("Input new score > ")
            if (checkFormat(new_score, mode="score") and checkLegitimacy(new_score, mode="score")):
                stu: Student
                stu = student.get(sno)
                with open(path.url_student, "r", encoding="UTF-8") as file_stu:
                    read = file_stu.readlines()
                read[stu.line - 1] = "".join(
                    [sno.ljust(len["sno"], " "),
                     strJust(stu.name, len["name"], just="left", fill=" "),
                     str(stu.age).ljust(len["age"], " "),
                     stu.clas.ljust(len["clas"], " "),
                     str(float(new_score)).rjust(len["score"], " "), "\n"])
                with open(path.url_student, "w+", encoding="UTF-8") as file_stu:
                    file_stu.writelines(read)
                    file_stu.flush()
                print("Score update success")
        con = input("Enter 1 to continue; 2 to break > ")
        if (con == "2"):
            print()
            break


def insertStu():
    global stuno
    global len
    while (True):
        loop = [0, 1, 1, 1, 1]
        conti = "1"
        readStudent()
        sno = input("".join(["As format:2022010001".ljust(22, " "), "Input student no     > "]))
        if (checkFormat(sno, mode="sno") and checkLegitimacy(sno, mode="sno") and checkIn(sno, stuno, target="student no", mode="not in")):
            while (loop[1] == 1 and conti == "1"):
                name = input("".join([strJust("As format:张三", 22, just="left", fill=" "), "Input student name   > "]))
                if (checkFormat(name, mode="name") and checkLegitimacy(name, mode="name")):
                    loop[1] = 0
                    while (loop[2] == 1 and conti == "1"):
                        age = input("".join(["As format:18".ljust(22, " "), "Input student age    > "]))
                        if (checkFormat(age, mode="age") and checkLegitimacy(age, mode="age")):
                            loop[2] = 0
                            while (loop[3] == 1 and conti == "1"):
                                clas = input("".join(["As format:SE-22-1".ljust(22, " "), "Input student class  > "]))
                                if (checkFormat(clas, mode="clas") and checkLegitimacy(clas, mode="clas")):
                                    loop[3] = 0
                                    while (loop[4] == 1 and conti == "1"):
                                        score = input("".join(["As format:60.0".ljust(22, " "), "Input student score  > "]))
                                        if (checkFormat(score, mode="score") and checkLegitimacy(score, mode="score")):
                                            loop[4] = 0
                                            write = "".join([
                                                sno.ljust(len["sno"], " "),
                                                strJust(name, len["name"], just="left", fill=" "),
                                                age.ljust(len["age"], " "),
                                                strJust(clas, len["clas"], just="left", fill=" "),
                                                score.rjust(len["score"], " "), "\n"
                                            ])
                                            with open(path.url_student, "a", encoding="UTF-8") as file_stu:
                                                file_stu.write(write)
                                                file_stu.flush()
                                            print("New student insert success")
                                        else:
                                            conti = input("Continue:1  Break:2 > ")
                                else:
                                    conti = input("Continue:1  Break:2 > ")
                        else:
                            conti = input("Continue:1  Break:2 > ")
                else:
                    conti = input("Continue:1  Break:2 > ")
        if (conti == "1"):
            con = input("Enter 1 to continue; 2 to break > ")
            if (con == "2"):
                print()
                break
        else:
            break


def deleteStu():
    global stuno
    global student
    while (True):
        readStudent()
        showStuInfo()
        sno = input("Delete student where student no > ")
        if (checkIn(sno, stuno, target="student no", mode="in")):
            with open(path.url_student, "r", encoding="UTF-8") as file_stu:
                read = file_stu.readlines()
            stu: Student
            stu = student[sno]
            index = stu.line - 1
            read.pop(index)
            with open(path.url_student, "w+", encoding="UTF-8") as file_stu:
                file_stu.writelines(read)
                file_stu.flush()
            print("Student delete success")
        con = input("Enter 1 to continue; 2 to break > ")
        if (con == "2"):
            print()
            break


def editStuInfo():
    global stuno
    global student
    global len
    while (True):
        readStudent()
        showStuInfo()
        sno = input("Edit student infomation where student no > ")
        if (checkIn(sno, stuno, target="student no", mode="in")):
            with open(path.url_student, "r", encoding="UTF-8") as file_stu:
                read = file_stu.readlines()
            target = input("Edit ?  Student No:1  Name:2  Age:3  Class:4  Score:5 > ")
            in_tar: dict = {"1": "sno", "2": "name", "3": "age", "4": "clas", "5": "score"}
            in_nam: dict = {"1": "student no", "2": "name", "3": "age", "4": "class", "5": "score"}
            err = 0
            if (target in in_tar.keys()):
                stu: Student
                stu = student[sno]
                index = stu.line - 1
                text = read[index]
                arr = text.split()
                index_arr = int(target) - 1
                new = input("Input new {0} > ".format(in_nam[target]))
                if (target == "1"):
                    if (checkIn(new, stuno, target=in_nam[target], mode="not in") and checkFormat(new, mode=in_tar[target]) and checkLegitimacy(new, mode=in_tar[target])):
                        arr[index_arr] = new
                    else:
                        err = 1
                else:
                    if (checkFormat(new, mode=in_tar[target]) and checkLegitimacy(new, mode=in_tar[target])):
                        arr[index_arr] = new
                    else:
                        err = 1
            else:
                err = 1
                print("Illegal modification target")

            if (err == 0):
                newline = "".join(
                    [arr[0].ljust(len["sno"], " "),
                     strJust(arr[1], len["name"], just="left", fill=" "), arr[2].ljust(len["age"], " "),
                     strJust(arr[3], len["clas"], just="left", fill=" "), arr[4].rjust(len["score"], " "), "\n"])
                read[index] = newline
                with open(path.url_student, "w+", encoding="UTF-8") as file_stu:
                    file_stu.writelines(read)
                    file_stu.flush()
                print("Student info edit success")
        con = input("Enter 1 to continue; 2 to break > ")
        if (con == "2"):
            print()
            break


class Student:
    sno: str
    name: str
    age: int
    clas: str
    score: float
    line: int

    def __init__(self, sno, name, age, clas, score, line) -> None:
        self.sno = sno
        self.name = name
        self.age = age
        self.clas = clas
        self.score = score
        self.line = line


def readStudent():
    with open(path.url_student, "r", encoding="UTF-8") as file_stu:
        stulist = file_stu.readlines()
    global stuno
    global stuname
    global student
    student.clear()
    stuno.clear()
    stuname.clear()
    line = 0
    try:
        for item in stulist:
            line += 1
            arr = item.split()
            stuno.append(arr[0])
            stuname.append(arr[1])
            student[arr[0]] = Student(arr[0], arr[1], int(arr[2]), arr[3], float(arr[4]), line)
    except Exception as e:
        print("Error: Student file damaged")
        sys.exit()


def is_chinese(char) -> bool:
    if (char >= u'\u4e00' and char <= u'\u9fa5'):
        return True
    else:
        return False


def strJust(text, width: int, just: str = "left", fill: str = " ") -> str:
    text = str(text)
    cn_count = 0
    for char in text:
        if (is_chinese(char)):
            cn_count += 2
        else:
            cn_count += 1

    if (just == "left"):
        return text + fill * (width - cn_count)
    elif (just == "right"):
        return fill * (width - cn_count) + text
    elif (just == "center"):
        le = ((width - cn_count) // 2)
        ri = width - le
        return le * fill + text + ri * fill
    else:
        print("Error: Wrong just mode")


def checkFormat(text: str, mode: str) -> bool:
    if (mode == "sno"):
        length = 10
        target = "Student No"
    elif (mode == "name"):
        length = 8
        target = "Name"
    elif (mode == "age"):
        length = 3
        target = "Age"
    elif (mode == "clas"):
        length = 10
        target = "Class"
    elif (mode == "score"):
        length = 6
        target = "Score"
    else:
        print("Error: Mode invalid")
        return False

    if (text != ""):
        if (text.find(" ") == -1):
            cn_count: int = 0
            for char in text:
                if (is_chinese(char)):
                    cn_count += 2
                else:
                    cn_count += 1
            if (cn_count <= length):
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


def checkLegitimacy(text: str, mode: str) -> bool:
    if (mode == "sno"):
        if (text.isdecimal()):
            return True
        else:
            print("Student No can contain only digital")
            return False
    elif (mode == "name"):
        err = 0
        for char in text:
            if (is_chinese(char) or char.isalpha()):
                pass
            else:
                err = 1
        if (err == 0):
            return True
        else:
            print("Name can contain only Chinese and English alphabet")
            return False
    elif (mode == "age"):
        if (text.isdecimal()):
            return True
        else:
            print("Age can contain only digital")
            return False
    elif (mode == "clas"):
        err = 0
        for char in text:
            if (char == "-" or char.isalnum()):
                pass
            else:
                err = 1
        if (err == 0):
            return True
        else:
            print("Class can contain only English alphabet or (-) like \"SE-22-1\"")
            return False
    elif (mode == "score"):
        err = 0
        for char in text:
            if (char.isdecimal() or char == "."):
                pass
            else:
                err = 1
        if (err == 0):
            return True
        else:
            print("Score can contain only float")
            return False
    else:
        print("Error: Illegal mode")
        return False


def checkIn(strin: str, listin: list, target: str, mode: str = "in") -> bool:
    if (mode == "in"):
        if (strin in listin):
            return True
        else:
            print(" ".join([target.title(), "not exist"]))
            return False
    elif (mode == "not in"):
        if (strin not in listin):
            return True
        else:
            print(" ".join([target.title(), "already exists"]))
            return False
    else:
        print("Error: Mode invalid")
        return False
