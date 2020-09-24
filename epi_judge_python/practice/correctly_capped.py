'''
This question is asked by Google. Given a string, 
return whether or not it uses capitalization correctly. 
A string correctly uses capitalization if all letters are capitalized, 
no letters are capitalized, or only the first letter is capitalized.

Ex: Given the following strings...

"USA", return true
"Calvin", return true
"compUter", return false
"coding", return true
'''

def correctly_capped(string):
  if len(string) <= 1:
    return True
  all_capital = True
  all_lower = True
  i = 1
  while (all_capital or all_lower) and i < len(string):
    if string[i].isupper():
      all_lower = False
    else:
      all_capital = False
    i += 1
  if i == len(string):
    return (string[0].isupper() and all_capital) or \
    (string[0].islower() and all_lower) or (string[0].isupper() and all_lower) # True if cap + all_cap, cap + all lower, lower + all lower
  else:
    return False


strings = ['USA', 'Calvin', 'compUter', 'coding', '', 'I', 'i']
for i, string in enumerate(strings):
  print(i, correctly_capped(string))