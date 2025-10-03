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
  print("3. Delete")
  print("4. Exit program")
  return input("Choose alternative (1-4): ")

# Simple dictionary program using lists of strings

def check_mod1(word, list1):
  return word in list1

def insert_mod1(list1, list2):
  itemword, itemmeaning = wordtoinsert()
  if check_mod1(itemword, list1):
    print(f"{itemword} already exists in the dictionary.")
    return
  list1.append(itemword)
  list2.append(itemmeaning)

def lookup_mod1(list1, list2):
  word = wordtolookup()
  if check_mod1(word, list1):
    index = list1.index(word)
    print(f"Description for {word} : {list2[index]}")
  else:
    print(f"{word} not found in the dictionary.")

def delete_mod1(list1, list2):
  word = wordtolookup()
  if check_mod1(word, list1):
    index = list1.index(word)
    list1.pop(index)
    list2.pop(index)
    print(f"{word} has been deleted from the dictionary.")
  else:
    print(f"{word} not found in the dictionary.")

# Dictionary program using list of tuples

def check_mod2(word, list):
  for w, m in list:
    if w == word:
      return True
  return False

def insert_mod2(list, dummy):
  itemword, itemmeaning = wordtoinsert()
  if check_mod2(itemword, list):
    print(f"{itemword} already exists in the dictionary.")
    return
  list.append((itemword, itemmeaning))
  
def lookup_mod2(list, dummy):
  word = wordtolookup()
  for w, m in list:
    if w == word:
      print(f"Description for {word} : {m}")
      return
  print(f"{word} not found in the dictionary.")
  
def delete_mod2(list, dummy):
  word = wordtolookup()
  for i, (w, m) in enumerate(list):
    if w == word:
      list.pop(i)
      print(f"{word} has been deleted from the dictionary.")
      return
  print(f"{word} not found in the dictionary.")
  
# Dictionary program using dictionary data structure

def check_mod3(word, dictionary):
  return word in dictionary

def insert_mod3(dictionary, dummy):
  itemword, itemmeaning = wordtoinsert()
  if check_mod3(itemword, dictionary):
    print(f"{itemword} already exists in the dictionary.")
    return
  dictionary[itemword] = itemmeaning

def lookup_mod3(dictionary, dummy):
  word = wordtolookup()
  if check_mod3(word, dictionary):
    print(f"The meaning of {word} : {dictionary[word]}")
  else:
    print(f"{word} not found in the dictionary.")

def delete_mod3(dictionary, dummy):
  word = wordtolookup()
  if check_mod3(word, dictionary):
    del dictionary[word]
    print(f"{word} has been deleted from the dictionary.")
  else:
    print(f"{word} not found in the dictionary.")
    
  """
  Common execution function for all modules
  insfunc = insert function
  lookfunc = lookup function
  delfunc = delete function
  """
def main_exec(insfunc, lookfunc, delfunc, list1, list2):
  meny = True
  while meny:
    val = printmeny()

    if val == '1':
      insfunc(list1, list2)
    elif val == '2':
      lookfunc(list1, list2)
    elif val == '3':
      delfunc(list1, list2)
    elif val == '4':
      meny = False
      print("Exit program.")
    else:
      print("Invalid choice, please try again.")
    
def main_mod1():
  list1 = []
  list2 = []
  main_exec(insert_mod1, lookup_mod1, delete_mod1, list1, list2)
      
def main_mod2():
  list_of_tuples = []
  dummy = []
  main_exec(insert_mod2, lookup_mod2, delete_mod2, list_of_tuples, dummy)
      
def main_mod3():
  dictionary = {}
  dummy = {}
  main_exec(insert_mod3, lookup_mod3, delete_mod3, dictionary, dummy)