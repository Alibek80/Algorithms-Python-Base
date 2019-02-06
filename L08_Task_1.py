# Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.


def rabin_karp(s, subs):
    len_sub = len(subs)
    h_sub = hash(subs)
    # print(h_sub)

    for i in range(len(s) - len_sub + 1):
        if h_sub == hash(s[i:i + len_sub]):
            return i
    # return -1


#string_1 = open("war-and-peace.txt", 'r')
#string_1 = string_1.read()

string_1 = "qwertyuiopasdfghjklzxcvbnm"
string_1 = string_1.lower()

N = len(string_1)
substr = []
for i in range(N-1):
    for j in range(i, N):
        substr.append(string_1[i:j])

print(substr)
#print(len(substr))

substr = set(substr)

num = []
for i in substr:
    num.append(rabin_karp(string_1, i))

print(len(num))