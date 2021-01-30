import re
chars = list("abcdefghijklmnopqrstuvwxyz")


def binStringToText(binstring: str):
    binstring = re.sub('[\s+]', '', binstring)
    out = ""
    for i in range(8, len(binstring)+1, 8):
        out += binCharToText(binstring[i-8:i])
    return out


def binCharToText(bin):
    bin = list(bin)
    prefix = str.join("", bin[:3])
    body = bin[3:]
    body.reverse()
    num = 0
    for i in range(len(body)):
        if body[i] == "0":
            continue
        elif body[i] == "1":
            num += pow(2, i)
    if prefix == "010":
        return chars[num - 1].upper()
    elif prefix == "011":
        return chars[num - 1]
    else:
        return chars[num - 1]


print(binStringToText("01110100 01100001 01110011 01101011 01101011 01101001 01101100 01101100 00100000 00101111 01001001 01001101 00100000 01100010 01110010 01100001 01101001 01101110 00101110 01100101 01111000 01100101 00100000 00101111 01000110"))
