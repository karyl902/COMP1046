from collections import defaultdict

d = defaultdict(list)
e = defaultdict(set)

d['a'].append(1)
d['a'].append(2)
d['a'].append(3)
d['b'].append(4)
d['b'].append(5)

e['a'].add(1)
e['a'].add(2)
e['a'].add(3)
e['b'].add(4)
e['b'].add(5)

print("d=" + str(d.items()))  
print("e=" + str(e.items())) 