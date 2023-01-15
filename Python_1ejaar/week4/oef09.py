import sys
lijst_getallen = [11, 52, 125, -89, 1245]
lijst_woorden = ["jan", "feb", "maa", "apr", "mei"]
def max_en_min_uit_list(x):
    return f'uit {x} is het max {x.sort()[-1]} en het min {x.sort()[0]}'

print(max_en_min_uit_list(lijst_getallen))



