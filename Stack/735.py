class Solution:
    def asteroidCollision(self, asteroids):
        stack = []

        for ast in asteroids:

            while stack and ast < 0 < stack[-1]:

                if -ast > stack[-1]:
                    stack.pop()
                    continue

                elif -ast == stack[-1]:
                    stack.pop()
                break

            else:
                stack.append(ast)






if __name__ == '__main__':
    s = Solution()
    # asteroids = [5, 10, -5]
    # asteroids = [8, -8]
    # asteroids = [10, 2, -5]
    asteroids = [-2, -1, 1, 2]
    print(s.asteroidCollision(asteroids))