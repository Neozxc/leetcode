class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.task_info: Dict[int, List[int]] = {}
        self.tasks_heap: List[Tuple[int, int]] = []

        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_info[taskId] = [userId, priority]
        heapq.heappush(self.tasks_heap, (-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        self.task_info[taskId][1] = newPriority
        heapq.heappush(self.tasks_heap, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.task_info:
            del self.task_info[taskId]

    def execTop(self) -> int:
        while self.tasks_heap:
            neg_priority, neg_taskId = self.tasks_heap[0]
            priority = -neg_priority
            taskId = -neg_taskId

            if taskId not in self.task_info:
                heapq.heappop(self.tasks_heap)
                continue

            if self.task_info[taskId][1] != priority:
                heapq.heappop(self.tasks_heap)
                continue

            userId = self.task_info[taskId][0]
            del self.task_info[taskId]
            heapq.heappop(self.tasks_heap)

            return userId

        return -1
