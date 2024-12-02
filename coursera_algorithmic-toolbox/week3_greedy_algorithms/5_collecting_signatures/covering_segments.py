# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    count = 0
    # Sorting availability times based on ending time
    segments.sort(key=lambda x:x[1])

    # Keep a track of the end point of the first segment and append it to the final list of points.
    last_end = segments[0].end
    points.append(last_end)

    # Check if saved end point is part of next segment. 
    # If it's not, save it as a new end point (end of a new disjoint segment) and append to final list of points. Continue otherwise.
    for i in range(1, len(segments)):
        if last_end < segments[i].start or last_end > segments[i].end:
            last_end = segments[i].end
            points.append(last_end)

    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
