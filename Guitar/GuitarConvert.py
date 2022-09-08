from PIL import Image
from Guitar.GuitarSheets import sheet

imageResources = Image.open('GuitarResource.jpg')
emptySpace = Image.open('EmptySpace.png')

inputText = open('music.txt')
inputMusic = inputText.readlines()

for i in range(len(inputMusic)):
    inputMusic[i] = inputMusic[i].replace('\n', '')

print(inputMusic)

cellWidht = 82
cellHeight = 540

for i in range(1, len(inputMusic)):
    num = sheet[inputMusic[i]] - 0
    note = imageResources.crop((cellWidht * num, 0, cellWidht * (num+1), cellHeight))
    emptySpace.paste(note, (cellWidht * (i-1), 0))

type = '.png'
way = ''
name = way + inputMusic[0] + type
print(name)
emptySpace.save(name)