# Uses python3

'''
	""	b	e   n   y   a   m
""	0	1	2	3	4	5	6
e   1	1	1	2	3	4	5
p   2
h   3
r   4
e   5
m   6

'''

# Time Complexity - O(nm) | Space Complexity - O(nm)
def edit_distance(s, t):
	table = [[i for i in range(len(s) + 1)] for j in range(len(t) + 1)]
	for i in range(1, len(t) + 1):
		table[i][0] = table[i - 1][0] + 1

	for i in range(1, len(t) + 1):
		for j in range(1, len(s) + 1):
			if t[i - 1] == s[j - 1]:
				table[i][j] = table[i - 1][j - 1]
			else:
				table[i][j] = min(table[i][j - 1], table[i - 1][j], table[i - 1][j - 1]) + 1

	return table[-1][-1]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
