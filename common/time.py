"""
Copyright (c) 2018 Genome Research Ltd.

Author: Christopher Harrison <ch12@sanger.ac.uk>

This program is free software: you can redistribute it and/or modify it
under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at
your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero
General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

from datetime import datetime, timedelta, timezone
import json

from common import types as T


__all__ = ["ISO8601", "JSONEncoder", "now", "delta"]


now = lambda: datetime.now(timezone.utc)
delta = timedelta


ISO8601 = "%Y-%m-%dT%H:%M:%SZ%z"

class JSONEncoder(json.JSONEncoder):
    """ JSON encoder that understands datetimes """
    def default(self, obj:T.Any) -> T.Any:
        if isinstance(obj, datetime):
            return obj.strftime(ISO8601)

        # TODO? Serialisation for timedelta

        super().default(obj)
