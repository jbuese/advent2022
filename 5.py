def main():
  """
  advent of code 5
  """
  with open('input5.txt', 'r') as file:
    input = file.read()

  challenge1(input)
  challenge2(input)


def build_stacks(stacks_input):
  """
  Builds stacks from input:
  ```
      [D]          [['Z', 'N'],
  [N] [C]      ->  ['M', 'C', 'D'],
  [Z] [M] [P]      ['P']]
   1   2   3
  ``` 
  @returns list of lists with stacks
  """
  stacks_input = stacks_input.split("\n")
  stacks_input = stacks_input[::-1]
  
  stacks = [[] for _ in range(0, int(stacks_input[0][len(stacks_input[0])-2]))]
  stacks_input = stacks_input[1:]
  
  for stack_row in stacks_input:
    for i in range(1, len(stack_row), 4):
      el = stack_row[i]
      if el!=' ':
        stacks[int((i-1)/4)].append(stack_row[i])
      
  return stacks
     
      
def perform_moves_9000(stacks, moves_input):
  """
  Performs moves of a CrateMover 9000 which can only move a single crate at once
  """
  moves = moves_input.split("\n")
  for move in moves:
    _, amount, _, from_c, _, to_c = move.split(" ")
    for _ in range(0, int(amount)):
      stacks[int(to_c)-1].append(stacks[int(from_c)-1].pop())
  return stacks


def perform_moves_9001(stacks, moves_input):
  """
  Performs moves of a CrateMover 9001 which moves multiple crates at once (keeping their order)
  """
  moves = moves_input.split("\n")
  for move in moves:
    _, amount, _, from_c, _, to_c = move.split(" ")
    len_substack_indexed = len(stacks[int(from_c)-1])
    split_index = len_substack_indexed-int(amount)
    stacks[int(to_c)-1].extend(stacks[int(from_c)-1][split_index:len_substack_indexed])
    stacks[int(from_c)-1] = stacks[int(from_c)-1][:split_index]
    
  return stacks
      
      
def challenge1(input_s):
  stacks_input, moves_input = input_s.split("\n\n")
  stacks = perform_moves_9000(build_stacks(stacks_input), moves_input)
  result = ""
  for stack in stacks:
    result += stack.pop()
  print(result)


def challenge2(input_s):
  stacks_input, moves_input = input_s.split("\n\n")
  stacks = perform_moves_9001(build_stacks(stacks_input), moves_input)
  result = ""
  for stack in stacks:
    result += stack.pop()
  print(result)


if __name__ == '__main__':
    main()
