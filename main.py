import webapp2
import logging

import jinja2
import os

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

#-----------------------------------------------------


#-----------------------------------------------------
class Handler (webapp2.RequestHandler):





#---------------APP ROUTING---------------------------

app = webapp2.WSGIApplication([
  ('/blogjson.?', MainPage),
  ('/blogjson/newpost.?', NewPost),
  ('/blogjson/flush.?', ClearCache),
  webapp2.Route(r'/blogjson/<post_id:\d+>', handler=PostHandler),
  webapp2.Route(r'/blogjson/<post_id:\d*>.json', handler=jsonHandler),
  ('/blogjson/welcome.*',WelcomeHandler),
  ('/blogjson/signup', Register),
  ('/blogjson/login', Login),
  ('/blogjson/logout', Logout),
], debug=True)
