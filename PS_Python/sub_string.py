string = "abcd"

# pk = [string[i:j] for i in range(len(string)) for j in range(i+1, len(string)+1)]
# print(pk)
for i in range(len(string)):
    for j in range(i+1, len(string)+1):
        print(string[i:j])
