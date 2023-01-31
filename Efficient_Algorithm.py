# kavan qu zi jing, 224545C, BA2201

from timeit import default_timer as timer

start = timer()
def sum_of_2numbers(list, z):
    x = 0                   # the beginning index the start of the list
    y = len(list) - 1         # the last index the end of the list
    while list[x] < list[y]:
        if list[x] + list[y] == z:
            return (list[x], list[y],True)
        elif list[x] + list[y] > z:
            y -= 1
        else:
            x += 1
    return ("Not found","Not found",False)

list = [2, 3, 5, 7, 8, 10, 15, 16, 23,28]
z = 15
result = sum_of_2numbers(list, z)
print("x =" ,result[0])
print("y =", result[1])
print(result[2])

end = timer()
cal = (end - start) * 1000
print(cal, 'milliseconds')
