sentence = input("enter a sentence: ")
space = 0
if len(sentence)==0:
    print("you entered an empty string")
else:
    print("the length of the sentence is:", len(sentence))
    print("the first character is:",sentence[0])
    print("the last character is:",sentence[-1])
    print("reverse of the string is:",sentence[::-1])
    print("the sliced version of string is (every second character)")
    print(sentence[::2])
    for i in sentence:
        if i == " ":
            space+=1
    print("the number of spaces in the string is:", space)
            