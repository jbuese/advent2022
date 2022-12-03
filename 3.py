def main():
  """
  advent of code 3
  """
  with open('input3.txt', 'r') as file:
    input = file.read()

  input_s = input.split('\n')
  
  challenge1(input_s)
  challenge2(input_s)
  
  
def get_item_value(item):
  if item.islower():
    return ord(item)-96
  else:
    return ord(item)-38
  
  
def challenge1(input_s):
  sum = 0
  for rucksack in input_s:
    half1 = rucksack[:len(rucksack)//2]
    half2 = rucksack[len(rucksack)//2:]
    intersection = set([item for item in half1 if item in half2])
    for item in intersection:
      sum += get_item_value(item)
  print(sum)
  
  
def challenge2(input_s):
  sum = 0
  groups = []
  
  for i in range(0, len(input_s), 3):
    groups.append(input_s[i:i+3])
  
  for group in groups:
    intersection = set(group[0]) & set(group[1]) & set(group[2])
    sum += get_item_value(intersection.pop())
    
  print(sum)


if __name__ == '__main__':
    main()
