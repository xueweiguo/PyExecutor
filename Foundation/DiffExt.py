import difflib


def diff(a, b):
    opcodes = difflib.SequenceMatcher(None, a, b).get_opcodes()
    op_list = []
    for tag, i1, i2, j1, j2 in opcodes:
        print("%7s a[%d:%d] (%s) b[%d:%d] (%s)" % (tag, i1, i2, a[i1:i2], j1, j2, b[j1:j2]))
        if tag != 'equal':
            op_list.append((tag, i1, i2, b[j1:j2]))
    return op_list


def merge(a, op_list):
    cur = 0
    b = []
    for tag, i1, i2, text in op_list:
        print("%7s a[%d:%d] (%s) text (%s)" % (tag, i1, i2, a[i1:i2], text))
        if tag == 'insert':
            b.extend([a[cur:i1], text])
            cur = i2
        elif tag == 'replace':
            b.extend([a[cur:i1], text])
            cur = i2
        elif tag == 'delete':
            b.append(a[cur:i1])
            cur = i2
        else:
            pass
    b.append(a[cur:])
    b = ''.join(b)
    return b

if __name__ == '__main__':
    a = 'This is a test for difflib.'
    b = 'That is a testttt for dlib.'


    print('--------------------------')
    op_list = diff(a,b)
    print('--------------------------')
    print('merge:',merge(a, op_list))
    print('orige:',b)

