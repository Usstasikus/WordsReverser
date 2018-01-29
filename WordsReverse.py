def reverse(text):
    a = 0
    b = 0
    limit = len(text)
    while a < limit: # пока есть, что читать
        while text[a] == ' ': # ищем начало слова
            a += 1
            if a >= limit: # если больше не осталось слов
                return     # завершаем работу функции

        b = a
        while text[b] != ' ': # ищем конец слова
            b += 1
            if b >= limit: # если достигли конца текста
                break      # выходим из цикла
        print(text[b-1:a:-1] + text[a]) # выводим реверсированное слово
        a = b


with open("input.txt") as f:
    text = " ".join(line.strip() for line in f.readlines())
    reverse(text)