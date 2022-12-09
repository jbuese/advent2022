import math


def main():
  """
  advent of code 9
  """
  with open('input9.txt', 'r') as file:
    input_f = file.read()
    
  input_s = input_f.split('\n')

  challenge1(input_s)
  challenge2(input_s)


def calc_t_pos(h_pos, t_pos):
  """
  function that calculates the next pos for T given the new
  pos of H
  """
  d_x = h_pos[0] - t_pos[0]
  d_y = h_pos[1] - t_pos[1]

  if(abs(d_x)+abs(d_y)>2):
    d_x = int(d_x*0.5) if abs(d_x) == 2 else d_x
    d_y = int(d_y*0.5) if abs(d_y) == 2 else d_y
    t_pos = (t_pos[0]+d_x, t_pos[1]+d_y)
  elif(d_y == 0 and abs(d_x) > 1):
    d_x = int(d_x*0.5) if abs(d_x) == 2 else d_x
    t_pos = (t_pos[0]+d_x, t_pos[1])
  elif(d_x == 0 and abs(d_y) > 1):
    d_y = int(d_y*0.5) if abs(d_y) == 2 else d_y
    t_pos = (t_pos[0], t_pos[1]+d_y)
    
  return t_pos


def perform_moves_calc2(input_s):
  """
  performs moves for challenge 2 (only put # at pos of tail no. 9)
  - based on the calc_t_pos-function
  """
  # if index out of range errors occur the board needs to be bigger
  board = [['.' for x in range(500)] for y in range(500)]
  pos_s = [(250,250) for _ in range(10)]

  for move in input_s:
    direction, steps = move.split(' ')
    for _ in range(0, int(steps)):
      match direction:
        case "U":
          pos_s[0] = (pos_s[0][0]+1, pos_s[0][1])
        case "D":
          pos_s[0] = (pos_s[0][0]-1, pos_s[0][1])
        case "R":
          pos_s[0] = (pos_s[0][0], pos_s[0][1]+1)
        case "L":
          pos_s[0] = (pos_s[0][0], pos_s[0][1]-1)

      for t_i in range(1, len(pos_s)):
        pos_s[t_i] = calc_t_pos(pos_s[t_i-1], pos_s[t_i])
        if t_i == 9:
          board[pos_s[t_i][0]][pos_s[t_i][1]] = '#'
  return board


def perform_moves_calc(input_s):
  """
  function to calculate board with # at pos tail has visited
  - based on the calc_t_pos-function
  """
  # if index out of range errors occur the board needs to be bigger
  board = [['.' for x in range(500)] for y in range(500)]
  h_pos = (250, 250)
  t_pos = (250, 250)

  for move in input_s:
    direction, steps = move.split(' ')
    for _ in range(0, int(steps)):
      match direction:
        case "U":
          h_pos = (h_pos[0]+1, h_pos[1])
        case "D":
          h_pos = (h_pos[0]-1, h_pos[1])
        case "R":
          h_pos = (h_pos[0], h_pos[1]+1)
        case "L":
          h_pos = (h_pos[0], h_pos[1]-1)

      t_pos = calc_t_pos(h_pos, t_pos)
      board[t_pos[0]][t_pos[1]] = '#'
  return board


def perform_moves(input_s):
  """
  function to calculate board with # at pos tail has visited
  - based on vector calculations 
  - this did not work for the second challenge so might be wrong
  """
  # if index out of range errors occur the board needs to be bigger
  board = [['.' for x in range(500)] for y in range(500)]
  h_pos = (250,250)
  t_pos = (250,250)
  
  for move in input_s:
    direction, steps = move.split(' ')
    vector = (0, 0)
    for _ in range(0,int(steps)):
      prev_h_pos = h_pos
      
      match direction:
        case "U":
          h_pos = (h_pos[0]+1, h_pos[1])
        case "D":
          h_pos = (h_pos[0]-1, h_pos[1])
        case "R":
          h_pos = (h_pos[0], h_pos[1]+1)
        case "L":
          h_pos = (h_pos[0], h_pos[1]-1)
      
      # if the distance is not higher than 1.5 H and T are right next to each
      # other (distance==1) or diagonally next to each other (distance~=1.4)
      # and no move needs to be performed, otherwise a move needs to be done
      # but if the distance is higher than ~2.14 an illegal pos occured 
      vector = (prev_h_pos[0] - t_pos[0], prev_h_pos[1] - t_pos[1])
      distance = math.sqrt(
        (h_pos[0] - t_pos[0])**2 +
        (h_pos[1] - t_pos[1])**2
      )
      if(distance >= 1.42):
        if(distance > 2.24):
          print("something went wrong")
        t_pos = (t_pos[0]+vector[0], t_pos[1]+vector[1])
      if(distance != 0):
        board[t_pos[0]][t_pos[1]] = '#'
  return board
          

def challenge1(input_s):
  board = perform_moves(input_s)
  count = 0
  for row in board[::-1]:
    # print(''.join(row))  # pretty print the final board
    count += row.count("#")
  print(count)


def challenge2(input_s):
  board = perform_moves_calc2(input_s)
  count = 0
  for row in board[::-1]:
    # print(''.join(row))  # pretty print the final board
    count += row.count("#")
  print(count)


if __name__ == '__main__':
    main()
