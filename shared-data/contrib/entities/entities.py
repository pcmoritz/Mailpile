import datetime

import spacy
from spacy import displacy

from mailpile.commands import Command
from mailpile.i18n import gettext as _
from mailpile.mailutils.emails import Email
from mailpile.plugins.search import View
from mailpile.util import *

nlp = spacy.load('en')

class EntityView(View):

    @classmethod
    def view(cls, result):
        mid = result["message_ids"][0]
        messages = result["data"]["messages"][mid]
        plaintext = messages['text_parts'][0]['data']
        entities = displacy.render(nlp(plaintext), style="ent")
        return {"message": result["data"]["messages"][mid],
                "metadata": result["data"]["metadata"][mid],
                "entities": entities}
