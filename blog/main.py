import webapp2
import os
import jinja2
import datetime

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))



class Post(db.Model):
    title = db.StringProperty(required = True)
    post = db.TextProperty(required = True)
    posted = db.DateTimeProperty(auto_now_add = True)

class MainPage(Handler):
    def render_base(self, post_id="", title="", post="", posted="", error=""):
        self.render("base.html", title=title, post=post, posted=posted, error=error)

    def get(self):
        self.render_base()

    def post(self):
        title = self.request.get('title')
        post = self.request.get('post')
        posted = datetime.datetime.now()
        if title and post:
            a = Post(title = title, post = post, posted = posted)
            a.put()
            self.redirect("/blog/" + str(a.key().id()))
        else:
            error = "Please submit a title and a post."
            self.render_base(title, post, error)

class NewPost(Handler):

    def get(self, id):

        postid = Post.get_by_id( int(id) )


        t = jinja_env.get_template("post.html")
        content = t.render(posts = postid, title = self.request.get('title'), posted = self.request.get('posted'), post = self.request.get('post'))
        self.response.write(content)

class Recent(Handler):

    def get(self):

        q = Post.all().order("-posted")
        posts = q.fetch(limit = 5)



        t = jinja_env.get_template("recent.html")
        content = t.render(posts = posts, title = self.request.get('title'), post = self.request.get('post'))
        self.response.write(content)





app = webapp2.WSGIApplication([
    ('/', MainPage),
    webapp2.Route('/blog/<id:\d+>', NewPost),
    ('/recent', Recent)


], debug=True)
