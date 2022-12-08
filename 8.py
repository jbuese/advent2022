def main():
  """
  advent of code 8
  """
  with open('input8.txt', 'r') as file:
    input_f = file.read()
    
  input_s = input_f.split('\n')

  challenge1(input_s)
  challenge2(input_s)


def challenge1(input_s):
  len_row = len(input_s[0])
  len_column = len(input_s)
  count = 2*len_row+2*len_column-4
  
  for i in range(1, len_column-1):
    for j in range(1, len_row-1):
      value = input_s[i][j]
      invisible = 0
      for i_t in range(i-1, -1, -1):
        if(input_s[i_t][j] >= value):
          invisible += 1
          break
      for i_b in range(i+1,len_column):
        if(input_s[i_b][j] >= value):
          invisible += 1
          break
      for j_l in range(j-1, -1, -1):
        if(input_s[i][j_l] >= value):
          invisible += 1
          break
      for j_r in range(j+1,len_row):
        if(input_s[i][j_r] >= value):
          invisible += 1
          break

      if(invisible<4):
        count += 1
  print(count)


def challenge2(input_s):
  len_row = len(input_s[0])
  len_column = len(input_s)
  scenic_max = 0
  
  for i in range(1, len_column-1):
    for j in range(1, len_row-1):
      value = input_s[i][j]
      topV, bottomV, leftV, rightV = 0,0,0,0
      for i_t in range(i-1, -1, -1):
        topV += 1
        if(input_s[i_t][j] >= value):
          break
      for i_b in range(i+1, len_column):
        bottomV += 1
        if(input_s[i_b][j] >= value):
          break
      for j_l in range(j-1, -1, -1):
        leftV += 1
        if(input_s[i][j_l] >= value):    
          break
      for j_r in range(j+1, len_row):
        rightV += 1
        if(input_s[i][j_r] >= value):
          break
      scenic_max = max(scenic_max, topV*bottomV*leftV*rightV)
  
  print(scenic_max)


if __name__ == '__main__':
    main()
