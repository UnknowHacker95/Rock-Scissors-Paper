import random

a = ['R', 'P', 'S']
print("Hi! Do you want to play with a person or a computer?(computer = 1, person = 2)")
s = int(input())
v = {'R':'S', 'S':'P', 'P':'R'}
f = False
while(f == False):
  print("Enter the first player's decision:")
  c = input()
  if(c in a): f = True
if(s == 2):
  f = False
  while(f == False):
    print("Enter the second player's decision:")
    d = input()
    if(d in a): f = True  
else:
  x = random.randint(0, 2)
  d = a[x]
  print("Computer's decision -", d)
if(v[c] == d):
  if(s == 2):
    print("1st player wins (⌐■_■)")
  else: print("player wins (￣^￣)ゞ")
elif(v[d] == c):
  if(s == 2):
    print("2nd player wins (⌐■_■)")
  else:
    print("computer wins (╯°益°)╯彡┻━┻")
else:
  print("Draw")