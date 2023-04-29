text = input("Paste in your text to see word and sentence count. \n\n")

words = text.split(" ")

print(f"Your word count is {len(words)} words.")

sentences = text.split(".")

print(f"Your sentence count is {len(sentences)} sentences.")