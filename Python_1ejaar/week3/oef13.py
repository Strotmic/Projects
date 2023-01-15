def swap(x,y):
    woord1 = y[0:2]+x[2:] + ' ' + x[0:2]+y[2:]
    print(woord1)
if __name__ == '__main__':
    swap('abc','xyz')

    