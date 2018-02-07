
'''
maketrans(x, y=None, z=None, /)
    Return a translation table usable for str.translate().

    If there is only one argument, it must be a dictionary mapping Unicode
    ordinals (integers) or characters to Unicode ordinals, strings or None.
    Character keys will be then converted to ordinals.
    If there are two arguments, they must be strings of equal length, and
    in the resulting dictionary, each character in x will be mapped to the
    character at the same position in y. If there is a third argument, it
    must be a string, whose characters will be mapped to None in the result.
'''
print(help(str.maketrans))
from string import maketrans
suchas = maketrans('sm','@$')
s = 'this is sam\'s dog'
print(s)
"this is sam's dog"
print(s.translate(suchas))
"thi@ i@ @a$'@ dog"
print(s.translate(suchas,"dog")) #去除d,o,g字符
"thi@ i@ @a$'@ "