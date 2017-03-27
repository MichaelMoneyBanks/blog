from Post import Post
class LinkPost(Post):
    def __init__(self, title, author, url):
        super().__init__(self, title, author, None)
        self.link_url = url
        self.clicks = 0


    def click(self):
        self.clicks += 1


    def __str__(self):
        return "Title: " + self.title + " Author: " + self.author + "Url: " + self.link_url + " has " + self.clicks + " clicks."
