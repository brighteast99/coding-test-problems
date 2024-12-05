import heapq


class Job:
    def __init__(self, time, workload):
        self.time = time
        self.workload = workload

    def __lt__(self, other):
        if self.workload != other.workload:
            return self.workload < other.workload
        if self.time != other.time:
            return self.time < other.time
        return False


def solution(jobs):
    jobs.sort()
    jobs = [Job(s, l) for (s, l) in jobs]
    task_queue = []
    completed = []

    t = 0
    while len(task_queue) + len(jobs) > 0:
        if len(task_queue) > 0:
            cur_job = heapq.heappop(task_queue)
        else:
            cur_job = jobs.pop(0)
        t = max(t, cur_job.time)
        t += cur_job.workload
        completed.append(t - cur_job.time)

        while len(jobs) and t >= jobs[0].time:
            heapq.heappush(task_queue, jobs.pop(0))

    return sum(completed) // len(completed)
