# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    segments = sorted(segments, key=lambda x: (x[1]))
    #write your code here
    while len(segments)>=1:
        correspondingPt = False
        while len(segments)>1 and segments[0].end >= segments[1].start:
            point = 0
            if (segments[0].end < segments[1].end):
                point = segments[0].end
            else:
                point = segments[1].end
            if isAlreadyPoint(points,point) == False:
                correspondingPt = True
                points.append(point)
            del segments[1]
            if len(segments)-1 == 0:
                break

        if correspondingPt == False:
            points.append(segments[0].end)
        del segments[0]

        if len(segments) == 0:
            break

    return points

def isAlreadyPoint(listPts,point):
    try:
        index = listPts.index(point)
    except:
        return False
    return True

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
