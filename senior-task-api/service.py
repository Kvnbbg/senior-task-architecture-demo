from typing import Dict, List, Optional
from datetime import datetime, timezone
from models import Task, TaskCreate, TaskUpdate, TaskStatus


class TaskService:
    """Isolated business logic for task management.
    In-memory for demo; in production inject a repository.
    """

    def __init__(self) -> None:
        self._tasks: Dict[int, Task] = {}
        self._next_id: int = 1

    def create(self, data: TaskCreate) -> Task:
        now = datetime.now(timezone.utc)
        task = Task(
            id=self._next_id,
            title=data.title,
            description=data.description,
            priority=data.priority,
            due_date=data.due_date,
            status=TaskStatus.TODO,
            created_at=now,
            updated_at=now,
        )
        self._tasks[task.id] = task
        self._next_id += 1
        return task

    def get(self, task_id: int) -> Optional[Task]:
        return self._tasks.get(task_id)

    def list(self, status: Optional[TaskStatus] = None) -> List[Task]:
        tasks = list(self._tasks.values())
        if status is not None:
            tasks = [t for t in tasks if t.status == status]
        return sorted(tasks, key=lambda t: t.created_at, reverse=True)

    def update(self, task_id: int, data: TaskUpdate) -> Optional[Task]:
        task = self._tasks.get(task_id)
        if task is None:
            return None

        update_data = data.model_dump(exclude_unset=True)
        if not update_data:
            return task

        updated = task.model_copy(update=update_data)
        updated.updated_at = datetime.now(timezone.utc)
        self._tasks[task_id] = updated
        return updated

    def delete(self, task_id: int) -> bool:
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False
