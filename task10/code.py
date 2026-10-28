# Case Study 35: Text Compression

text = input("Enter a string: ")

compressed = ""
count = 1

for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        count += 1
    else:
        compressed += text[i - 1] + str(count)
        count = 1

if len(text) > 0:
    compressed += text[-1] + str(count)

print("Original String:", text)
print("Original Length:", len(text))
print("Compressed String:", compressed)
print("Compressed Length:", len(compressed))

if len(compressed) < len(text):
    print("Compression is beneficial")
else:
    print("Compression is not beneficial")
    print("Final String:", text)
