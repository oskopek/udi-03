st = 'This is just a string!'
stlen = len(st)
st2 = [''] * stlen
i = 0

while i < stlen:
    st2[i] = st[stlen-i-1]
    i += 1
print(''.join(st2))

