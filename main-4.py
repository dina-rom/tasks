#1.
for i in range(1, 1001):
    if i%17 == 0:
        print(i)

#2.
for i in range(1, 1001):
    if "2" in str(i):
        print(i)

#3.
for i in range(1, 10001):
    if str(i) == str(i)[::-1]:
        print(i)

#4.
new = "the best text"
print(new.count(" "))

#5
vov = ["a", "e", "i", "o", "u", "y"]
input = "newgoodstring"
n = []
for i in input:
    if i.lower() not in vov:
        n.append(i)
ans = "".join(n)
ans

#6
new = "the best string"
for i in new.split():
    if len(i) <= 5:
        print(i)

#7
new = "the best string"
ans = {}
for i in new.split():
    ans[i] = len(i)
ans

#8
ans = []
new = "newgoodstring"
for i in new:
    if not (i in ans):
        ans.append(i)
print(ans)

#9
sqr = lambda x: x * x
lst = [2, 5, 7, 8, 10]
print(list(map(sqr, lst)))

#10
import math
lst = [(1, 1), (2, 3), (5, 3), (2, 8)]
ans = {}
for i in lst:
    if i[1] == 5 * i[0] - 2:
        ans[i] = math.sqrt(math.pow(i[0], 2) + math.pow(i[1], 2))
print(ans)

#11
ans = []
for i in range(2, 28):
    if i%2 == 0:
        ans.append(i*i)
print(ans)

#12
import math
lst = [(1, 1), (2, 3), (5, 3), (2, 8), (1, -11)]
ans = 0
for i in lst:
    if i[0] >= 0 and i[1] >= 0:
        ans = max(ans, math.sqrt(math.pow(i[0], 2) + math.pow(i[1], 2)))
print(ans)

#13
l1 = [1, 2, 3, 5, 8]
l2 = [2, 4, 8, 16, 32]
l = lambda x, y: (x + y, x - y)
print(list(map(l, l1, l2)))

#14
import math
lst = ['43141', '32441', '431', '4154', '43121']
ans = []
for i in lst:
    a = int(math.pow(int(i), 2))
    if a%2 == 0:
        ans.append(a)
ans

#15
inp = """name,Petya,Vasya,Masha,Vova
grade,5,5,8,3
subject,math,language,physics,math
year,1999,2000,1995,1998"""

ans = []
lst = {}
for i in input.split("\n"):
    ln = i.split(",")
    lst[ln[0]] = ln[1:]
for name, grade, subject, year in zip(lst["name"], lst["grade"], lst["subject"], lst["year"]):
    ans.append({"name": name, "grade": grade, "subject": subject, "year": year})
ans

#16
in = [[11.9, 12.2, 12.9],
    [15.3, 15.1, 15.1], 
    [16.3, 16.5, 16.5],
    [17.7, 17.5, 18.1]]
out = [61.2, 61.3, 62.6]   

lst = list(zip(*in))
ans = []
for i in lst:
    ans.append(sum(i))
ans