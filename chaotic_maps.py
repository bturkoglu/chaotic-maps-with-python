import math
from operator import mod


def chaos(Index, Initial_Value, Max_iter):
	x = [0.0] * (Max_iter + 1)
	G = [0.0] * (Max_iter + 1)
	x[1] = Initial_Value

	if Index == 1: #Chebyshev map
		for i in range(1, Max_iter):
			deger = math.cos((i) * math.acos(x[i]))
			x[i + 1] = deger
			G[i] = ((x[i] + 1) * 100) / 2

	if Index == 2: #Circle map
		a = 0.5
		b = 0.2
		for i in range(1, Max_iter):
			x[i + 1] = mod(x[i] + b - (a / (2 * math.pi)) * math.sin(2 * math.pi * x[i]), 1)
			G[i] = x[i] * 100

	if Index == 3: #Gauss/mouse map
		for i in range(1, Max_iter):
			if x[i] == 0:
				x[i + 1] = 0
			else:
				x[i + 1] = mod(1 / x[i], 1)
			G[i] = x[i] * 100

	if Index == 4: #Iterative map
		a = 0.7
		for i in range(1, Max_iter):
			x[i + 1] = math.sin((a * math.pi) / x[i])
			G[i] = ((x[i] + 1) * 100) / 2
		# normalize it from [-1 1] to [0 1]
		a,b,c,d =-1, 1, 0, 1
		for i in range(1, Max_iter+1):
			x[i] =((x[i]-a)*(d-c))/(b-a)

	if Index == 5: #Logistic map
		a = 4
		for i in range(1, Max_iter):
			x[i + 1] = a * x[i]*(1-x[i])
			G[i] = x[i] * 100

	if Index == 6: #Piecewise map
		P = 0.4
		for i in range(1, Max_iter):
			if 0 <= x[i] < P:
				x[i + 1] = x[i] / P
			if P <= x[i] < 0.5:
				x[i + 1] = (x[i] - P) / (0.5 - P)
			if 0.5 <= x[i] < 1 - P:
				x[i + 1] = (1 - P - x[i]) / (0.5 - P)
			if 1 - P <= x[i] < 1:
				x[i + 1] = (1 - x[i]) / P

			G[i] = x[i] * 100

	if Index == 7: #Sine map
		for i in range(1, Max_iter):
			x[i + 1] = math.sin(math.pi * x[i])
			G[i] = x[i] * 100

	if Index == 8: #Singer map
		u = 1.07
		for i in range(1, Max_iter):
			x[i + 1] = u * ( 7.86 * x[i] - 23.31 * (x[i]**2) + 28.75*(x[i]**3)-13.302875*(x[i]**4))
			G[i] = x[i] * 100

	if Index == 9: #Sinusoidal map
		for i in range(1, Max_iter):
			x[i + 1] = 2.3 * x[i] ** 2 * math.sin(math.pi * x[i])
			G[i] = x[i] * 100

	if Index == 10: #Tent map
		x[1] = 0.6
		for i in range(1, Max_iter):
			if x[i] < 0.7:
				x[i + 1] = x[i] / 0.7
			if x[i] >= 0.7:
				x[i + 1] = (10.0/3) * (1 - x[i])

			G[i] = x[i] * 100

	return x[1:]


if __name__ == '__main__':
	gelen = chaos(10, 0.7, 11)
	for i in gelen:
		print(i)
