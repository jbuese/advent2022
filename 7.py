def main():
  """
  advent of code 7
  """
  with open('input7.txt', 'r') as file:
    input_f = file.read()
    
  input_s = input_f.split('\n')

  challenge1(input_s)
  challenge2(input_s)


def calc_dir_sizes(input_s):
  """
  calculate the disk size for a given input of terminal commands
  """
  current_branch = []
  all_directories = {"/": 0}

  for line in input_s:
    if(line.startswith('$')):
      line = line[2:]
      if(line.startswith("cd ..")):
        # remove last directory from current_branch
        current_branch.pop()
      elif(line.startswith("cd /")):
        current_branch = ["/"]
      elif(line.startswith("cd")):
        # add new directory to current_branch and all directories
        # sadly the names are not unique so I add the parent directories as a prefix
        # the dollar sign is added for persisting which level the directory is at
        directory = f"${current_branch[-1]}_{line[3:]}"
        current_branch.append(directory)
        all_directories[directory] = 0
    else:
      # sum up if file
      if not (line.startswith("dir") or line.startswith("ls")):
        for directory in current_branch:
          all_directories[directory] += int(line.split(' ')[0])
    
  return all_directories


def challenge1(input_s):
  directories = calc_dir_sizes(input_s)
  sum = 0
  for directory in directories:
    size = directories[directory]
    if size <= 100000:
      sum += size
  print(sum)


def challenge2(input_s):
  disk_space = 70000000
  update_space = 30000000
  
  directories = calc_dir_sizes(input_s)
  available_space = disk_space-directories["/"]
  need_space = update_space - available_space
  
  directories = {name: size for name, size in directories.items() if size >= need_space}
  res_key, res_val = min(directories.items(), key=lambda x: abs(need_space - x[1]))
  
  # print("available space:", available_space)
  # print("needed space:", need_space)
  # print("dirs big enough:", directories)
  print(res_key, res_val, sep=', ')


if __name__ == '__main__':
    main()
