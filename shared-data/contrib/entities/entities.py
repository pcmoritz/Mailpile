import datetime

from mailpile.commands import Command
from mailpile.i18n import gettext as _
from mailpile.mailutils.emails import Email
from mailpile.plugins.search import View
from mailpile.util import *


class EntityView(View):

    @classmethod
    def view(cls, result):
        mid = result["message_ids"][0]
        print("XXX", result["data"]["messages"][mid])
        return {"message": result["data"]["messages"][mid],
                "metadata": result["data"]["metadata"][mid]}
