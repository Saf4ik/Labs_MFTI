# # Упражнение №2
# # Вывести на экран все элементы множества A, которых нет в множестве B.
#
# A = set('bqlpzlkwehrlulsdhfliuywemrlkjhsdlfjhlzxcovt')
# B = set('zmxcvnboaiyerjhbziuxdytvasenbriutsdvinjhgik')
# for x in A:
#     if x not in B:
#         print(x)
#
# # COMPLETE



# # Упражнение №3
# # Даны четыре множества:
# #
# # A = set('0123456789')
# # B = set('02468')
# # C = set('12345')
# # D = set('56789')
# # Найти элементы, принадлежащие множеству E:
#
#
# A = set('0123456789')
# B = set('02468')
# C = set('12345')
# D = set('56789')
#
# print(((A-B) & (C-D)) | ((D-A) & (B-C)))
#
# #COMPLETE


# import string
# import operator
#
# def parse(text):
#     s = ''
#     for char in text:
#         if char not in string.punctuation and char != '\n':
#             s += char
#     res = []
#     for i in s.split(' '):
#         res.append(i)
#     return res
#
# def count_words(res):
#     stat = {}
#     for i in res:
#         if i in stat:
#             stat[i] += 1
#         else:
#             stat[i] = 1
#     return stat
#
#
# def sort_by_values(dictionary):
#     return sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)
#
#
# with open('license.txt') as f:
#     text = sort_by_values(count_words(parse(f.read().lower())))
#
# for i in text[:10]:
#     print(i)
#
# # COMPLETE

# import string
#
#
# def parse_words(text:str):
#     res = []
#     for i in text.split('\n'):
#         res.append(i.split('\t-\t'))
#     return res
#
# def create_dict(list):
#     dict = {}
#     for i in list:
#         dict[i[0]] = i[1]
#     return dict
#
#
# def translate(text:str):
#     trans_text = ''
#     for row in text.lower().split('\n'):
#         for word in row.split(' '):
#             if word in d.keys():
#                 trans_text += ''.join(d[word]) + ' '
#             else:
#                 trans_text += ''.join(word) + ' '
#     with open('output.txt', 'w') as f:
#         f.write(trans_text)
#
#
# with open('EN-RU.txt') as f:
#     d = create_dict(parse_words(f.read()))
# print(d)
#
# with open('input.txt') as f:
#     s = translate(f.read())
#
# #COMPLETE


# Упражнение №6. Страны и Языки
# Дан список стран и языков на которых говорят в этой стране в формате <Название Страны> : <язык1> <язык2> <язык3>
# в файле task5/input.txt. На ввод задается N - длина списка и список языков.
# Для каждого языка укажите, в каких странах на нем говорят.
#
# Ввод	Вывод
# 3
# азербайджанский	Азербайджан
# греческий	Кипр Греция
# китайский	Китай Сингапур



def parse_words(text:str):
    res = []
    for i in text.split('\n'):
        res.append(i.split(' : '))
    return res


def create_dict(list):
    dict = {}
    for i in list:
        dict[i[0]] = i[1]
    return dict


with open('country-lang.txt') as f:
    d = create_dict(parse_words(f.read()))


def get_key(value,d=d):
    values = []
    for k, v in d.items():
        if value in v:
             values.append(k)
    return values

# value = 'греческий'
# res = get_key(value)
# print(res)

N = int(input("Введите длину списка: "))
Languages = []
for i in range(N):
    Languages.append(input(f'Введите язык № {i+1}: '))

for i in Languages:
    print(*get_key(i))


#COMPLETED