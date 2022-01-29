# 判断一个字符串是否为中文
def is_chinese(char) -> bool:
    if (char >= u'\u4e00' and char <= u'\u9fa5'):
        return True
    else:
        return False


# 含中文字符串的格式化对齐操作
def strJust(text: str, width: int, just: str = "left", fill: str = " ") -> str:
    stext = str(text)
    utext = stext.encode("UTF-8")
    cn_count = 0
    for char in utext:
        if (is_chinese(char)):
            cn_count += 2
        else:
            cn_count += 1

    if (just == "left"):
        return stext + fill * (width - cn_count)
    elif (just == "right"):
        return fill * (width - cn_count) + stext
    elif (just == "center"):
        le = ((width - cn_count) // 2)
        ri = width - le
        return le * fill + stext + ri * fill
    else:
        print("Error: Wrong just mode")
