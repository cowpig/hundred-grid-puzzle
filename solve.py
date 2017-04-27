matrix = [
	[
		{ 1: 9, 2: 7, 3: 8, 4: 3, 5: 1, 6: 2, 7: 6, 8: 4, 9: 5}, 
		{ 1: 8, 2: 9, 3: 7, 4: 2, 5: 3, 6: 1, 7: 5, 8: 6, 9: 4}
	], [
		{ 1: 6, 2: 4, 3: 5, 4: 9, 5: 7, 6: 8, 7: 3, 8: 1, 9: 2}, 
		{ 1: 5, 2: 6, 3: 4, 4: 8, 5: 9, 6: 7, 7: 2, 8: 3, 9: 1}
	]
]

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

def mat(corn): 
	row, col = corn
	return matrix[row, col]

def available_corners(n, corner):
	row, col = corner
	return [((row + drow) % 1, (col + dcol) % 1) for drow, dcol in corners[n]]

def neighbors(n, corner):
	return [mat(corn) for corn in available_corners(corner)]
