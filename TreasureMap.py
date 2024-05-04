line1=['','','']
line2=['','','']
line3=['','','']
map=[line1,line2,line3]
position=input("Enter the index of the treasure: ")
Letter=position[0].lower()
abc=['a','b','c'] 
indexLetter=abc.index(Letter)
indexNumber=int(position[1])-1
map[indexNumber][indexLetter]='X'
print(f"{line1}\n{line2}\n{line3}")