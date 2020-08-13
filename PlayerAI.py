# -*- coding: utf-8 -*-
"""
Created on Thu May 14 07:54:21 2020

@author: Necro
"""

from random import randint

from BaseAI import BaseAI

 

class PlayerAI(BaseAI):

def getMove(self, grid):

moves = grid.getAvailableMoves()

return moves[randint(0, len(moves) - 1)] if moves else None