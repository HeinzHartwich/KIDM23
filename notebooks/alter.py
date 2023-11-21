# ARRAY -> LIST {mutable, immutable}
alter = [19, 22, 24, 29, 23, 17, 25, 22, 18, 18, 26, 24, 22, 21, 19, 27, 25, 24, 21]

# Iterator
for element in alter:
    print(element)

i = 0
while i < len(alter):
    print(alter[i])
    i = i+1

print(alter[2:5])

alter[2] = 94

print(alter)
