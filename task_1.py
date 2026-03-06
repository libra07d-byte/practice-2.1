import csv
with open('text.txt','w') as file:
    txt = [
        ["Адский хардкор."],
        ["Необходима разработка баз данных для 1С."],
        ["Камень я не дам."],
        ["Где деньги взять? давно известно..."],
        ["Тут ничего нет."]
    ]
    writer = csv.writer(file)
    writer.writerows(txt)


with open('text.txt','r') as file:
    content = file.readlines()
    num_lines = len(content)
    words = sum(len(line.split()) for line in content)
    longest_words = max(content,key = len).strip() if content else None

print(f'Количество сторк:{num_lines}')
print(f'Количество слов:{words}')
print(f'Самая длинная строка:{longest_words}')
