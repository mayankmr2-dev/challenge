marks = "English = 78 Science = 83 Math = 68 History = 65"

# range 97 to 123 - you get all alphabets from a to z
# print(ord("a")) - 97 and ord("z") - 122
marks = marks.lower()
alphabets = [chr(i) for i in range(97, 123)]
alphabets.append(" ")
alphabets.append("=")
print(alphabets)
final = [k for k in marks if k not in alphabets]
print(final)
english = int(final[0]+final[1])
science = int(final[2]+final[3])
math = int(final[4]+final[5])
history = int(final[6]+final[7])
sumOfMarks = english+science+math+history
print("Total", sumOfMarks)
print("Average", sumOfMarks/4)

'''
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '=']
['7', '8', '8', '3', '6', '8', '6', '5']
Total 294
Average 73.5

'''
