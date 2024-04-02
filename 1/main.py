data = {}
data2 = {}

for i in 'gbolofothonbhggffnt':  
  if i in data:
    data[i] = data[i] + 1
  else:
    data[i] = 1

for i in "bothon":
    if i in data2:
        data2[i] = data2[i] + 1
    else:
        data2[i] = 1

_min = float("inf")

for i in "bothon":
    if data[i] / data2[i] < _min:
        _min = data[i] / data2[i]


print(_min)


