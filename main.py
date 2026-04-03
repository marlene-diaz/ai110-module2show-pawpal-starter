

from pawpal_system import Owner, Pet, Task, Scheduler

owner = Owner("Marlene")

pet1 = Pet("Dog")
pet2 = Pet("Cat")

owner.add_pet(pet1)
owner.add_pet(pet2)

pet1.add_task(Task("Feed dog", "08:00"))
pet1.add_task(Task("Walk dog", "09:00"))
pet2.add_task(Task("Feed cat", "07:30"))

scheduler = Scheduler(owner)

tasks = scheduler.sort_tasks()

print("Today's Schedule:")
for task in tasks:
    print(f"{task.time} - {task.action}")