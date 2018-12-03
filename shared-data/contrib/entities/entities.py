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
        messages = result["data"]["messages"][mid]
        plaintext = messages['text_parts'][0]['data']
        return {"message": result["data"]["messages"][mid],
                "metadata": result["data"]["metadata"][mid],
                "plaintext": plaintext}
