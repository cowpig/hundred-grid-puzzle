def is_valid(coord):
	valid = (0,1,2,3,4,5,6,7,8)
	row, col = coord
	return row in valid and col in valid

def add(coord, move):
	return (coord[0] + move[0], coord[1] + move[1])

def neighbors(coord):
	moves = [
		(3,0),
		(-3,0),
		(0,3),
		(0,-3),
		(2,2),
		(-2,2),
		(2,-2),
		(-2,-2),
	]
	return [
		add(coord, move) for move in moves
		if is_valid(add(coord, move))
	]

def dfs(coord, visited=None):
	visited = visited or []

	# print(coord, len(visited))

	if len(visited) == 99:
		return visited + [coord]

	solutions = []

	for neighbor in neighbors(coord):
		if neighbor not in visited:
			solution = dfs(neighbor, visited + [coord])
			if solution:
				solutions.append(solution)

	return solutions

print(dfs((0,0)))