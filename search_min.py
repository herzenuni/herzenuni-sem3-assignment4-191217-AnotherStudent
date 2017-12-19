def search_min(array):
	def mul(x, y, z):
		if (type(x) != int) or (type(y) != int) or (type(z) != int):
			raise ValueError('bad arguments!')
		return x * y * z


	if type(array) != list:
		raise ValueError('array isn''t list!')		

	if len(array) < 3:
		raise ValueError('len too few!')

	minimal = mul(array[0], array[1], array[2])
	counter = 0
	for x in range(len(array)):
		for y in range(x + 1, len(array)):
			for z in range(y + 1, len(array)):
				temp = mul(array[x], array[y], array[z])
				if temp < minimal:
					minimal = temp

	return minimal

if __name__ == "__main__":
	print(search_min([1, 2, -10, 0, 100, 1000]))