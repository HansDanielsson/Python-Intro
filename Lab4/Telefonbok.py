"""
Söker efter ett värde 'item' i en lista av dictionaries ('phonebook').
Letar i fältet 'skey', som kan innehålla komma-separerade värden.

Returnerar index för första matchen, annars -1.
"""
def itemsearch(skey, item, phonebook):
  for index, post in enumerate(phonebook):
    # Hämta värdet för nyckel 'skey', eller tom sträng om nyckeln saknas
    field_value = post.get(skey, "")
    
    # Dela upp fältet på kommatecken och ta bort mellanslag runt varje del.
    split_values = [v.strip() for v in field_value.split(",")]
    
    # Kolla om det sökta värdet finns i listan.
    if item in split_values:
      return index
  
  return -1
      
"""
Lägger till en ny post i phonebook om både namn och nummer är unika.
command: Lista där [1] är namn och [2] är nummer.
phonebook: Lista av dictionaries med nycklarna Name och Number
"""
def addcommand(command, phonebook):
  if len(command) < 3:
    return
  
  name = command[1]
  number = command[2]
  
  # Kontrollerar om numret redan finns.
  if itemsearch("Number", number, phonebook) != -1:
    print(number + " already exists")
    return
  
  if itemsearch("Name", name, phonebook) != -1:
    print(name + " already exists")
    return

  phonebook.append({"Name": name + ",", "Number": number})

"""
Söker efter ett namn i phonebook och skriver ut tillhörand nummer.
"""
def lookupcommand(command, phonebook):
  if len(command) < 2:
    return
  
  name = command[1]
  
  posindex = itemsearch("Name", name, phonebook)
  
  if posindex == -1:
    print(name + " not found")
  else:
    print(phonebook[posindex]["Number"])

"""
Lägger till ett alias till en befintlig kontakt i phonebook.
"""
def aliascommand(command, phonebook):
  if len(command) < 3:
    return
  
  name = command[1]
  newname = command[2]
  
  # Kontroll: aliasnamnet får inte redan finnas
  if itemsearch("Name", newname, phonebook) != -1:
    print("name not found or duplicate name")
    return
  
  # Hitta den post där orginalnamnet finns.
  posindex = itemsearch("Name", name, phonebook)
  if posindex == -1:
    print("name not found or duplicate name")
    return

  phonebook[posindex]["Name"] += newname + ","
  
"""
Ändrar numret för en kontakt med det givna namnet, om
- namnet finns i phonebook
- det nya numret inte redan används
"""
def changecommand(command, phonebook):
  if len(command) < 3:
    return
  
  name = command[1]
  number = command[2]
  
  # Kontrollera om numret redan finns någon annanstans.
  if itemsearch("Number", number, phonebook) != -1:
    print(number + " already exists")
    return

  # Hitta posten som innehåller namnet
  posindex = itemsearch("Name", name, phonebook)
  if posindex == -1:
    print(name + " not found")
    return

  phonebook[posindex]["Number"] = number
  
"""
Sparar phonebook ut på text fil
"""
def savecommand(command, phonebook):
  if len(command) < 2:
    return
  
  # Försöker öppna filen säkert
  try:
    # Öppna filen för skrivning
    with open(command[1], "w", encoding="utf-8") as f:
      # loopa igenom phonebook och skriv ut posten
      for post in phonebook:
        # Hämta värdet för nyckel 'Name'
        names = post["Name"]
        
        # Dela upp fältet på kommatecken och ta bort mellanslag runt varje del.
        name_list = [name.strip() for name in names.split(",")]
        
        # Skriv ut alla namn med samma nummer
        for item in name_list:
          if len(item) > 0:
            f.write(f"{post["Number"]};{item};\n")
  except Exception as e:
    print(f"Fel vid sparning: {e}")
    
    
"""
Läser tillbaka phonebook från text fil.
"""
def loadcommand(command, phonebook):
  if len(command) < 2:
    return
  
  # Försöker öppna filen säkert
  try:
    with open(command[1], "r", encoding="utf-8") as f:
      # Töm phonebook för inläsning från fil
      phonebook.clear()
      
      # loopa igenom filen
      for post in f:
        item = [p.strip() for p in post.strip().split(";") if p.strip()]
        print(item)
        if len(item) != 2:
          continue
        
        # Kolla om numret finns
        posindex = itemsearch("Number", item[0], phonebook)
        if posindex == -1:
          phonebook.append({"Name": item[1] + ",", "Number": item[0]})
        else:
          phonebook[posindex]["Name"] += item[1] + ","
  except Exception as e:
    print(f"Fel vid inläsning: {e}")
    

"""
Skriver ut nuvarande phonebook
"""
def printbok(phonebook):
  for post in phonebook:
    print(post)

def main():
  phonebook = []
  while True:
    try:
      command = input("phoneBook>").strip().split()
      if not command:
        continue # hoppa över tomma rader
      cmd = command[0].lower()
      if cmd == "add":
        addcommand(command, phonebook)
      elif cmd == "lookup":
        lookupcommand(command, phonebook)
      elif cmd == "alias":
        aliascommand(command, phonebook)
      elif cmd == "change":
        changecommand(command, phonebook)
      elif cmd == "save":
        savecommand(command, phonebook)
      elif cmd == "load":
        loadcommand(command, phonebook)
      elif cmd == "print":
        printbok(phonebook)
      elif cmd == "quit":
        break
    except Exception as e:
      print(f"Fel: {e}")