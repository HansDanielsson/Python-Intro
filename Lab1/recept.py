"""
Filen innehåller funktioner för receptberäkning.
* recept(antal): Skriver ut ingredienser för sockerkaka baserat på antal personer.
* tidblanda(antal): Beräknar tid för att blanda ingredienser baserat på antal personer.
* tidgradda(antal): Beräknar tid för att grädda kakan baserat på antal personer.
* sockerkaka(antal): Skriver ut recept och total tid för att baka kakan baserat på antal personer.
"""
def recept(antal):
  orginal_antal = 4
  print("Recept för sockerkaka till ", antal, "personer:")
  print(round(3 * antal / orginal_antal), "st ägg")
  print(round(3 * antal / orginal_antal), "dl strösocker")
  print(round(2 * antal / orginal_antal), "tsk vaniljsocker")
  print(round(2 * antal / orginal_antal), "tsk bakpulver")
  print(round(3 * antal / orginal_antal), "dl vetemjöl")
  print(round(75 * antal / orginal_antal), "g smör")
  print(round(1 * antal / orginal_antal), "dl vatten")
  
def tidblanda(antal):
  return 10 + antal

def tidgradda(antal):
  return 30 + antal * 3

def sockerkaka(antal):
  recept(antal)
  print("Tid att baka kakan: ", tidblanda(antal) + tidgradda(antal), "minuter")
  print("-" * 35)
  print()
  
sockerkaka(4)
sockerkaka(7)