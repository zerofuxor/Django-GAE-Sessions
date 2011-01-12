Django GAE Sessions
===================

Django GAE Sessions is a Django session engine to work with Google App Engine.

Installing Django GAE Sessions
------------------------------

1. Copy the `sessions` directory to your App Engine project directory, or as a
   zip, so Python's zipimporter can find it.
2. Uncomment the line in `settings.py`:
        
        MIDDLEWARE_CLASSES = (
        ...
            'django.contrib.sessions.middleware.SessionMiddleware',
        ...
        )
        
3. Set the `SESSION_ENGINE` setting to:
        
        SESSION_ENGINE = 'sessions.engine'

   or if you place your external dependencies in a folder like `lib`, you can write:

        SESSION_ENGINE = 'lib.sessions.engine'

That's it.
