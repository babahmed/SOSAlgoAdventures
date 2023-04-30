def find_board_length(arr):
  if len(arr) == 1:
    return 1  
  arr.sort()
  leftPointer = 0
  rightPointer = len(arr) -1
  mid_point = int((arr[rightPointer] - arr[leftPointer])/2)
  mid_value = arr[0] + mid_point
  closest_index = find_closest_index(arr, mid_value)

  left_size = arr[closest_index] - arr[0]
  right_size = arr[rightPointer] - arr[closest_index]

  board_length = min(left_size, right_size)
  return board_length


def find_closest_index(arr, mid_point):
    closest_num = arr[0]
    closest_index = 0 
    for index, num in enumerate(arr):
        if abs(num - mid_point) < abs(closest_num - mid_point):
            closest_num = num
            closest_index = index
        if num > mid_point:
            break
    return closest_index
    
print(find_board_length([0, 44, 32, 30, 42, 18, 34, 16, 35])) 
print(find_board_length([11, 20, 15])) 
print(find_board_length([15, 20, 9, 11]))
print(find_board_length([9]))

