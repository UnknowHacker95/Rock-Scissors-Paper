a = ['R', 'P', 'S', 'Rock', 'Paper', 'Scissors']
print("Hi!")
f = False
while(f == False):
  print("Enter the first player's decision:")
  c = input()
  if(c not in a): print("Enter the first player's decision:")
  else: f = True
f = False
while(f == False):
  print("Enter the second player's decision:")
  d = input()
  if(d not in a): print("Enter the second player's decision:")
  else: f = True
if(c == 'P' and d == 'R') or (c == 'Paper' and d == 'Rock'):
  print("1st player wins")
elif(d == 'P' and c == 'R') or (d == 'Paper' and c == 'Rock'):
  print("2nd player wins")
elif(c == 'R' and d == 'S') or (c == 'Rock' and d == 'Scissors'):
  print("1st player wins")
elif(c == 'S' and d == 'R') or (c == 'Scissors' and d == 'Rock'):
  print("2nd player wins")
elif(c == 'S' and d == 'P') or (c == 'Scissors' and d == 'Paper'):
  print("1st player wins")
elif(c == 'P' and d == 'S') or (c == 'Paper' and d == 'Scissors'):
  print("2nd player wins")
else: print("Draw")