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

__all__ = [
    "CannotConnect",
    "NoServerSpecified",
    "NoSuchDistinguishedName",
    "PayloadNotFetched"
]

class CannotConnect(BaseException):
    """ Raised when a connection cannot be established """

class NoServerSpecified(BaseException):
    """ Raised when the LDAP server hasn't been injected """

class NoSuchDistinguishedName(BaseException):
    """ Raised on an invalid DN """

class PayloadNotFetched(BaseException):
    """ Raised when the payload hasn't yet been fetched """
