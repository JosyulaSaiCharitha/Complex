"""
*Given a list of Strings, and an external order in which it needs to be sorted, Sort the given list of *strings.
*
*For example:
*Input Strings : "Ajay", "Raja", "Keshav", "List", "Set", "Elephant", "Drone",
*Sort order:TESARDLK
*Sorted Strings: "Elephant", "Set","Ajay", "Raja", "Drone","List","Keshav"
"""
strings= "Ajay", "Raja", "Keshav", "List", "Set", "Elephant", "Drone"
order = "TESARDLK"

for i in order:
    for j in range(len(strings)):
        if strings[j][0] == i:
            print(strings[j], end=", ")
