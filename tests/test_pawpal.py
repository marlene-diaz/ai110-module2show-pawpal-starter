from pawpal_system import Task, Pet

def test_task_complete():
    task = Task("Feed", "08:00")
    task.mark_complete()
    assert task.completed == True

def test_add_task():
    pet = Pet("Dog")
    pet.add_task(Task("Walk", "09:00"))
    assert len(pet.tasks) == 1
    