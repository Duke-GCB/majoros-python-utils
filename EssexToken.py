#!/bin/env python
#=========================================================================
# This is OPEN SOURCE SOFTWARE governed by the Gnu General Public
# License (GPL) version 3, as described at www.opensource.org.
# Copyright (C)2016 William H. Majoros (martiandna@gmail.com).
#=========================================================================
from __future__ import (absolute_import, division, print_function, 
   unicode_literals, generators, nested_scopes, with_statement)
from builtins import (bytes, dict, int, list, object, range, str, ascii,
   chr, hex, input, next, oct, open, pow, round, super, filter, map, zip)

######################################################################
# Represents a token in a Essex file --- either a parenthesis or a
# literal (a literal is anything other than a parenthesis: a tag/ident-
# ifier, number, or string).  Note that the scanner can't differentiate
# between a tag and a datum, so the parser must do this.
#
# Attributes:
#   tokenType : one of "(", ")", or "L" (literal)
#   lexeme : string
# Methods:
#   token=EssexToken(type,lexeme)
#   type=token.getType()
#   string=token.getLexeme()
#   bool=token.sOpenParen()
#   bool=token.isCloseParen()
#   bool=token.isLiteral()
######################################################################

class EssexToken:
    def __init__(self,type,lexeme=None):
        self.type=type
        if(lexeme is not None and len(lexeme)>0):
            self.lexeme=lexeme

    def getType(self):
        return self.type

    def getLexeme(self):
        return self.lexeme

    def isOpenParen(self):
        return self.type=="("

    def isCloseParen(self):
        return self.type==")"

    def isLiteral(self):
        return self.type=="L"
