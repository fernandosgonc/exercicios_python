min = 0
max = 0
for num in [-1, 5, 89, 43, 12, -9]:
    if(num > max):
        max = num
    if(num < min):
        min = num

print('*****\n', 'Max: ', max, '\nMin: ', min)

print('---------------')
str = 'fernando'
for char in str:
    print(char)

index = -1
while(index>=len(str)*-1):
    print(str[index])
    index -= 1

fruta = 'fruta'
print(fruta[:])

def contagem(str, letra):
    count = 0
    for char in str:
        if char == letra:
            count += 1
    return count

print("teste de função")
print(contagem('1589428846', '8'))