sentence = input("enter a sentence: ")
vowel = 0
consonant = 0
count = 0
word = 0
for i in sentence :
    if i == " ":
        word += 1
        continue;
    count += 1
    if i in "aeiouAEIOU":
        vowel += 1
        continue
    consonant += 1
print("the number of characters in the sentence is:(ignoring spaces )", count)
print("the number of words in the sentence is:", word+1)
print("the number of vowels in the sentence is:", vowel)
print("the number of consonants in the sentence is:", consonant)