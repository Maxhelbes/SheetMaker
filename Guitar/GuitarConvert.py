from PIL import Image
from Resources.GuitarSheets import sheet

imageResources = Image.open('Guitar/Resources/GuitarResource.jpg')
emptySpace = Image.open('Guitar/Resources/EmptySpace.png')

inputText = open('Guitar/music.txt')
inputMusic = inputText.readlines()

for i in range(len(inputMusic)):
    inputMusic[i] = inputMusic[i].replace('\n', '')

print(inputMusic)

cellWidht = 82
cellHeight = 540

SDVIG = 12

for i in range(1, len(inputMusic)):
    num = sheet[inputMusic[i]] - 0 + SDVIG
    note = imageResources.crop((cellWidht * num, 0, cellWidht * (num+1), cellHeight))
    emptySpace.paste(note, (cellWidht * (i-1), 0))

type = '.png'
way = 'Guitar/Tabs/'
name = way + inputMusic[0] + type
print(name)
emptySpace.save(name)