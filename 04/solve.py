with open('./input.txt', 'r') as fh:
  draws = fh.readline().strip().split(',')
  boards = []
  while fh.readline():
    board = []
    for i in range(5):
      board.append(fh.readline().strip().split())
    boards.append(board)

def check_board(draws, board):
  for row in board:
    if set(row) <= set(draws):
      return True
  for col in zip(*board):
    if set(col) <= set(draws):
      return True

def calculate_solution(board, draws):
  s = 0
  for row in board:
    for n in row:
      if n not in draws:
        s += int(n)
  return s * int(draws[-1])

def part1(boards, draws):
  for i in range(len(draws)):
    for b in boards:
      if check_board(draws[:i+1], b):
        print(f'winner found: {b}\ndraws: {draws[:i+1]}')
        print(f'solution: {calculate_solution(b, draws[:i+1])}')
        return

def part2(boards, draws):
  winners = []
  for i in range(len(draws)):
    for b in boards:
      if check_board(draws[:i+1], b):
        if b not in winners:
          winners.append(b)
          last_draw = i
  print(f"last winner: {winners[-1]}")
  print(f"solution: {calculate_solution(winners[-1], draws[:last_draw+1])}")


part1(boards, draws)
part2(boards, draws)