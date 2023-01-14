list1 = [10, 20, 30, 40, 40, 40, 70, 80, 99]
list2 = ['a', 'b', 'c', 'd', 'e', 'f']

def tel_element_binnen_interval(l,s,t):
    if s not in l:
        s=l[0]
    if t not in l:
        t = l[len(l)-1]
    return(len(l[l.index(s):l.index(t)])+1)

if __name__ == '__main__':
    print(tel_element_binnen_interval(list1,40,100))

