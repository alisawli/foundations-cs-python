def factorial(number):
  if number < 0:
    return " Factorial is not defined for negative numbers"
  elif number == 0 or number == 1:
    return 1
  else:
    result = 1
    for i in range(2, number + 1):
      result *= i
    return result


def divisor(n):
  list = []
  for i in range(1, n + 1):
    if n % i == 0:
      list.append(i)
  return list


def reverseString(string):
  reverse = ""
  for i in range(len(string) - 1, -1, -1):
    reverse += string[i]
  return reverse


def listofevennumbers(list):
  list2 = []
  for i in list:
    if i % 2 == 0:
      list2.append(i)
  return list2


def strong_password(string):
  length = len(string)
  resultOfUpper = False
  resultOfLower = False
  resultOfDigit = False
  resultOfSpecial = False
  result = False
  for i in string:
    if i.isupper():
      resultOfUpper = True
      break
  for i in string:
    if i.islower():
      resultOfLower = True
      break
  for i in string: 
    if i.isdigit():
      resultOfDigit = True
      break
  for i in string:
    if not (i.isalpha() or i.isdigit() or i == ' '):
      resultOfSpecial = True
      break

  if (length > 8 and resultOfUpper and resultOfLower and resultOfDigit
      and resultOfSpecial):
    result = True
  return result


def is_Ip4(string):
  result = False
  ip = string.split(".")
  for i in range(0, len(ip)):
    ip[i] = int(ip[i])
  s = 0
  for i in ip:
    if 0 <= i <= 255:
      s = s + 1
  if s == 4:
    result = True
  return result



print(is_Ip4("192.155.10.5"))
print(strong_password("Sawli123564@"))