from Post import Post
class ImagePost(Post):
    def __init__(self, title, author, file_name):
        super().__init__(title, author, None)
        self.file_name = file_name

    def __str__(self):
        return "Title: " + self.title + " Author: " + self.author + " File name: " + self.file_name

print(ImagePost("Cat in a hat", "Mike", "the_hat_cat"))
