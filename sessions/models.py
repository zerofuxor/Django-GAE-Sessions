# Copyright 2010 Jose Maria Zambrana Arze
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by post law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import base64
import cPickle as pickle

from google.appengine.ext import db
from django.conf import settings
from django.utils.hashcompat import md5_constructor

class Session(db.Model):
  """Django compatible App Engine Datastore session model."""
  session_key = db.StringProperty()
  session_data = db.TextProperty()
  expire_date = db.DateTimeProperty()
  
  def get_decoded(self):
    """
    Returns the session data decoded as a dictionary.
    """
    encoded_data = base64.decodestring(self.session_data)
    pickled, tamper_check = encoded_data[:-32], encoded_data[-32:]
    tamper_gen = md5_constructor(pickled + settings.SECRET_KEY).hexdigest()
    if tamper_gen != tamper_check:
      from django.core.exceptions import SuspiciousOperation
      raise SuspiciousOperation, "User tampered with session cookie."
    try:
      return pickle.loads(pickled)
    except:
      return {}

  @staticmethod
  def encode(session_dict):
    """
    Returns the given session dictionary pickled and encoded as a string.
    """
    pickled = pickle.dumps(session_dict)
    pickled_md5 = md5_constructor(pickled + settings.SECRET_KEY).hexdigest()
    return base64.encodestring(pickled + pickled_md5)

  @staticmethod
  def save(session_key, session_dict, expire_date):
    """
    Saves session data if exists or creates a new one.
    """
    s = Session.get_session(session_key)
    if not s:
      s = Session(session_key=session_key, session_data=session_dict,
                  expire_date=expire_date)
    else:
      s.session_data = session_dict
      s.expire_date = expire_date
      
    if session_dict:
        s.put()
    else:
        s.delete() # Clear sessions with no data.
    return s

  @staticmethod
  def get_session(session_key, expire_date=None):
    """
    Get session object
    """
    query = Session.all().filter('session_key = ', session_key)
    
    if expire_date is not None:
      query.filter('expire_date >', expire_date)
      
    return query.get()