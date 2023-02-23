words = input("Enter a sentence : \n")

def sort_words(words):
  words_list = words.split("-")
  words_list.sort()
  return "-".join(words_list)

print(sort_words(words))
