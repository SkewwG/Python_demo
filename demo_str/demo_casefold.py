# casefold() 返回小写，与lower()类似，但lower只针对ASCII，casefold()针对Unicode()
'''
casefold(...)
    S.casefold() -> str

    Return a version of S suitable for caseless comparisons.
'''
print(help(str.casefold))
a = 'ASD'
b = a.casefold()
print(b)                                    # b = asd
