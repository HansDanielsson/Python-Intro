"""
  Skriver ut menyvalen för 0 -> 4
"""
def meny(kim, chris, board):
  print("=== Bulletin board system ===")
  print("Kim reads message: " + board[kim].messagetype())
  print("Chris reads message: " + board[chris].messagetype())
  print("1: Direct Kim to other board")
  print("2: Direct Chris to other board")
  print("3: Tell Kim to post a message")
  print("4: Tell Chris to post a message")
  print("0: exit")
  return newmessage("Enter choice: ")

"""
Rutin som skriver ut meddelande samt hämtar svaret
"""
def newmessage(message):
  return input(message)

"""
Klassen som håller reda på alla meddelanden till anslagstavlan
.send() : Adderar meddelande
.messagetype() : Skriver ut meddelandet
"""
class Board:
  def __init__(self, msg): # Konstruktorn
    self.message = msg # Instansvariabel för att lagra meddelanden
  def send(self, msg):
    self.message += msg + "\n" # Lägg till nytt meddelande
  def messagetype(self):
    return self.message

"""
Huvudrutin som simmulerar anslagstavlor för 2 personer
"""
def main():
  # Skapa 2 anslagstavlor
  board = [Board("Board1:\n"),Board("Board2:")]
  # Initiera Kim och Chris till olika anslagstavlor
  kim = 0
  chris = 1
  notexit = True
  while notexit:
    command = meny(kim, chris, board)
    if command == '1':
      kim = (kim + 1) % 2
    elif command == '2':
      chris = (chris + 1) % 2
    elif command == '3':
      board[kim].send(newmessage("Enter message:"))
    elif command == '4':
      board[chris].send(newmessage("Enter message:"))
    elif command == '0':
      notexit= False