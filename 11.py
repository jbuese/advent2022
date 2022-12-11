from functools import reduce
import math

def main():
  """
  advent of code 11
  """
  with open('input11.txt', 'r') as file:
    input_f = file.read()

  input_s = input_f.split('\n\n')

  challenge1(input_s)
  challenge2(input_s)


def ex_op(monkey_items, operation):
  op = {'+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y }
  
  operation = operation[19:].split(" ")
  
  for item_i in range(len(monkey_items)):
    monkey_items[item_i] = math.trunc(op[operation[1]](
      monkey_items[item_i] if operation[0] == "old" else int(operation[0]),
      monkey_items[item_i] if operation[2] == "old" else int(operation[2])
    ) / 3)
  
  return monkey_items


def ex_op_2(monkey_items, operation, monkeys_mod):
  op = {'+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y }
  
  operation = operation[19:].split(" ")
  
  for item_i in range(len(monkey_items)):
    item = math.trunc(op[operation[1]](
      monkey_items[item_i] if operation[0] == "old" else int(operation[0]),
      monkey_items[item_i] if operation[2] == "old" else int(operation[2])
    ))
    
    monkey_items[item_i] = item % monkeys_mod
  
  return monkey_items
  
  
def ex_test(monkey_items, monkeys_items, test):
  true_throw = int(test[1][29:])
  false_throw = int(test[2][29:])

  for monkey_item in monkey_items:
    if(monkey_item % int(test[0][21:]) == 0):
      monkeys_items[true_throw].append(monkey_item)
    else:
      monkeys_items[false_throw].append(monkey_item)
  return monkeys_items
      
      
def challenge1(input_s):
  monkeys_items = [
      list(map(int, monkey.split("\n")[1][18:].split(", ")))
      for monkey
      in input_s
  ]
  
  monkey_inspections = [0 for _ in range(len(monkeys_items))]
  
  for round in range(1,21):
    for monkey_i in range(len(monkeys_items)):
      monkey_items = monkeys_items[monkey_i]
      monkey_inspections[monkey_i] += len(monkey_items)
      monkey_items = ex_op(monkey_items, input_s[monkey_i].split("\n")[2])
      monkeys_items[monkey_i] = []
      monkeys_items = ex_test(
          monkey_items, monkeys_items, input_s[monkey_i].split("\n")[3:])
    print(round, monkeys_items)
  
  two_max = sorted(range(len(monkey_inspections)), key=lambda i: monkey_inspections[i])[-2:]
  print(monkey_inspections[two_max[0]]*monkey_inspections[two_max[1]])


def challenge2(input_s):
  monkeys_items = [
      list(map(int, monkey.split("\n")[1][18:].split(", ")))
      for monkey
      in input_s
  ]

  monkeys_mod = reduce(lambda x, y: x*y, [
      int(monkey.split("\n")[3][21:].split(", ")[0])
      for monkey
      in input_s
  ])
    
  monkey_inspections = [0 for _ in range(len(monkeys_items))]

  for round in range(1,10001):
    for monkey_i in range(len(monkeys_items)):
      monkey_items = monkeys_items[monkey_i]
      monkey_inspections[monkey_i] += len(monkey_items)
      monkey_items = ex_op_2(
          monkey_items, input_s[monkey_i].split("\n")[2], monkeys_mod)
      monkeys_items[monkey_i] = []
      monkeys_items = ex_test(monkey_items, monkeys_items,
                              input_s[monkey_i].split("\n")[3:])
    if round%1000 == 0 or round==20:
      print(round, monkey_inspections)
    
  two_max = sorted(range(len(monkey_inspections)),
                   key=lambda i: monkey_inspections[i])[-2:]
  print(monkey_inspections[two_max[0]]*monkey_inspections[two_max[1]])


if __name__ == '__main__':
    main()
