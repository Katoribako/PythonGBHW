# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка,  K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем
# слова. Будем считать, что на вход подается только одно слово,
# которое содержит либо только английские, либо только русские буквы.

class WrongNumber(Exception):
    pass


try:
    eng = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JZ',
           10: 'QZ'}
    rus = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ',
           8: 'ШЭЮ',
           10: 'ФЩЪ'}
    answer = abs(int(input("Please choose your language 1 - Eng / 0 - Rus")))
    if answer > 1:
        raise WrongNumber()
except WrongNumber:
    print("Please input 1 or 0")
except ValueError:
    print("Please input 1 or 0")
else:
    user_text = input("Please input a text what you need: ").upper()
    if answer == 1:
        print(f"You have been earned "
              f"{sum([j for i in user_text for j, v in eng.items() if i in v])}"
              f" points")
    else:
        print(f"Вы заработали "
              f"{sum([j for i in user_text for j, v in rus.items() if i in v])}"
              f" очков")
