from collections import deque

class RecentCounter:
    def __init__(self):
        self.recentCounter = deque()

    def ping(self, t: int):
        self.recentCounter.append(t)
        print(self.recentCounter)

        while self.recentCounter[0] < t-3000:
            self.recentCounter.popleft()

        print(self.recentCounter)
        return len(self.recentCounter)



if __name__ == '__main__':
    input = [[], [1], [100], [3001], [3002], [3101]]
    project = RecentCounter()
    # param_1 = project.ping(input[0])
    param_2 = project.ping(input[1][0])
    param_3 = project.ping(input[2][0])
    param_4 = project.ping(input[3][0])
    param_5 = project.ping(input[4][0])
    param_6 = project.ping(input[5][0])
    print(param_2, param_3, param_4, param_5, param_6)
