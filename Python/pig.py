original= raw_input("Enter the sentence here:")
words=original.split()
new_words=[]
for x in words:
    if x[0] in 'aeiou':
        newword=x+'yay'
        new_words.append(newword)
    else:
        vowel_pos= 0
        for letter in x:
            if letter not in "aeiou":
                 vowel_pos +=1
            else:
                break
            cons=x[:vowel_pos]
            rest_word=x[vowel_pos:]
            new_word=rest_word + cons + 'ay'
            new_words.append(new_word)

output = " ".join(new_words)
print output
        
            
