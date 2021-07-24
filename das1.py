
def selectword(word):
    if type(word) != str:                               #check type 
        print("This program designed for words")
    elif len(word)%2 == 0:                              #check length word even or odd
        print("It is not possible to determine the center of a word of even length")
    else :
        centerword = len(word)/2                        #decide cneter index
        firstletter = centerword - 1                    #decide previous and next indexs
        afterletter = centerword + 2
        word2 = word[int(firstletter):int(afterletter)] #make a new word
        return word2
def middlestring(s1,s2):
    if len(s1)%2 != 0:                                  #chenck length
        print("for the resulting word to be symmetrical, the length of the first word must be even")
    else :
        end =len(s1)                                    #length string1
        center = end/2                                  #center string1
        word = s1[0:int(center)] + s2 + s1[int(center):int(end)] #male a new word
        return word

word = input("input the word: ") 
print(selectword(word)) #call function
s1 = input("s1:")
s2 = input("s2:")
print(middlestring(s1,s2)) #call function


