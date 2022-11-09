sequence1 = "GTTTTAATTTTTAATCTAAATTAAAAGTATAATTATATATTATATTAATATATTCATGTCATCTAGGATAAATATATAAGATATATAATTTAATTAAAAA"
sequence2 = "AAATAATACAAGATCAAATTAATTACCTAATAATATTTATTAATTAATATAATAATTAAAAGTTTATTAAATCATATTATTAATGTTTTTTAAATATTTT"


match = 2
mismatch = -1
gap = 0

sequence1 = '-'+sequence1
sequence2 = '-'+sequence2

grid = [['_' for _ in range(len(sequence2))] for _ in range(len(sequence1))]


def match_check(a,b):
  if a == b:
    return match
  return mismatch

step = 0

for i in range(len(grid[0])):
  grid[0][i] = step

for i in range(len(grid)):
  grid[i][0] = step

for i in range(1,len(sequence1)):
  for j in range(1,len(sequence2)):
    c_match = grid[i-1][j-1] + match_check(sequence1[i], sequence2[j])
    delete = grid[i-1][j] + gap
    insert = grid[i][j-1] + gap
    # if -ve make it 0
    grid[i][j] = max(c_match, insert, delete, 0)


alignment_A = ""
alignment_B = ""
max_i = len(sequence1)-1
max_j = len(sequence2)-1
max_value = float('-inf')

for i in range(len(grid)):
    a_row = grid[i]
    cur_max_value = max(a_row)
    if cur_max_value > max_value:
      j = a_row.index(cur_max_value)
      max_i = i
      max_j = j
      max_value = cur_max_value

i,j = max_i, max_j

while (i > 0 and j > 0 and grid[i][j] > 0):
  if (i > 0 and j > 0 and grid[i][j] == grid[i-1][j-1] + match_check(sequence1[i], sequence2[j])):
    alignment_A = sequence1[i] + alignment_A
    alignment_B = sequence2[j] + alignment_B
    i = i - 1
    j = j - 1
  elif i > 0 and grid[i][j] == grid[i-1][j] - gap:
    alignment_A = sequence1[i] + alignment_A
    alignment_B = "-" + alignment_B
    i = i - 1
  else:
    alignment_A = "-" + alignment_A
    alignment_B = sequence2[j] + alignment_B
    j = j - 1

res = 0
for w1,w2 in zip(alignment_A, alignment_B):
  res += match_check(w1, w2)
 
print(f"{alignment_B}\n{alignment_A}\nScore = {res}")
