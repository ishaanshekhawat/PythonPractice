# https://datalemur.com/questions/python-idle-gpu-days

def gpu_idle_days(days, training_sessions):
	ls = []
	for i in range(1, days + 1):
	  ls.append(i)
	  
	for i in training_sessions:
	  for j in range(i[0], i[1]+1):
	    if j in ls:
	      ls.remove(j)
	      
	return len(ls)
