from datetime import date
import pytest
from models import TaskCreate, TaskUpdate, Priority, TaskStatus
from service import TaskService


@pytest.fixture
def service() -> TaskService:
    return TaskService()


def test_create_task(service: TaskService) -> None:
    data = TaskCreate(title="Write senior PR", priority=Priority.HIGH)
    task = service.create(data)
    assert task.id == 1
    assert task.title == "Write senior PR"
    assert task.priority == Priority.HIGH
    assert task.status == TaskStatus.TODO
    assert task.created_at == task.updated_at


def test_title_stripped_and_validated(service: TaskService) -> None:
    data = TaskCreate(title="  Clean title  ")
    task = service.create(data)
    assert task.title == "Clean title"


def test_blank_title_rejected() -> None:
    with pytest.raises(ValueError):
        TaskCreate(title="   ")


def test_get_and_list(service: TaskService) -> None:
    service.create(TaskCreate(title="A"))
    service.create(TaskCreate(title="B", priority=Priority.LOW))
    assert service.get(1) is not None
    assert service.get(999) is None
    tasks = service.list()
    assert len(tasks) == 2
    assert tasks[0].title == "B"  # newest first


def test_update(service: TaskService) -> None:
    task = service.create(TaskCreate(title="Original"))
    updated = service.update(task.id, TaskUpdate(title="Updated", status=TaskStatus.IN_PROGRESS))
    assert updated is not None
    assert updated.title == "Updated"
    assert updated.status == TaskStatus.IN_PROGRESS
    assert updated.updated_at > task.created_at


def test_update_not_found(service: TaskService) -> None:
    assert service.update(999, TaskUpdate(title="X")) is None


def test_delete(service: TaskService) -> None:
    task = service.create(TaskCreate(title="To delete"))
    assert service.delete(task.id) is True
    assert service.get(task.id) is None
    assert service.delete(task.id) is False


def test_list_by_status(service: TaskService) -> None:
    t1 = service.create(TaskCreate(title="Todo"))
    service.create(TaskCreate(title="Other"))
    service.update(t1.id, TaskUpdate(status=TaskStatus.DONE))
    done = service.list(status=TaskStatus.DONE)
    assert len(done) == 1
    assert done[0].title == "Todo"
