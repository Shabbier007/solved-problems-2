# first sort the array descending with respect to the profit of each job
# find the maxi deadline from the jobs jobs[1]
# create an array of maximum deadline and initialize it -1
# iterate from the end of the dead list and check if any -1 exist then update that index with the profit
# return maximum profit and count of no of jobs
# time complexity O(nlogn) + O(nxm)


Jobs = [(1,4,20),(2,1,10),(3,1,40),(4,1,30)]
Jobs.sort(key = lambda y : y[2], reverse= True)
print(Jobs)
max_ = 0
for i in Jobs:
    if max_ < i[1]:
        max_ = i[1]
dead = [-1 for i in range(max_)]
countJobs, profit = 0, 0
for i in Jobs:
    for j in range(i[1]-1, -1, -1):
        if dead[j] == -1:
            dead[j] = i[0]
            countJobs += 1
            profit += i[2]
            break
print(dead)
print(countJobs, profit)


def JobScheduling(self, Jobs, n):
    # code here
    Jobs.sort(key=lambda Jobs: Jobs.profit, reverse=True)

    max_ = 0
    for i in Jobs:
        if max_ < i.deadline:
            max_ = i.deadline
    dead_line = [-1 for i in range(max_)]
    countJobs, profit = 0, 0
    for i in Jobs:
        for j in range(i.deadline - 1, -1, -1):
            if dead_line[j] == -1:
                countJobs += 1
                profit += i.profit
                dead_line[j] = i.id
                break
    return [countJobs, profit]
