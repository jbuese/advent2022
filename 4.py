def main():
  """
  advent of code 4
  """
  with open('input4.txt', 'r') as file:
    input = file.read()

  input_s = input.split('\n')

  challenge1(input_s)
  challenge2(input_s)


def get_section_borders(pair):
  """
  Gets the start and end points of every section out of a string
  similar to: "76-93,94-94" (in this case: 76, 93, 94, 94)
  @returns start1, end1, start2, end2
  """
  assign1, assign2 = pair.split(',')
  start1 = int(assign1.split("-")[0])
  end1 = int(assign1.split("-")[1])
  start2 = int(assign2.split("-")[0]) 
  end2 = int(assign2.split("-")[1])
  return start1, end1, start2, end2


def challenge1(input_s):
  sum = 0
  for pair in input_s:
    start1, end1, start2, end2 = get_section_borders(pair)
    
    if(
      (start1 <= start2 and end1 >= end2) or
      (start2 <= start1 and end2 >= end1)
    ):
      sum+=1
      
  print(sum)


def challenge2(input_s):
  sum = 0
  for pair in input_s:
    start1, end1, start2, end2 = get_section_borders(pair)

    if(
      (start1 <= start2 and end1 >= start2) or
      (start1 <= end2 and start1 >= start2)
    ):
      sum += 1

  print(sum)


if __name__ == '__main__':
    main()
