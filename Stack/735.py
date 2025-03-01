class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        right_dir, left_dir = [], []

        for a in asteroids:
            if a > 0:
                right_dir.append(a)

            if a < 0:
                left_dir.append(a)

            while len(right_dir) != 0 or len(left_dir) != 0:
                if len(right_dir) != 0 and len(left_dir) != 0:
                    if right_dir[-1] > -left_dir[-1]:
                        left_dir.pop(-1)
                    elif right_dir[-1] < -left_dir[-1]:
                        right_dir.pop(-1)
                    else:
                        right_dir.pop(-1)
                        left_dir.pop(-1)

        return right_dir + left_dir