class Task:
    def __init__(self, id, title, done=False):
        self.id = id
        self.title = title
        self.done = done

    def mark_done(self):
        self.done = True

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "done": self.done
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["title"],
            data["done"]
        )

