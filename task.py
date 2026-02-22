class Task:
    def __init__(self, id, title, done=False, priority="medium", deadline=None ):
        self.id = id
        self.title = title
        self.done = done
        self.priority = priority
        self.deadline = deadline

    def mark_done(self):
        self.done = True

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "done": self.done,
            "priority":  self.priority,
            "deadline": self.deadline
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["title"],
            data["done"],
            data.get("priority", "medium"),
            data.get("deadline", None)
        )

