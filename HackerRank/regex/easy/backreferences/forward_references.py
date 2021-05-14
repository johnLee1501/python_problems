"""
Task

You have a test string S.
Your task is to write a regex which will match , with following condition(s):

S consists of tic or tac.
tic should not be immediate neighbour of itself.
The first tic must occur only when tac has appeared at least twice before.
Valid S

tactactic
tactactictactic

Invalid S

tactactictactictictac
tactictac

SOLUTION:$Regex_Pattern = '/^tac(tac(tic)?)*$/';
"""