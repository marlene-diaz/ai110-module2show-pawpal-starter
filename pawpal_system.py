from dataclasses import dataclass, field
from typing import List


@dataclass
class Task:
    # this means bathing, feeding, walking
    action: str
    # this if for scheduling purposes
    time: str
    completed: bool = False

# this will be the completed attribute
    def mark_complete(self):
        self.completed = True

@dataclass
class Pet:
    name: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        self.tasks.append(task)

class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)

class Scheduler:
    def __init__(self, owner):
        self.owner = owner

    def get_all_tasks(self):
        tasks = []
        for pet in self.owner.pets:
            tasks.extend(pet.tasks)
        return tasks

    def sort_tasks(self):
        return sorted(self.get_all_tasks(), key=lambda t: t.time)