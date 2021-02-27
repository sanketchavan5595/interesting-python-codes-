import os
path = 'D:\Cartoon Series\Avater- The Last Airbender\Season 1' # paste your path here

files = os.listdir(path)


for file in files:
    print(file)


# for renaming files

i = 1
for file in files:
   os.rename(os.path.join(path, file), os.path.join(path, "Avater-The Last Air Bender Season " + str(i)))
   i = i + 1
print(os.listdir(path))
