def is_schrikkeljaar(i):
        if i %4==0 and i %100!=0:
            return True

if __name__ == '__main__':
    start = int(input('Startjaar: '))
    stop = int(input('Stopjaar: '))
    for i in range(start, stop+1):
        if is_schrikkeljaar(i) == True: print(i)

