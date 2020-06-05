import sys
import string


def hadNaVelblouda(s):
    res = ""

    enlarge = False

    for l in s:
        if l == '_':
            enlarge = True
        elif enlarge:
            res += l.upper()
            enlarge = False
        else:
            res += l

    return res


def velbloudNaHada(s):
    res = ""
    for l in s:
        res += '_' + l.lower() if l in string.ascii_uppercase else l

# tento prikaz vyse se da zapsat i takto:
#        if l in string.ascii_uppercase:
#            res += '_' + l.lower()
#        else:
#            res += l

    return res


s = sys.argv[1]
print("Prevod na velblouda:", s, "-->", hadNaVelblouda(s))
print("Prevod na hada:     ", s, "-->", velbloudNaHada(s))

