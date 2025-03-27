import csv


with open('data.csv', 'r', encoding='utf8') as file:
    reader = csv.reader(file)
    list = []
    list.append(next(reader))

    for x in reader:
        languages = x[4]
        languages = languages.split(',')
        for i, language in enumerate(languages):
            new_language = language.replace("<strong>*</strong><br><strong>*</strong>languages with full audio support", "")
            new_language = new_language.replace("<br><strong>*</strong>languages with full audio support", "")
            new_language = new_language.replace("<strong>*</strong>", "")
            new_language = new_language.replace("<strong>", "")
            new_language = new_language.replace("</strong>", "")
            new_language = new_language.replace("<br>", "")
            languages[i] = new_language.strip()
        x[4] = languages
        list.append(x)

with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(list)
