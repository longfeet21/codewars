'''
4 kyu
Given a Sudoku data structure with size NxN, N > 0 and √N == integer, write a method to validate if it has been filled out correctly.
The data structure is a multi-dimensional Array, i.e:

Rules for validation

Data structure dimension: NxN where N > 0 and √N == integer
Rows may only contain integers: 1..N (N included)
Columns may only contain integers: 1..N (N included)
'Little squares' (3x3 in example above) may also only contain integers: 1..N (N included)

data1 = [
  [0,2,3, 4,5,6, 7,8,9], [1,2,3, 4,5,6, 7,8,9], [1,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9], [1,2,3, 4,5,6, 7,8,9], [1,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9], [1,2,3, 4,5,6, 7,8,9], [1,2,3, 4,5,6, 7,8,9]
]

data2 = [
  [7,8,4, 1,5,9, 3,2,6],
  [5,3,9, 6,7,2, 8,4,1],
  [6,1,2, 4,3,8, 7,5,9],
  [9,2,8, 7,1,5, 4,6,3],
  [3,5,7, 8,4,6, 1,9,2],
  [4,6,1, 9,2,3, 5,8,7],
  [8,7,6, 3,9,4, 2,1,5],
  [2,4,3, 5,6,1, 9,7,8],
  [1,9,5, 2,8,7, 6,3,4]
]

data3 =[
  [1,2,3, 4,5,6, 7,8,9],
  [2,3,1, 5,6,4, 8,9,7],
  [3,1,2, 6,4,5, 9,7,8], 
  [4,5,6, 7,8,9, 1,2,3],
  [5,6,4, 8,9,7, 2,3,1],
  [6,4,5, 9,7,8, 3,1,2], 
  [7,8,9, 1,2,3, 4,5,6],
  [8,9,7, 2,3,1, 5,6,4],
  [9,7,8, 3,1,2, 6,4,5]
]
'''

from math import sqrt

class Sudoku(object):
    def __init__(self, data):
        self.data = data
        
    def is_valid(self):
        if not self.correct_size(self.data):
            return False
        if not self.correct_number(self.data):
            return False
        if not self.correct_type(self.data):
            return False
        return True
    
    def correct_size(self, data):
        if not len(data) > 0:
            return False
        
        for row in data:
            if not len(row) == len(data):
                return False
        
        for i in range(int(sqrt(len(data)))):
            for j in range(int(sqrt(len(data)))):
                i *= int(sqrt(len(data)))
                j *= int(sqrt(len(data)))
                valid = [False]*len(data)
                for x in range(i, i+int(sqrt(len(data)))):
                    for y in range(j, j+int(sqrt(len(data)))):
                        n = data[x][y]
                        try:
                            valid[n-1] = True
                        except :
                            return False
                return all(valid)

        return True     
    
    def correct_number(self, data):
        col = [x for x in list(zip(*data))]
        for i in range(len(data)):
            for j in range(len(data[i])):
                if not data[i][j] in range(1, len(data)+1):
                    return False

        for i in col:
            if sorted(list(i)) != list(range(1, len(data)+1)):
                return False

        return True
    
    def correct_type(self, data):
        for rows in data:
            for i in rows:
                if not type(i) is int:
                    return False
        
        return True

S = Sudoku(data2)
if S.is_valid():
    print('valid')
else:
    print('nope')