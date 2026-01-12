class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time = 0
        for i in range(len(points) - 1):
            max_x = max(points[i][0], points[i+1][0])
            min_x = min(points[i][0], points[i+1][0])

            max_y = max(points[i][1], points[i+1][1])
            min_y = min(points[i][1], points[i+1][1])

            total_time += max((max_x - min_x), (max_y - min_y))

        return total_time