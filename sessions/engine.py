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

import datetime

from common.sessions.models import Session

from django.contrib.sessions.backends.base import SessionBase
from django.core.exceptions import SuspiciousOperation
from django.utils.encoding import force_unicode

class SessionStore(SessionBase):
  """
  Implements database session store.
  """
  def load(self):
    try:
      s = Session.get_session(
        session_key = self.session_key,
        expire_date = datetime.datetime.now()
      )
    except (SuspiciousOperation):
      s = None
      self.create()
      
    if s:
      return self.decode(force_unicode(s.session_data))
    return {}

  def exists(self, session_key):
    try:
      session_data = Session.get_session(session_key)
    except (SuspiciousOperation):
      session_data = None

    if session_data:
      return True
    return False

  def create(self):
    self.session_key = self._get_new_session_key()
    self.save(must_create=True)
    self.modified = True
    self._session_cache = {}

  def save(self, must_create=False):
    data = self._get_session(no_load=must_create)
    session = Session.save(
        self.session_key,
        self.encode(data),
        self.get_expiry_date()
    )

  def delete(self, session_key=None):
    if session_key is None:
      if self._session_key is None:
        return
      session_key = self._session_key
    Session.get_session(session_key).delete()
