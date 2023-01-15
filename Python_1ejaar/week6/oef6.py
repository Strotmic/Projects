# ENKEL MCT!
# Gebruik bestand in doc/morsevertaling.txt
import re
mor_dic = {}
f = open('doc/morse_vertaling.txt')

def inlezen_morse_bestand(doc):
    x = doc.readlines()
    for i in range(1,len(x)):
        key = x[i].split(';')
        value = re.sub('\n','',key[1])
        mor_dic[key[0]]=value
    return mor_dic
    
def vertaal_letter(s,d):
    if s in d:
        return(d[s])
    else:
        return '?'
        
def vertaal_tekst(s,d):
    s = [*s]
    ret =''
    for i in s:
        ret += vertaal_letter(i,d)
    return ret


(inlezen_morse_bestand(f))
print(vertaal_letter('z',mor_dic))
print(vertaal_tekst('sos',mor_dic))
