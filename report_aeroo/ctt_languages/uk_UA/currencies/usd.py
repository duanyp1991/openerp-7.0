#!/usr/bin/python
# -*- coding: utf8 -*-

from report_aeroo.ctt_objects import ctt_currency

class usd(ctt_currency):
    def _init_currency(self):
        self.language = u'uk_UA'
        self.code = u'USD'
        self.fractions = 100
        self.cur_singular = u' доллара США'
        # default plural form for currency
        self.cur_plural = u' долларов США'
        self.cur_plural_2to4 = u' доллара США'
        self.frc_singular = u' цент'
        # default plural form for fractions
        self.frc_plural = u' центов'
        self.frc_plural_2to4 = u' цента'
        # grammatical genders: f - feminine, m - masculine, n -neuter
        self.cur_gram_gender = 'm'
        self.frc_gram_gender = 'm'
    
usd()
