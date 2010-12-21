"""
Python module to give matplotlib some support for colorblind friendly colors.
Ref http://jfly.iam.u-tokyo.ac.jp/color/#pallet
(I reordered the palette to make the colors that are harder to see in lineplots (sky blue, yellow) further down the list, to alternate warm and cool

To use:  

import this module

initialise a generator by creating a name:

colorgen = cudtools.CUDcolorGen()

Then use the next builtin to get the next color from the palette

color = next( colorGen )


TODO:  consider outputting name too
       offer choice of palettes
       
"""

CUDcolorD = {}

CUDcolorD['Black'] = (0,0,0)              # cool
CUDcolorD['Vermillion'] = (0.8,0.4,0)       #warm
CUDcolorD['Blue'] = (0,0.45,0.7)              # cool
CUDcolorD['Orange'] = (0.9,0.6,0)       #warm
CUDcolorD['Bluish Green'] = (0,0.6,0.5)              # cool
CUDcolorD['Reddish Purple'] = (0.8,0.6,0.7)     #warm
CUDcolorD['Sky Blue'] = (0.35,0.7,0.9)              # cool
CUDcolorD['Yellow'] = (0.95,0.9,0.25)       #warm

CUDcolorOrderL=['Black', 'Vermillion', 'Blue', 'Orange', 'Bluish Green', 'Reddish Purple', 'Sky Blue', 'Yellow']


LL = len(CUDcolorOrderL)

def CUDcolorGen() :

    """
    wheels through the colorblind friendly palette to yield the next 
    color, cycling back to start after end.
    """

    idx = 0
    while True :
        yield CUDcolorD[ CUDcolorOrderL[ idx ] ]
        idx = (idx + 1 ) % LL
