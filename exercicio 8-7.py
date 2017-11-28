def mdc(a,b):
    if b == 0:
        return a
    return mdc(b, a % b)

print("MDC 10 e 5 --> %d" % mdc(10,5))
print("MDC 32 e 24 --> %d" % mdc(32,24))
print("MDC 5 e 3 --> %d" % mdc(5,3))
