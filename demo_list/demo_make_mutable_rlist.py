# 函数时列表
def to_mutable_rlist(source):
    """Return a functional list with the same contents as source."""
    s = make_mutable_rlist()
    for element in reversed(source):
        s('push_first', element)
    return s

def make_mutable_rlist():
    """Return a functional implementation of a mutable recursive list."""
    contents = []

    def dispatch(message, value=None):
        nonlocal contents
        if message == 'len':
            return len_rlist(contents)
        elif message == 'getitem':
            return getitem_rlist(contents, value)
        elif message == 'push_first':
            contents = make_rlist(value, contents)
        elif message == 'pop_first':
            f = first(contents)
            contents = rest(contents)
            return f
        elif message == 'str':
            return str(contents)

    return dispatch

suits = ['coin', 'string', 'myriad']
s = to_mutable_rlist(suits)
s('str')
