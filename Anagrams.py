"""
* Given two strings check whehter they are anagrams or not.
* Two strings are set to be anagram if they have same characters but in different order.
* For example "STOP" and "TOPS" are set to be anagrams.
* "DORMITORY" and "DIRTY ROOM" are anagram
* but "STOP" and "POSE" are NOT anagrams.
"""
string1="stop"
string2="pose"
if len(string1)== len(string2):
    for i in range(len(string2)):
        if string1[i] not in string2:
            print("not anagrams")
            break
    else:
        print("Anagrams")



