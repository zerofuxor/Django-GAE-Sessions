Django GAE Sessions
===================

Django GAE Sessions is a django session engine to work with
Google App Engine.

Installing Django GAE Sessions
------------------------------

1. Put session folder under common.
2. uncomment the line:
<<<<<<< HEAD
>    MIDDLEWARE_CLASSES = (
>      ...
>      'django.contrib.sessions.middleware.SessionMiddleware',
>      ...
>    )
3. set the session engine to:
>  SESSION_ENGINE = 'common.sessions.engine'
=======
    MIDDLEWARE_CLASSES = (
      ...
      'django.contrib.sessions.middleware.SessionMiddleware',
      ...
    )
3. set the session engine to:
  SESSION_ENGINE = 'common.sessions.engine'
>>>>>>> 4d82e057e9a93980e4a127c0d5254cb362e51fde
