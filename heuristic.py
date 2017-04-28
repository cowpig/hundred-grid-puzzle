from brute_force import neighbors

def available(coord, visited):
	return [c for c in neighbors(coord) if c not in visited]

def iso_first_search(coord, visited=None):
	visited = visited or []

	if len(visited) == 99:
		return visited + [n]

	avail = available(n, visited)

	for nxt in sorted(avail, key=lambda n2: len(available(n2, visited))):
		solution = iso_first_search(nxt, visited + [n])
		if solution:
			return solution

	return None

print(iso_first_search((0,0)))
