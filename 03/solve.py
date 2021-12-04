with open('./input.txt', 'r') as f:
    numbers = []
    for l in f:
        numbers.append(l.strip())

def get_most_common(column, numbers, inv=False):
  ones = 0
  zeros = 0
  for n in numbers:
    if n[column] == "1":
      ones += 1
    else:
      zeros += 1
  if inv:
    return '0' if ones >= zeros else '1'
  else:
    return '1' if ones >= zeros else '0'

def find_gamma(numbers):
  cols = len(numbers[0])
  ret = ""
  for col in range(cols):
    ret += get_most_common(col, numbers)
  return ret

def find_epsilon(gamma):
  return ''.join('1' if x =='0' else '0' for x in gamma)

print(f"part 1: {int(find_gamma(numbers),2) * int(find_epsilon(find_gamma(numbers)), 2)}")

def o2(numbers, col, inv=False):
  if len(numbers) == 1:
    return numbers
  else:
    filtered = list(filter(lambda num: num[col] == get_most_common(col, numbers, inv=inv), numbers))
    return o2(filtered, col+1, inv=inv)


print(f"part 2: {int(o2(numbers, 0)[0], 2) * int(o2(numbers, 0, inv=True)[0], 2)}")