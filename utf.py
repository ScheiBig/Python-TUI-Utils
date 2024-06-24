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

	* ``"┌"`` is ``box.tl.br``,
	* ``"├"`` is ``box.l.trb``.

	Additionally, letter case (and count) is significant, as it denotes
	formatting:

	* lower-case single letter - normal line,
	* upper-case single letter - heavy line.

	Inside each class (excluding ``ot``), there is also a ``D`` class - it
	changes context of heavy line:

	* outside ``D`` class, heavy means thick line,
	* inside ``D`` class, heavy means double line.

	For example:

	* ``"┪"`` is ``box.r.tLB`,
	* ``"╧"`` is ``box.b.D.LuR``.

	Dotted lines are only used in spans, so they are written
	as ``[d/D]{number}``, where:
	* case of ``d`` is used for thin/thick line,
	* {number} is how many dots/dashes are inside line.

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

	(Please be aware, that symbols in this class-namespace are ordered according
	to explained above property-name encoding, and not unicode
	code-point - which should not matter to the end-user.)
	'''

	class t:
		'''
		Top-side borders
		'''

	class tr:
		'''
		Top-right corners
		'''

		##-------------------------Normal solid lines-------------------------##
		bl: _L["┐"] = "┐"
		'''Box Drawings: **U+2510**( ``┐`` ) - light down and left'''
		bL: _L["┑"] = "┑"
		'''Box Drawings: **U+2511**( ``┑`` ) - down light and left heavy'''
		BL: _L["┓"] = "┓"
		'''Box Drawings: **U+2513**( ``┓`` ) - heavy down and left'''
		Bl: _L["┒"] = "┒"
		'''Box Drawings: **U+2512**( ``┒`` ) - down heavy and left light'''
		
		A: _L["╮"] = "╮"
		'''Box Drawings: **U+256e**( ``╮`` ) - light arc down and left'''
		class D:
			'''
			Top-right corners with double lines
			'''
			bL: _L["╕"] = "╕"
			'''Box Drawings: **U+2555**( ``╕`` ) - down single and left double'''
			BL: _L["╗"] = "╗"
			'''Box Drawings: **U+2557**( ``╗`` ) - double down and left'''
			Bl: _L["╖"] = "╖"
			'''Box Drawings: **U+2556**( ``╖`` ) - down double and left single'''


	class r:
		'''
		Right-side borders
		'''

	class br:
		'''
		Bottom-right corners
		'''

		##-------------------------Normal solid lines-------------------------##
		tl: _L["┘"] = "┘"
		'''Box Drawings: **U+2518**( ``┘`` ) - light up and left'''
		tL: _L["┙"] = "┙"
		'''Box Drawings: **U+2519**( ``┙`` ) - up light and left heavy'''
		TL: _L["┛"] = "┛"
		'''Box Drawings: **U+251b**( ``┛`` ) - heavy up and left'''
		Tl: _L["┚"] = "┚"
		'''Box Drawings: **U+251a**( ``┚`` ) - up heavy and left light'''
		
		A: _L["╯"] = "╯"
		'''Box Drawings: **U+256f**( ``╯`` ) - light arc up and left'''
		class D:
			'''
			Bottom-right corners with double lines
			'''
			tL: _L["╛"] = "╛"
			'''Box Drawings: **U+255b**( ``╛`` ) - up single and left double'''
			TL: _L["╝"] = "╝"
			'''Box Drawings: **U+255d**( ``╝`` ) - double up and left'''
			Tl: _L["╜"] = "╜"
			'''Box Drawings: **U+255c**( ``╜`` ) - up double and left single'''

	class b:
		'''
		Bottom-side borders
		'''

	class bl:
		'''
		Bottom-left corners
		'''

		##-------------------------Normal solid lines-------------------------##
		tr: _L["└"] = "└"
		'''Box Drawings: **U+2514**( ``└`` ) - light up and right'''
		tR: _L["┕"] = "┕"
		'''Box Drawings: **U+2515**( ``┕`` ) - up light and right heavy'''
		TR: _L["┗"] = "┗"
		'''Box Drawings: **U+2517**( ``┗`` ) - heavy up and right'''
		Tr: _L["┖"] = "┖"
		'''Box Drawings: **U+2516**( ``┖`` ) - up heavy and right light'''
		
		A: _L["╰"] = "╰"
		'''Box Drawings: **U+2570**( ``╰`` ) - light arc up and right'''
		class D:
			'''
			Bottom-left corners with double lines
			'''
			tR: _L["╘"] = "╘"
			'''Box Drawings: **U+2558**( ``╘`` ) - up single and right double'''
			TR: _L["╚"] = "╚"
			'''Box Drawings: **U+255a**( ``╚`` ) - double up and right'''
			Tr: _L["╙"] = "╙"
			'''Box Drawings: **U+2559**( ``╙`` ) - up double and right single'''

	class l:
		'''
		Left-side borders
		'''

	class tl:
		'''
		Top-left corners
		'''

		##-------------------------Normal solid lines-------------------------##
		br: _L["┌"] = "┌"
		'''Box Drawings: **U+250c**( ``┌`` ) - light down and right'''
		bR: _L["┍"] = "┍"
		'''Box Drawings: **U+250d**( ``┍`` ) - down light and right heavy'''
		BR: _L["┏"] = "┏"
		'''Box Drawings: **U+250f**( ``┏`` ) - heavy down and right'''
		Br: _L["┎"] = "┎"
		'''Box Drawings: **U+250e**( ``┎`` ) - down heavy and right light'''
		
		A: _L["╭"] = "╭"
		'''Box Drawings: **U+256d**( ``╭`` ) - light arc down and right'''
		class D:
			'''
			Top-left corners with double lines
			'''
			bR: _L["╒"] = "╒"
			'''Box Drawings: **U+2552**( ``╒`` ) - down single and right double'''
			BR: _L["╔"] = "╔"
			'''Box Drawings: **U+2554**( ``╔`` ) - double down and right'''
			Br: _L["╓"] = "╓"
			'''Box Drawings: **U+2553**( ``╓`` ) - down double and rightsingle'''

	class tb:
		'''
		Top-to-bottom borders
		'''

		##-------------------------Normal solid lines-------------------------##
		tb: _L["│"] = "│"
		'''Box Drawings: **U+2502**( ``│`` ) - light vertical'''
		tB: _L["╽"] = "╽"
		'''Box Drawings: **U+257d**( ``╽`` ) - light up and heavy down'''
		TB: _L["┃"] = "┃"
		'''Box Drawings: **U+2503**( ``┃`` ) - heavy vertical'''
		Tb: _L["╿"] = "╿"
		'''Box Drawings: **U+257f**( ``╿`` ) - heavy up and light down'''

		##-----------------------Partials / half lines------------------------##
		t_: _L["╵"] = "╵"
		'''Box Drawings: **U+2575**( ``╵`` ) - light up'''
		T_: _L["╹"] = "╹"
		'''Box Drawings: **U+2579**( ``╹`` ) - heavy up'''
		b_: _L["╷"] = "╷"
		'''Box Drawings: **U+2577**( ``╷`` ) - light down'''
		B_: _L["╻"] = "╻"
		'''Box Drawings: **U+257b**( ``╻`` ) - heavy down'''

		##---------------------------Dashed lines-----------------------------##
		d2: _L["╎"] = "╎"
		'''Box Drawings: **U+254e**( ``╎`` ) - light double dash vertical'''
		D2: _L["╏"] = "╏"
		'''Box Drawings: **U+254f**( ``╏`` ) - heavy double dash vertical'''
		d3: _L["┆"] = "┆"
		'''Box Drawings: **U+2506**( ``┆`` ) - light triple dash vertical'''
		D3: _L["┇"] = "┇"
		'''Box Drawings: **U+2507**( ``┇`` ) - heavy triple dash vertical'''
		d4: _L["┊"] = "┊"
		'''Box Drawings: **U+250a**( ``┊`` ) - light quadruple dash vertical'''
		D4: _L["┋"] = "┋"
		'''Box Drawings: **U+250b**( ``┋`` ) - heavy quadruple dash vertical'''
		
		class D:
			'''
			Top-to-bottom borders with double lines
			'''
			TB: _L["║"] = "║"
			'''Box Drawings: **U+2551**( ``║`` ) - double vertical'''

	class lr:
		'''
		Left-to-right borders
		'''

		##-------------------------Normal solid lines-------------------------##
		lr: _L["─"] = "─"
		'''Box Drawings: **U+2500**( ``─`` ) - light horizontal'''
		lR: _L["╼"] = "╼"
		'''Box Drawings: **U+257c**( ``╼`` ) - light left and heavy right'''
		LR: _L["━"] = "━"
		'''Box Drawings: **U+2501**( ``━`` ) - heavy horizontal'''
		Lr: _L["╾"] = "╾"
		'''Box Drawings: **U+257e**( ``╾`` ) - heavy left and light right'''

		##-----------------------Partials / half lines------------------------##
		l_: _L["╴"] = "╴"
		'''Box Drawings: **U+2574**( ``╴`` ) - light left'''
		L_: _L["╸"] = "╸"
		'''Box Drawings: **U+2578**( ``╸`` ) - heavy left'''
		r_: _L["╶"] = "╶"
		'''Box Drawings: **U+2576**( ``╶`` ) - light right'''
		R_: _L["╺"] = "╺"
		'''Box Drawings: **U+257a**( ``╺`` ) - heavy right'''

		##---------------------------Dashed lines-----------------------------##
		d2: _L["╌"] = "╌"
		'''Box Drawings: **U+254c**( ``╌`` ) - light double dash horizontal'''
		D2: _L["┅"] = "┅"
		'''Box Drawings: **U+2505**( ``┅`` ) - heavy triple dash horizontal'''
		d3: _L["┄"] = "┄"
		'''Box Drawings: **U+2504**( ``┄`` ) - light triple dashhorizontal'''
		D3: _L["╍"] = "╍"
		'''Box Drawings: **U+254d**( ``╍`` ) - heavy double dash horizontal'''
		d4: _L["┈"] = "┈"
		'''Box Drawings: **U+2508**( ``┈`` ) - light quadruple dash horizontal'''
		D4: _L["┉"] = "┉"
		'''Box Drawings: **U+2509**( ``┉`` ) - heavy quadruple dash horizontal'''

		class D:
			'''
			Left-to-right borders with double lines
			'''
			__: _L["═"] = "═"
			'''Box Drawings: **U+2550**( ``═`` ) - double horizontal'''



	class cr:
		'''
		"Cross" borders (all 4 directions)
		'''

	class ot:
		'''
		Other borders (diagonals)
		'''

		J: _L["╱"] = "╱"
		'''Box Drawings: **U+2571**( ``╱`` ) - light diagonal upper right to lower left'''
		L: _L["╲"] = "╲"
		'''Box Drawings: **U+2572**( ``╲`` ) - light diagonal upper left to lower right'''
		X: _L["╳"] = "╳"
		'''Box Drawings: **U+2573**( ``╳`` ) - light diagonal cross'''
