#!/usr/bin/env python
# coding: utf-8

# In[5]:


lines = []
with open("Day4.txt") as f:
  for l in f:
    lines.append(l.strip())

calls = [int(x) for x in lines[0].split(",")]

boards = []

for i in range(2, len(lines), 6):
  board = []
  for n in range(5):
    board.append([int(x) for x in lines[i + n].split(" ") if x != ""])
  boards.append(board)

boardplays = []
for board in boards:
  boardplays.append([[False for i in range(5)] for j in range(5)])

boarddone = [False for i in range(len(boards))]
  
for call in calls:
  for bn, board in enumerate(boards):
    for y in range(5):
      for x in range(5):
        if board[y][x] == call:
          boardplays[bn][y][x] = True
  for bn, boardplay in enumerate(boardplays):
    if boarddone[bn]:
      continue
    win = False
    for col in range(5):
      if all([boardplay[col][x] for x in range(5)]):
        win = True
    for row in range(5):
      if all([boardplay[y][row] for y in range(5)]):
        win = True
    if win:
      s = 0
      for y in range(5):
        for x in range(5):
          if boardplay[y][x] == False:
            s += boards[bn][y][x]
      print(s * call)
      boarddone[bn] = True


# In[ ]:




