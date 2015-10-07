# -*- coding: utf-8 -*-

lower = -20
upper = 140
step = 10

cels = lower
while ( cels < upper ):
	fahr = 9./5 * cels + 32
	print '%6.3f°C = %6.1f°F' % (cels, fahr)
	cels += step

