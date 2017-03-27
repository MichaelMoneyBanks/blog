from Post import Post
class VideoPost(Post):
    def __init__(self, title, author, url):
        Post.__init__(self, title, author, None)
        self.video_url = url
        self.plays = 0

    def play(self):
        self.plays += 1

    def __str__(self):
        return self.title + " played " + str(self.plays) + " times"
