import pickle
t = [1, 2, 3, 4, 5]
s = pickle.dumps(t)
t1 = pickle.loads(s)
print t1

