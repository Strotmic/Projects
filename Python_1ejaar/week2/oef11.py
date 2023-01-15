def toon_max(a,b,c):
    max = a
    if b>a:
        max=b
    if c>max:
        max=c
    return max

if __name__ == '__main__':
    print(toon_max(10,7,3))