def next_at_corner(corn):
	matrix = [
		[
			{ 1: 9, 2: 7, 3: 8, 4: 3, 5: 1, 6: 2, 7: 6, 8: 4, 9: 5}, 
			{ 1: 8, 2: 9, 3: 7, 4: 2, 5: 3, 6: 1, 7: 5, 8: 6, 9: 4}
		], [
			{ 1: 6, 2: 4, 3: 5, 4: 9, 5: 7, 6: 8, 7: 3, 8: 1, 9: 2}, 
			{ 1: 5, 2: 6, 3: 4, 4: 8, 5: 9, 6: 7, 7: 2, 8: 3, 9: 1}
		]
	]
	row, col = corn
	return matrix[row][col]

def available_corners(n, corner):
	corners = {
		1: ((1, 0), (0, 1)),
		2: ((1, 1), (0, 1)),
		3: ((1, 1), (0, 1)),
		4: ((1, 0), (1, 1)),
		5: ((1, 0), (0, 1), (1, 1)),
		6: ((1, 0), (0, 1), (1, 1)),
		7: ((1, 0), (1, 1)),
		8: ((1, 0), (0, 1), (1, 1)), 
		9: ((1, 0), (0, 1), (1, 1)),
	}
	row, col = corner
	return [((row + drow) % 2, (col + dcol) % 2) for drow, dcol in corners[n]]

def describe(n, corner):
	corner_descriptions = {
		(0,0): "tl",
		(1,0): "tr",
		(0,1): "bl",
		(1,1): "br",
	}
	return "{}_{}".format(n, corner_descriptions[corner])

def build_tree(n, corner, n_seen=None):
	n_seen = n_seen or []

	output = []

	print('build_tree', n, corner, n_seen)
	label = describe(n, corner)

	for next_corner in available_corners(n, corner):
		next_n = next_at_corner(next_corner)[n]
		if next_n not in n_seen:
			output.append((label, build_tree(next_n, next_corner, n_seen + [n])))

	return output


print(build_tree(1, (0,0)))
