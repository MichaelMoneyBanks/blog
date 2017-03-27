class Post:
    def __init__(self, title, author, body):
        self.title = title
        self.author = author
        self.body = body
        self.likes = 0

    def like(self):
        self.likes += 1

    def __str__(self):
        return self.title + " by " + self.author
