# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxt.async_support.eqonex import eqonex


class equos(eqonex):

    def describe(self):
        return self.deep_extend(super(equos, self).describe(), {
            'id': 'equos',
            'name': 'EQUOS',
            'urls': {
                'logo': 'https://user-images.githubusercontent.com/1294454/107758499-05edd180-6d38-11eb-9e09-0b69602a7a15.jpg',
            },
        })
