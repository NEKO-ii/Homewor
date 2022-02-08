import pandas as pd
import package.path as path
import package.student as student
import package.encrypt as encrypt
import traceback
import os
import time

impath = path.path_import
expath = path.path_export
len: dict = {"sno": 15, "name": 10, "age": 10, "clas": 10, "score": 10, "line": 57}


def impStu():
    file: str
    xlsfilelist: list = []
    while (True):
        con_f0 = False
        cho_f1 = input("Use default file directory or other?  Default:1  Other:2  Break:3 > ")
        if (cho_f1 == "1"):
            xlsfilelist = []
            filelist = os.listdir(impath)
            print("Current file list:\n==============================")
            if (filelist):
                for filename in filelist:
                    extname = os.path.splitext(filename)[1]
                    if (extname == ".xls" or extname == ".xlsx"):
                        xlsfilelist.append(filename)
                        print(filename)
            else:
                print("Empty")
            print("==============================")

            filename = input("Choose import file > ")
            if (filename in xlsfilelist):
                file = "\\".join([impath, filename])
                con_f0 = True
            else:
                print("File not found")

        elif (cho_f1 == "2"):
            url = input("Input a path > ")
            xlsfilelist = []
            if (os.path.exists(url)):
                if (os.path.isfile(url)):
                    extname = os.path.splitext(os.path.basename(url))[1]
                    if (extname == ".xls" or extname == ".xlsx"):
                        file = url
                        con_f0 = True
                        print("The incoming file is confirmed")
                else:
                    filelist = os.listdir(url)
                    print("Current file list:\n==============================")
                    if (filelist):
                        for filename in filelist:
                            extname = os.path.splitext(filename)[1]
                            if (extname == ".xls" or extname == ".xlsx"):
                                xlsfilelist.append(filename)
                                print(filename)
                    else:
                        print("Empty")
                    print("==============================")

                    filename = input("Choose import file > ")
                    if (filename in xlsfilelist):
                        file = "\\".join([impath, filename])
                        con_f0 = True
                    else:
                        print("File not found")
            else:
                print("The file path does not exist")

        elif (cho_f1 == "3"):
            break
        else:
            print("Instruction does not exist")

        if (con_f0 is True):
            try:
                data = pd.read_excel(file, header=0)
                print("Run file detection...\n")
                cfre = checkFile(data)
                con = 1
                if (cfre[1]):
                    conf = input("\nSkip the wrong line and continue the import operation?  Yse:1 No:2 > ")
                else:
                    print("No Err\n")
                    conf = input("Confirm the import operation?  Yse:1 No:2 > ")
                if (conf == "2"):
                    con = 2

                if (con == 1):
                    row = 1
                    write: list = []
                    print("STUDENT INFO IMPORT LIST".center(55, "-"))
                    for item in data.values:
                        row += 1
                        if (row not in cfre[1]):
                            temp = "".join([
                                str(item[0]).split(".")[0].ljust(len["sno"], " "),
                                student.strJust(item[1], len["name"], just="left", fill=" "),
                                str(item[2]).split(".")[0].ljust(len["age"], " "),
                                student.strJust(str(item[3]).split(".")[0], len["clas"], just="left", fill=" "),
                                str(item[4]).rjust(len["score"], " "), "\n"
                            ])
                            print(temp, end="")
                            write.append(encrypt.ency(temp))
                    print("-" * 55)
                    if (write):
                        with open(path.url_student, "a", encoding="UTF-8") as file_stu:
                            file_stu.writelines(write)
                            file_stu.flush()
                        print("Student info import success")
                    else:
                        print("No Student info import")

            except Exception as e:
                print("The format of the imported file is incorrect\nERR MSG:")
                print(e)
                # traceback.print_exc()
                print()


def expStu():
    expfunlist = ["Export All Student Info", "Set Export Score Range", "Export By Student No.", "Break Export"]
    student.readStudent()
    studict = student.student
    stunolist = student.stuno
    lock = True
    while (lock):
        conlock = False
        funkey: list = []
        expstuno: list = []
        print("-" * 34)
        for i in range(expfunlist.__len__()):
            fun = expfunlist[i].ljust(30, " ")
            funkey.append(str(i + 1))
            print(F"{fun} : {i+1}")
        print("-" * 34)
        cho = input("Select the Export method > ")
        if (cho in funkey):
            if (cho == "1"):
                expstuno = stunolist
                conlock = True
            elif (cho == "2"):
                inp = input("Enter the range As 60-70; -60; 70-; 60 > ")
                fd = inp.find("-")
                rfd = inp.rfind("-")
                if (fd != rfd):
                    print("Incorrect input format: Too much '-'")
                elif (fd == -1):
                    try:
                        score = float(inp)
                        stu: student.Student
                        for sno in stunolist:
                            stu = studict[sno]
                            if (stu.score == score):
                                expstuno.append(sno)
                        conlock = True
                    except:
                        print("Incorrect input value: Input non-digital")
                else:
                    inparr = inp.split("-")
                    try:
                        if (fd == 0):
                            max = float(inparr[1])
                            min = 0.0
                        elif (fd == inp.__len__() - 1):
                            min = float(inparr[0])
                            max = 100.0
                        else:
                            in1 = float(inparr[0])
                            in2 = float(inparr[1])
                            if (in1 > in2):
                                max = in1
                                min = in2
                            elif (in1 < in2):
                                max = in2
                                min = in1
                            else:
                                max = min = in1
                        stu: student.Student
                        for sno in stunolist:
                            stu = studict[sno]
                            if (min <= stu.score and stu.score <= max):
                                expstuno.append(sno)
                        conlock = True
                    except:
                        print("Incorrect input value: Input non-digital")
            elif (cho == "3"):
                print("If there are more than one need to export please use space to separate")
                inp = input("Enter the student no. > ")
                inparr = inp.split()
                nesno: list = []
                for item in inparr:
                    if (item in stunolist):
                        expstuno.append(item)
                    else:
                        nesno.append(item)
                if (nesno):
                    print("Wrong input list:", nesno)
                conlock = True
            elif (cho == "4"):
                print()
                break
        else:
            print("Method not exist")

        if (conlock):
            if (expstuno):
                write: list = []
                columns: list = ["SNO", "Name", "Age", "Class", "Score"]
                stu: student.Student
                for sno in expstuno:
                    line: list = []
                    stu = studict[sno]
                    line.append(stu.sno)
                    line.append(stu.name)
                    line.append(stu.age)
                    line.append(stu.clas)
                    line.append(stu.score)
                    write.append(line)
                data = pd.DataFrame(write, columns=columns)

                print("Export Info:")
                print("-" * 55)
                for item in write:
                    temp = "".join([
                        str(item[0]).split(".")[0].ljust(len["sno"], " "),
                        student.strJust(item[1], len["name"], just="left", fill=" "),
                        str(item[2]).split(".")[0].ljust(len["age"], " "),
                        student.strJust(str(item[3]).split(".")[0], len["clas"], just="left", fill=" "),
                        str(item[4]).rjust(len["score"], " ")
                    ])
                    print(temp)
                print("-" * 55)

                conlock3 = True
                con = input("Confirm the export?  Yes:1 No:2 > ")
                if (con == "2"):
                    conlock3 = False
                while (conlock3):
                    print("Enter null will use the default file name; The input file can include an extension name '.xls' or '.xlsx'")
                    name = input("Enter the name of the exported file > ")
                    conlock2 = True
                    if (name == ""):
                        name = ".".join([time.strftime("%Y%m%d%H%M%S"), "xlsx"])
                        url = "\\".join([expath, name])
                    else:
                        namearr = os.path.splitext(name)
                        if (namearr[1] == ""):
                            name = ".".join([name, "xlsx"])
                            url = "\\".join([expath, name])
                        elif (namearr[1] == ".xls" or namearr[1] == ".xlsx"):
                            url = "\\".join([expath, name])
                        else:
                            print("The file extension name is incorrect")
                            conlock2 = False

                    if (conlock2):
                        if (os.path.isfile(url)):
                            print(F"File {name} aready exist")
                            print(F"Location: {url}")
                        else:
                            data.to_excel(url, index=0)
                            print("Student Info export success")
                            print(F"File Location: {url}")
                            break

                    con = input("Enter 1 to rename; 2 to break > ")
                    if (con == "2"):
                        lock = False
                        break
            else:
                print("No student information was found")

        con = input("Enter 1 to continue; 2 to break > ")
        if (con == "2"):
            print()
            break


def checkFile(data: pd.DataFrame) -> list:
    student.readStudent()
    stuno = student.stuno
    snoinxls: dict = {}
    snorepeat: list = []
    inerr: list = []
    formaterr: list = []
    legitimacyerr: list = []
    linewitherr: list = []
    returnlist: list = [True, linewitherr]

    line = 1
    for item in data.values:
        line += 1
        correct = True
        inre = checkIn(item, stuno, line)
        fore = checkFormat(item, line)
        lere = checkLegitimacy(item, line)
        if (inre[0] is False):
            inerr.append(inre[1])
            correct = False
        else:
            pass
        if (fore[0] is False):
            for err in fore[1]:
                if (err != ""):
                    formaterr.append(err)
            correct = False
        if (lere[0] is False):
            for err in lere[1]:
                if (err != ""):
                    legitimacyerr.append(err)
            correct = False
        if (correct):
            if (inre[2] in snoinxls):
                l: list
                l = snoinxls[inre[2]]
                l.append(line)
                if (inre[2] not in snorepeat):
                    snorepeat.append(inre[2])
                returnlist[0] = False
                linewitherr.append(line)
            else:
                l: list = [line]
                snoinxls[inre[2]] = l
        else:
            returnlist[0] = False
            linewitherr.append(line)

    if (inerr):
        print("===== SNO EXIST ERR =====")
        for item in inerr:
            print(item)
        print()
    if (formaterr):
        print("====== FORMAT ERR =======")
        for item in formaterr:
            print(item)
        print()
    if (legitimacyerr):
        print("==== LEGITIMACY ERR =====")
        for item in legitimacyerr:
            print(item)
        print()
    if (snorepeat):
        print("==== SNO REPEAT ERR =====")
        print("Duplicate student numbers exist in correct lines in XLS files")
        for rsno in snorepeat:
            print(F"Repeat SNO: {rsno}  On these lines: {snoinxls[rsno]}")
        print("----------------------------------------------------------------------------------------------")
        print("Attention: Information with duplicate student numbers will only be imported from the first one")
        print("----------------------------------------------------------------------------------------------\n")
    if (linewitherr):
        print("Error Rows Exist:", linewitherr, "   Total:", linewitherr.__len__())
    return returnlist


def checkFormat(lst: list, line: int) -> list:
    length: list = [10, 8, 3, 10, 6]
    target: list = ["Student No", "Name", "Age", "Class", "Score"]
    col: list = ["A", "B", "C", "D", "E"]
    formaterr: list = ["", "", "", "", ""]
    returnlist: list = [True, formaterr]

    loc = -1
    for item in lst:
        text = str(item)
        loc += 1
        if (loc == 0 or loc == 2 or loc == 3):
            text = text.split(".")[0]
        if (text != "nan"):
            if (text.find(" ") == -1):
                cn_count: int = 0
                for char in text:
                    if (student.is_chinese(char)):
                        cn_count += 2
                    else:
                        cn_count += 1
                if (cn_count <= length[loc]):
                    pass
                else:
                    formaterr[loc] = F"Location: {col[loc]}{line} -- {target[loc]} too long, MAX: {str(length[loc])}"
                    returnlist[0] = False
            else:
                formaterr[loc] = F"Location: {col[loc]}{line} -- {target[loc]} Cannot contain Spaces"
                returnlist[0] = False
        else:
            formaterr[loc] = F"Location: {col[loc]}{line} -- {target[loc]} cannot be empty"
            returnlist[0] = False

    return returnlist


def checkLegitimacy(lst: list, line: int) -> list:
    modelist: list = ["sno", "name", "age", "clas", "score"]
    col: list = ["A", "B", "C", "D", "E"]
    legitimacyerr: list = ["", "", "", "", ""]
    returnlist: list = [True, legitimacyerr]

    loc = -1
    for item in lst:
        text = str(item)
        loc += 1
        if (loc == 0 or loc == 2 or loc == 3):
            text = text.split(".")[0]
        mode = modelist[loc]
        if (mode == "sno"):
            if (text.isdecimal()):
                pass
            else:
                legitimacyerr[loc] = F"Location: {col[loc]}{line} -- Student No can contain only digital"
                returnlist[0] = False
        elif (mode == "name"):
            err = 0
            for char in text:
                if (student.is_chinese(char) or char.isalpha()):
                    pass
                else:
                    err = 1
            if (err == 0):
                pass
            else:
                legitimacyerr[loc] = F"Location: {col[loc]}{line} -- Name can contain only Chinese and English alphabet"
                returnlist[0] = False
        elif (mode == "age"):
            if (text.isdecimal()):
                pass
            else:
                legitimacyerr[loc] = F"Location: {col[loc]}{line} -- Age can contain only digital"
                returnlist[0] = False
        elif (mode == "clas"):
            err = 0
            for char in text:
                if (char == "-" or char.isalnum()):
                    pass
                else:
                    err = 1
            if (err == 0):
                pass
            else:
                legitimacyerr[loc] = F"Location: {col[loc]}{line} -- Class can contain only English alphabet or (-) like \"SE-22-1\""
                returnlist[0] = False
        elif (mode == "score"):
            try:
                float(text)
            except:
                legitimacyerr[loc] = F"Location: {col[loc]}{line} -- Score can contain only float"
                returnlist[0] = False

    return returnlist


def checkIn(lst: list, snolist: list, line: int) -> list:
    sno = str(lst[0]).split(".")[0]
    returnlist: list = [True, "", sno]
    if (sno not in snolist):
        pass
    else:
        returnlist[1] = F"Location: A{line} -- Student No. already exists"
        returnlist[0] = False
    return returnlist
