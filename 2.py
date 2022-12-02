def main():
  """
  advent of code 2
    - choose comb_strat1 for 1st challenge
    - choose comb_strat2 for 2nd challenge
  """
  
  """
    A - rock
    B - paper
    C - scissors
    X - rock
    Y - paper
    Z - scissors
  """
  comb_strat1 = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
  }
  
  """
    A - rock
    B - paper
    C - scissors
    X - loose
    Y - draw
    Z - win
  """
  comb_strat2 = {
    "A X": 3, # scissors 3
    "A Y": 4, # rock 1 
    "A Z": 8, # paper 2
    "B X": 1, # rock 1
    "B Y": 5, # paper 2
    "B Z": 9, # scissors 3
    "C X": 2, # paper 2
    "C Y": 6, # scissors 3
    "C Z": 7, # rock 1
  }
  
  with open('input2.txt', 'r') as file:
    input = file.read()

  input_s = input.split('\n')
  
  sum = 0
  for game in input_s:
    sum += comb_strat2[game]
    
  print(sum)


if __name__ == '__main__':
    main()
