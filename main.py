import random

a = ['R', 'P', 'S']
print("Hi! Do you want to play with a person or a computer?(computer = 1, person = 2)")
s = int(input())
if(s == 2):
  f = False
  while(f == False):
    print("Enter the first player's decision:")
    c = input()
    if(c in a): f = True
  f = False
  while(f == False):
    print("Enter the second player's decision:")
    d = input()
    if(d in a): f = True
  if(c == 'P' and d == 'R'):
    print("1st player wins")
  elif(d == 'P' and c == 'R'):
    print("2nd player wins")
  elif(c == 'R' and d == 'S'):
    print("1st player wins")
  elif(c == 'S' and d == 'R'):
    print("2nd player wins")
  elif(c == 'S' and d == 'P'):
    print("1st player wins")
  elif(c == 'P' and d == 'S'):
    print("2nd player wins")
  else:
    print("Draw")
else:
  f = False
  while(f == False):
    print("Enter the player's decision:")
    c = input()
    if(c in a): f = True
  x = random.randint(0, 2)
  d = a[x]
  if(c == 'P' and d == 'R'):
    print("player wins")
  elif(d == 'P' and c == 'R'):
    print("computer wins")
  elif(c == 'R' and d == 'S'):
    print("player wins")
  elif(c == 'S' and d == 'R'):
    print("computer wins")
  elif(c == 'S' and d == 'P'):
    print("player wins")
  elif(c == 'P' and d == 'S'):
    print("computer wins")
  else:
    print("Draw")