def countdigit(n):
  if n < 10:
    return 1
  else:
    return 1 + countdigit(n // 10)
def max(list):
  if len(list) == 1:
    return list[0]
  elif len(list) == 0:
    return 0
  else:
    max = 0
    for i in range(0, len(list)):
      if (list[i] > max):
        max = list[i]
    return max
def countTags(htmlcode, tags):
  tags1 = "<" + tags + ">"
  index = htmlcode.find(tags1)
  if (index == -1):
    return 0
  else:
    return 1 + countTags(htmlcode[index + len(tags) + 1:], tags)


def display_menu():
  print("1. Count Digits")
  print("2. Find Max")
  print("3. Count Tags")
  print("4. Exit")
  print("-" * 25)
def main():
  while True:
    display_menu()
    choice = input("Enter a choice: ")
    if choice == "1":
      n=int(input("Enter an integer: "))
      count = countdigit(n)
      print("Number of digits:", count)
    elif choice == "2":
      numbers=[]
      n = int(input("Enter number of elements : "))
      for i in range(0, n):
       ele = int(input())
       numbers.append(ele) 
      max_value = max(numbers)
      print("Maximum value:", max_value)
    elif choice == "3":
      html_code = '''<html>
<head>
<title>My Website</title>
</head>
<body>
<h1>Welcome to my website!</h1>
<p>Here you'll find information about me and my hobbies.</p>
<h2>Hobbies</h2>
<ul>
<li>Playing guitar</li>
<li>Reading books</li>
<li>Traveling</li>
<li>Writing cool h1 tags</li>
</ul>
</body>
</html>'''
      tag = input("Enter a tag: ")
      count = countTags(html_code, tag)
      print("Number of occurrences:", count)
    elif choice == "4":
      print("Exiting the program...")
      break
    else:
      print("Invalid choice. Please try again.")


if __name__ == "__main__":
  main()
