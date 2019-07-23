#! /usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from googletrans import Translator
from googletrans import LANGUAGES

__author__ = "bill.li"

FULL_LANGUAGES = dict()
for k, v in LANGUAGES.iteritems():
    FULL_LANGUAGES.update({v: k})


def translate(content):
    translator = Translator()
    target = translator.translate(content, dest=FULL_LANGUAGES["chinese (simplified)"],
                                  src=FULL_LANGUAGES["english"]).text
    return target


if __name__ == '__main__':
    pass
    # print translate("hello")