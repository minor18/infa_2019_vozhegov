from graph import *

def bird(x, y,k):
    polygon([(x,y),(x+40*k,y-20*k),(x+20*k,y-20*k),
         (x,y-10*k),(x-20*k,y-25*k),(x-50*k,y-30*k)])
          

canvasSize(1200, 800)
windowSize(1200, 800)

penSize(1)

penColor(255, 228, 196)
brushColor(255, 228, 196)
rectangle(0, 0, 1200, 170)

penColor(250, 218, 221)
brushColor(250, 218, 221)
rectangle(0, 170, 2500, 340)

penColor(245, 245, 220)
brushColor(245, 245, 220)
rectangle(0, 340, 2500, 510)

penColor("yellow")
brushColor("yellow")
circle(580, 170, 60)


penColor(252, 152, 49)
brushColor(252, 152, 49)
polygon([(7,374),    (14,325),    (54,318),   (81,304), 
         (108,288),  (143,262),   (177,230),  (207,201),
         (247,159),  (293,172),   (312,202),  (462,302), 
         (541,291),  (582,312),   (641,254),  (693,267), 
         (720,240),  (745,238),   (768,230),  (788,218), 
         (806,201),  (816,189),   (829,167),  (842,148), 
         (860,131),  (870,126),   (874,128),  (880,128), 
         (885,130),  (888,133),   (894,140),  (898,149), 
         (953,199),  (999,188),   (1019,193), (1038,203),
         (1077,229), (1117, 207), (1201,250)])

penColor(172, 67, 52)
brushColor(172, 67, 52)
polygon([(0,540),    (0,397),    (9,397),    (31,415),
         (44,384),   (54,363),   (72,339),   (94,324),
         (122,324),  (144,335),  (168,363),  (182,392),
         (193,412),  (204,477),  (208,513),  (262,423),
         (346,466),  (385,359),  (487,382),  (575,447),
         (690,423),  (712,394),  (737,367),  (766,344),
         (792,331),  (819,326),  (841,331),  (858,341),
         (887,368),  (919,392),  (950,412),  (980,424),
         (1033,360), (1082,396), (1106,354), (1154,360),
         (1200,284), (1200,514)])

penColor(179, 134, 148)
brushColor(179, 134, 148)
polygon([(0,541), (1200,514), (1200,800), (0,800)])

penColor(48, 16, 38)
brushColor(48, 16, 38)
polygon([(0,800),(0,411),(140,448),(260,594),(371,744),(410,772),(560,787),(758,679),
         (813,702),(865,723),(933,715),(1115,537),(1169,494),
         (1200,483),(1200,800)])

penColor(66, 33,11)
brushColor(66, 33,11)
bird(934,642,1.4)
bird(953,581,0.9)
bird(817,602,1)
bird(752,544,1.15)

bird(476,374,1)
bird(569,341,1)
bird(570,300,1)
bird(461,290,1)

