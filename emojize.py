import emoji

message = input("Input: ")
output = emoji.emojize(message, language="alias")
print(f"Output: {output}")