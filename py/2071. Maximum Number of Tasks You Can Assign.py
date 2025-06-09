class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()

        low, high = 0, min(len(tasks), len(workers))

        while low < high:
            mid = (low + high + 1) // 2
            
            if self.can_assign(tasks, workers, pills, strength, mid):
                low = mid
            else:
                high = mid - 1

        return low

    def can_assign(self, tasks, workers, pills, strength, k):
        task_sublist = tasks[:k]
        usable_workers = workers[-k:]
        worker_list = list(usable_workers)
        usable_workers.sort()

        i = k - 1
        pills_left = pills

        for task_demand in reversed(task_sublist):
            if worker_list and worker_list[-1] >= task_demand:
                worker_list.pop()
            elif pills_left > 0:
                idx = bisect.bisect_left(worker_list, task_demand - strength)

                if idx == len(worker_list):
                    return False
                
                del worker_list[idx]
                pills_left -= 1

            else:
                return False

        return True
