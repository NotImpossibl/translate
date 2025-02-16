#
# Copyright 2007 Zuza Software Foundation
#
# This file is part of translate.
#
# translate is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# translate is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

"""
This module represents the Spanish language.

.. note:: As it only has special case code for initial inverted punctuation,
   it could also be used for Asturian, Galician, or Catalan.
"""


from translate.lang import common


class es(common.Common):
    """This class represents Spanish."""

    @classmethod
    def punctranslate(cls, text):
        """Implement some extra features for inverted punctuation."""
        text = super().punctranslate(text)
        # If the first sentence ends with ? or !, prepend inverted ¿ or ¡
        firstmatch = cls.sentencere.match(text)
        # only one sentence (if any) - use entire string
        first = text if firstmatch is None else firstmatch.group()
        # remove trailing whitespace
        first = first.strip()
        # protect against incorrectly handling an empty string
        if not first:
            return text
        if first[-1] == "?":
            text = "¿" + text
        elif first[-1] == "!":
            text = "¡" + text
        return text
