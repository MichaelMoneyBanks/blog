import webapp2
import re

form = """
<!DOCTYPE html>
<html>
<head>
    <title>User Sign Up</title>
</head>
<body>
    <h1>User Sign Up</h1>
<h3>Please complete the following.</h3>
<form method = "post">
    <label>
        Username:
        <input type="text" name="username" value=%(username)s>
        <p><div style='color: red'>%(username_error)s</div></p>
    </label>
    <br>
    <label>
        Password:
        <input type="password" name="password" value=>
        <p><div style='color: red'>%(password_error)s</div></p>
    </label>
    <br>
    <label>
        Confirm Password:
        <input type="password" name="verify" value=>
        <p><div style='color: red'>%(verify_error)s</div></p>
    </label>
    <br>
    <label>
        Email (Optional):
        <input type="text" name="email" value=%(email)s>
        <p><div style='color: red'>%(email_error)s</div><p>
    </label>
    <br>
    <br>
    <input type="submit" name="Submit">
</form>
</body>
</html>
"""

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PASS_RE = re.compile(r".{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE = re.compile(r'^[\S]+@[\S]+\.+[\S]+$')
def valid_email(email):
    return not email or EMAIL_RE.match(email)



class MainHandler(webapp2.RequestHandler):

    def write_form(self, username="", username_error="", password_error="", verify_error="", email="", email_error=""):
        self.response.out.write(form % {"username":username, "username_error":username_error, "password_error":password_error, "verify_error":verify_error, "email":email, "email_error":email_error})

    def get(self):
        self.write_form()

    def post(self):

        have_error = False
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')
        verify_error = ""
        email_error = ""
        password_error = ""
        username_error = ""

        if not valid_username(username):
            username_error = "That's not a valid username."
            have_error = True

        if not valid_password(password):
            password_error = "That's not a valid password."
            have_error = True

        if password != verify:
            verify_error = "Does not match password."
            have_error = True

        if not valid_email(email):
            email_error = "That's not a valid email."
            have_error = True

        if have_error:
            self.write_form(username, username_error, password_error, verify_error, email, email_error)
        else:
            self.redirect('/login?username=' + username)



class Login(webapp2.RequestHandler):


    def get(self):

        username = self.request.get('username')

        welcome ="""<p>Thanks you for registering %s!</p>""" % username

        self.response.out.write(welcome)




app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/login', Login)
], debug=True)
