from PIL import Image

imageResources = Image.open('imageResources.png')
emptySpace = Image.open('emptySpace.png')

inputText = open('inputText.txt')
inputMusic = inputText.readlines()

for i in range(len(inputMusic)):
    inputMusic[i] = inputMusic[i].replace('\n', '')

print(inputMusic)