def main():
  """
  advent of code 6
  """
  with open('input6.txt', 'r') as file:
    input_f = file.read()

  challenge1(input_f)
  challenge2(input_f)


def detect_marker(input_f, marker_length):
  for endPos in range(marker_length, len(input_f)):
    if(len(set(input_f[(endPos-marker_length):endPos])) == marker_length):
      return endPos


def challenge1(input_f):
  print(detect_marker(input_f, 4))


def challenge2(input_f):
  print(detect_marker(input_f, 14))


if __name__ == '__main__':
    main()
