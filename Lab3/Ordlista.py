# Common functions for dictionary program
def wordtoinsert():
  word = input("Word to insert: ")
  meaning = input("Description of word: ")
  return word, meaning

def wordtolookup():
  return input("Word to lookup: ")

def printmeny():
  print("\nMenu for dictionary")
  print("1. Insert")
  print("2. Lookup")
  print("3. Exit program")
  return input("Choose alternative (1-3): ")

# Simple dictionary program using lists of strings
list1 = []
list2 = []

def check_mod1(word):
  return word in list1

def insert_mod1():
  itemword, itemmeaning = wordtoinsert()
  if check_mod1(itemword):
    print(f"{itemword} already exists in the dictionary.")
    return
  list1.append(itemword)
  list2.append(itemmeaning)

def lookup_mod1():
  word = wordtolookup()
  if check_mod1(word):
    index = list1.index(word)
    print(f"Description for {word} : {list2[index]}")
  else:
    print(f"{word} not found in the dictionary.")

# Dictionary program using list of tuples
list_of_tuples = []

def check_mod2(word):
  for w, m in list_of_tuples:
    if w == word:
      return True
  return False

def insert_mod2():
  itemword, itemmeaning = wordtoinsert()
  if check_mod2(itemword):
    print(f"{itemword} already exists in the dictionary.")
    return
  list_of_tuples.append((itemword, itemmeaning))
  
def lookup_mod2():
  word = wordtolookup()
  for w, m in list_of_tuples:
    if w == word:
      print(f"Description for {word} : {m}")
      return
  print(f"{word} not found in the dictionary.")
  
  
# Dictionary program using dictionary data structure
dictionary = {}

def check_mod3(word):
  return word in dictionary

def insert_mod3():
  itemword, itemmeaning = wordtoinsert()
  if check_mod3(itemword):
    print(f"{itemword} already exists in the dictionary.")
    return
  dictionary[itemword] = itemmeaning

def lookup_mod3():
  word = input("Enter the word to look up: ")
  if check_mod3(word):
    print(f"The meaning of {word} : {dictionary[word]}")
  else:
    print(f"{word} not found in the dictionary.")
    
def main_exec(ins,look):
  meny = True
  while meny:
    val = printmeny()

    if val == '1':
      ins()
    elif val == '2':
      look()
    elif val == '3':
      meny = False
      print("Exit program.")
    else:
      print("Invalid choice, please try again.")
    
def main_mod1():
  main_exec(insert_mod1, lookup_mod1)
      
def main_mod2():
  main_exec(insert_mod2, lookup_mod2)
      
def main_mod3():
  main_exec(insert_mod3, lookup_mod3)