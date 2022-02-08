from cryptography.fernet import Fernet

key = "HwYgbOonyJb7h85qA-AJnGXYQUnCsg3qH_XHXA7ToOI="
fern: Fernet


def initFernet():
    global fern
    fern = Fernet(key)


def ency(text: str) -> str:
    global fern
    utext = text.encode(encoding="UTF-8")
    cy_text = fern.encrypt(utext)
    return cy_text.decode(encoding="UTF-8") + "\n"


def decy(text_in: str) -> str:
    global fern
    s_btext = text_in.split("\n")[0]
    btext = bytes(s_btext.encode(encoding="UTF-8"))
    de_text = fern.decrypt(btext)
    text = de_text.decode(encoding="UTF-8")
    return text
