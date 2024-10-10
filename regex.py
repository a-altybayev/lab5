import re
with open(r"row.txt", 'r', encoding='utf-8') as file:
    content = file.readlines()
a = ''.join(content)
#task1
tx = re.compile("a{1}b*")
m = tx.findall(a)
print(m)

#task2
tx = re.compile("a{1}b{2,3}")
m = tx.findall(a)
print(m)

#task3
tx = re.compile("[a-z]*_[a-z]*")
m = tx.findall(a)
print(m)

#task4
tx = re.compile("[A-Z][a-z]+")
m = tx.findall(a)
print(m)

#task5
tx = re.compile("a\w.+b")
m = tx.findall(a)
print(m)

#task6
a = ''.join(str)
tx = re.sub('[ ,.]', ':', a)
print(tx)

#task7
tx = re.sub('_',' ', a)
tx = tx.title()
tx = re.sub(' ', '', tx)
print(tx)

#task8
tx = re.findall(r"[A-Z][a-z]*", a)
print(tx)

#task9
tx = re.sub(r"(\w)([A-Z])", r"\1 \2 ", a)
print(tx)

#task10
tx = re.sub('(.)([A-Z][a-z]+)', r'\1_\2 ', a)
tx = tx.lower()
tx = re.sub('([a-z0-9])([A-Z])', r'\1_\2', tx)
print(tx)