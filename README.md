Django GAE Sessions
===================

Django GAE Sessions is a django session engine to work with
Google App Engine.

Installing Django GAE Sessions
------------------------------

1. Put session folder under common.
2. uncomment the line:
        
      MIDDLEWARE_CLASSES = (
      ...
      'django.contrib.sessions.middleware.SessionMiddleware',
      ...
      )
        
3. set the session engine to:
        
        SESSION_ENGINE = 'common.sessions.engine'
        