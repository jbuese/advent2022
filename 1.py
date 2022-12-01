def main():
  with open('input2.txt', 'r') as file:
    input = file.read()
  
  input_s = input.split('\n')
  elf_carry = []
  temp = 0

  # first el
  elf_carry.append(0)
  for s in input_s:
    if s == '':
      elf_carry.append(0)
    else:
      elf_carry[-1] += int(s)
  
  # last el
  if(input_s.__contains__('')):
    elf_carry.append(temp)
  
  elf_carry.sort(reverse=True)
  
  print(sum(elf_carry[:3]))

if __name__ == '__main__':
    main()