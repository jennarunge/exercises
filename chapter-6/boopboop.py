file= open("name.txt", "w") #r+ means it starts at the beginning, a means append/ add to file
stuff=file.read(4)
print(stuff)
file.write("potatoes")
file.close()

line= file.readline()
while line!="":
    line= file.readline()

for line in file.readlines():
    pass