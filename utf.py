'''
### ``utf`` module provides characters and symbols used very often when creating TUI
applications.

#### Within this module, you will find objects for:
* ``utf.box`` - drawing boxes (tables).
'''

from typing import Literal as _L

class box:
	'''
	### This class contains box drawing symbols.

	The naming used in this class and its children is very specific, to ensure
	that minimum-length token is required to bring specific character - tokens
	that are typed as ``box.{a}.{b}`` use this notation:

	#### First, ``{a}`` denotes which part of box does this character belong to.
	
	Sides are denoted as:

	* ``t`` - top,
	* ``r`` - right,
	* ``b`` - bottom,
	* ``l`` - left.

	Additionally, two characters can be used to get corner (ex.
	``tr`` - top-right vertical direction first), or span (ex. 
	``tb`` - top-bottom, top/left first), and two additional classes are
	provided:

	* ``cr`` - "CRoss" symbols, that go into all 4 directions,
	* ``ot`` - "OTher" symbols, namely diagonal characters.

	#### Second, ``{b}`` denotes which parts of symbol are formatted in what way.

	Using notation from center (@) of symbol, each arm is named in its direction::

		.T.
		L@R
		.B.
	
	This allows to name each part according to its formatting - using additional
	order rules:
	* in corners, vertical direction first,
	* in sides, fist top/left part of major part (spanning full height/width) is
	used, then minor part (spanning half / pointing inside of box), then other
	major part.

	For example:

	* ``"┌"`` is ``box.tl.tl``,
	* ``"├"`` is ``box.l.trb``.

	Additionally, letter case (and count) is significant, as it denotes
	formatting:

	* lower-case single letter - thin line,
	* upper-case single letter - thick line,
	* lower-case two letters - double line.

	For example:

	* ``"┪"`` is ``box.r.tLB`.

	Dotted lines are only used in spans, so they are written
	as ``[d/D]{number}``, where:
	* case of ``d`` is used for thin/thick line,
	* {number} is how many "dots" (or lines) are inside line.
	
	For example:

	* ``"┉"`` is ``box.lr.D4`.

	Partial spans are denoted as ``[t/r/b/l]_``.
	
	For example:

	* ``"╺"`` is ``box.lr.R_`.

	Finally:

	* arcs/rounded corners are denoted simply as ``A``,
	* diagonals use letters that "touch their corners":
	  * ``"╱"`` is ``J``,
	  * ``"╲"`` is ``L``,
	  * ``"╳"`` is ``X``.

	'''
	class t:
		'''
		Top-side borders
		'''

	class tr:
		'''
		Top-right corners
		'''
	
	class r:
		'''
		Right-side borders
		'''
	
	class br:
		'''
		Bottom-right corners
		'''
	
	class b:
		'''
		Bottom-side borders
		'''
	
	class bl:
		'''
		Bottom-left corners
		'''
	
	class l:
		'''
		Left-side borders
		'''
	
	class tl:
		'''
		Top-left corners
		'''
	
	class tb:
		'''
		Top-to-bottom borders
		'''

	class lr:
		'''
		Left-to-right borders
		'''

	class cr:
		'''
		"Cross" borders (all 4 directions)
		'''
	
	class ot:
		'''
		Other borders (diagonals)
		'''
