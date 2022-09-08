from PIL import Image
from FluteSheets import sheet


tabs = Image.open('FluteResource.png')
baza = Image.open('Empty.png')

get = open('music.txt')

music = get.readlines()

for i in range(len(music)):
    music[i] = music[i].replace('\n', '')

print(music)

SDVIG = 0 # в полутонах.

for i in range(1, len(music)):
    num = sheet[music[i]] - SDVIG
    note = tabs.crop((24 * num, 0, 24 * (num+1), 288))
    baza.paste(note, (24 * (i - 1), 0))

#baza.show()
tip = '.png'
way = 'Tabs/'
name = way + music[0] + tip
print(name)
baza.save(name)
