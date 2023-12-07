def binarySearch(data, search_elem):
  l = 0
  h = len(data) - 1
  while l<=h:
    m = (l + h) // 2
    mid_elem = data[m]
    print(m, mid_elem)
    if search_elem<mid_elem:
      h = m - 1
    elif search_elem>mid_elem:
      l = m + 1
    else:
      return m+1


data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120, 140, 160, 180]
search_elem = 180
index = binarySearch(data, search_elem)
print(f"Element {search_elem} is found at the index of {index}")
