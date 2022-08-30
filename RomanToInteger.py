# roman to integer
given_string = 'LVIII'
roman_num = {
  'I': 1,
  'V': 5,
  'X': 10,
  'L': 50,
  'C': 100,
  'D': 500,
  'M': 1000
}
sum = 0
str_length = len(given_string)
skip_charact = False
# using for loop
for index in range(0, str_length):
  if skip_charact == True:
    skip_charact = False
    #(skipping characters(characters as charact))
    continue

  current = given_string[index]

  if index == str_length - 1:
    sum = sum + roman_num[current]
    skip_charact = False
    break

  if current == 'I':
    # 'I' can be placed V and X
    next = given_string[index+1]
    if next == 'V' or next == 'X':
      sum = sum + roman_num[next] - roman_num[current]
      skip_charact = True
      #print(f'sum of I {sum}')
    else:
      sum = sum + roman_num[current]

  elif current=='C':
    # 'C' can be placed D and M
    next = given_string[index+1]
    if next == 'D' or next == 'M':
      sum = sum + roman_num[next] - roman_num[current]
      skip_charact=True
      #print(f'sum of C {sum}')
    else:
      sum = sum + roman_num[current]

  elif current == 'X':
    # 'X' can be placed L and C
    next=given_string[index+1]
    if next == 'L' or next == 'C':
      sum = sum + roman_num[next] - roman_num[current]
      skip_charact = True
      #print(f'sum of X {sum}')
    else:
      sum = sum + roman_num[current]

  else:
    #print('regular scenario')
    sum = sum + roman_num[current]

# The total sum of the given_string is
print(f'the sum of given_string is {sum}')
