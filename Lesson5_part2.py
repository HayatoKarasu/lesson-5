word = str(input("Введите любое слово на английском: "))

glas = 'aeiou'
gl = 0

b = len(word)

for c in word:
    if c in glas:
        gl += 1
        print(c, end = ' ')

if gl > 0:
    d = b - gl 
    print("В данном слове", gl, "гласных и", d, "согласных")
elif gl == 0:
    print("False")
