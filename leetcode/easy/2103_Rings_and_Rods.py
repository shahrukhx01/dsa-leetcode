class Solution:
    def countPoints(self, rings: str) -> int:
        colorMap = {}

        for idx in range(0, len(rings), 2):
            color, key = rings[idx], rings[idx + 1]

            if key in colorMap and color not in colorMap[key]:
                colorMap[key] += color
            elif key not in colorMap:
                colorMap[key] = color

        ringCount = 0
        for ring in colorMap:
            if len(colorMap[ring]) == 3:
                ringCount += 1

        return ringCount
