def main():
  """
  advent of code 10
  """
  with open('input10.txt', 'r') as file:
    input_f = file.read()
    
  input_s = input_f.split('\n')

  challenge1(input_s)
  challenge2(input_s)


def execute_instr(reg_x, instr, instr_count, add):
  """
  Cxecutes a single instruction given the current register, the instruction, 
  the instr-count and the value of the add-switch
  
  Returns the new values for the register, instr-count and add
  """
  split = instr.split(" ")
  if(split[0] == "noop"):
    instr_count += 1
  else:
    if(add):
      reg_x += int(split[1])
      instr_count += 1
      add = False
    else:
      add = True
      
  return reg_x, instr_count, add


def challenge1(input_s):
  sum_20 = 0
  reg_x = 1
  instr_count = 0
  add = False
  
  for cycle in range(1,240):
    if((cycle+20)%40 == 0):
      sum_20 += cycle*reg_x
      
    reg_x, instr_count, add = execute_instr(
        reg_x, input_s[instr_count], instr_count, add)

  print(sum_20)


def challenge2(input_s):
  reg_x = 1
  instr_count = 0
  add = False

  crt = [[] for _ in range(6)]

  for row in range(6):
    for cycle in range(40):    
      if(abs(reg_x-cycle) <= 1):
        crt[row].append("#")
      else:
        crt[row].append(".")

      reg_x, instr_count, add = execute_instr(
          reg_x, input_s[instr_count], instr_count, add)
    
  for row in crt:
    print(''.join(row))  # pretty print the final board
    


if __name__ == '__main__':
    main()
