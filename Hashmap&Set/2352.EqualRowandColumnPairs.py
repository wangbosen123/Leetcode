## list 以及 tuple 解決
class Solution:
    def equalPairs(self, grid):
        rmap, cmap = [], []
        row, col = len(grid), len(grid[0])

        for r in range(row):
            rmap.append(tuple(grid[r]))

        for c in range(col):
            cmap.append(tuple(grid[r][c] for r in range(row)))

        count = 0
        for col in cmap:
            count += rmap.count(col)
        return count

class Solution:
    def equalPairs(self, grid):
        n = len(grid)
        count = 0
        rows = {}

        for r in range(n):
            row = tuple(grid[r])
            rows[row] = 1 + rows.get(row, 0)


        for c in range(n):
            col = tuple(grid[i][c] for i in range(n))
            count += rows.get(col, 0)

        return count


if __name__ == '__main__':
    gird = [[3, 1, 2, 2],
            [1, 4, 4, 5],
            [2, 4, 2, 2],
            [2, 4, 2, 2]]

    s = Solution()
    s.equalPairs(gird)
