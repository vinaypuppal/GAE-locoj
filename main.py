import webapp2
import os
import jinja2 #for templates
from google.appengine.ext import db #for database

template_dir = os.path.join(os.path.dirname(__file__), 'templates') #this tells where templates are present
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True) # autoescape is for escaping html specialchars

class Handler(webapp2.RequestHandler): #custom created class by me 
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)  
    def render(self, template, **kw): #for redering template
        self.write(self.render_str(template, **kw))

class MainPage(Handler):  # class to load main page
    def render_home(self): 
    	self.render("home.html")	
    def get(self):
        self.render_home()

class ProfilePage(Handler):  # class to load main page
    def render_profile(self): 
        self.render("profile.html")    
    def get(self):
        self.render_profile()

class LoopsPage(Handler):  # class to load main page
    def render_loops(self): 
        self.render("loops.html")    
    def get(self):
        self.render_loops()

class EventsPage(Handler):  # class to load main page
    def render_events(self): 
        self.render("events.html")    
    def get(self):
        self.render_events()                        

class PlacesPage(Handler):  # class to load main page
    def render_places(self): 
        self.render("places.html")    
    def get(self):
        self.render_places()

class MessagesPage(Handler):  # class to load main page
    def render_messages(self): 
        self.render("messages.html")    
    def get(self):
        self.render_messages()


app = webapp2.WSGIApplication([
    ('/', MainPage),('/profile',ProfilePage),('/loops',LoopsPage),('/places',PlacesPage),('/events',EventsPage),('/messages',MessagesPage)
], debug=True)
