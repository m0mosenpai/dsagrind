# python3
import sys


def compute_min_refills(distance, tank, stops):
	stops.append(distance)
	stops.insert(0,0)
	numRefills = 0
	currentRefill = 0

	# Since last element is the destination, loop through all stops before destination
	while currentRefill < len(stops) - 1:
		# Update last refilled stop
		lastRefill = currentRefill
		# Keep updating position while the next stop is reachable from the current one and you haven't arrived at your destination
		while (currentRefill < len(stops) - 1 and stops[currentRefill + 1] - stops[lastRefill] <= tank):
			currentRefill += 1

		# If next refill stop is not reachable from the last refilled stop, then it's not possible to reach the destination
		if currentRefill == lastRefill:
			return -1
		# If you haven't reached the destination yet, update refill count
		if currentRefill < len(stops) - 1:
			numRefills += 1

	return numRefills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))