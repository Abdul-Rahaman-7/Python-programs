# finding vowels and consonants

str1 = input("Enter: ")
str2 = "aAeEIIoOuU"

v=0
c=0

for i in str1 :
    if i in str2:
        v +=1
    else:
        c +=1

print(f"Nuber of vowels are {v}")
print(f"Nuber of consonants are {c}")            
