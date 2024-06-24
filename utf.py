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

		lbr: _L["┬"] = "┬"
		'''Box Drawings: **U+252c**( ``┬`` ) - light down and horizontal'''
		Lbr: _L["┭"] = "┭"
		'''Box Drawings: **U+252d**( ``┭`` ) - left heavy and right down light'''
		lbR: _L["┮"] = "┮"
		'''Box Drawings: **U+252e**( ``┮`` ) - right heavy and leftdown light'''
		lBr: _L["┰"] = "┰"
		'''Box Drawings: **U+2530**( ``┰`` ) - down heavy and horizontal light'''
		
		LbR: _L["┯"] = "┯"
		'''Box Drawings: **U+252f**( ``┯`` ) - down light and horizontal heavy'''
		LBr: _L["┱"] = "┱"
		'''Box Drawings: **U+2531**( ``┱`` ) - right light and left down heavy'''
		lBR: _L["┲"] = "┲"
		'''Box Drawings: **U+2532**( ``┲`` ) - left light and right down heavy'''
		LBR: _L["┳"] = "┳"
		'''Box Drawings: **U+2533**( ``┳`` ) - heavy down and horizontal'''
		
		class D:
			'''
			Top-side borders with double lines
			'''

			LbR: _L["╤"] = "╤"
			'''Box Drawings: **U+2564**( ``╤`` ) - down single and horizontal double'''
			lBr: _L["╥"] = "╥"
			'''Box Drawings: **U+2565**( ``╥`` ) - down double and horizontal single'''
			LBR: _L["╦"] = "╦"
			'''Box Drawings: **U+2566**( ``╦`` ) - double down and horizontal'''

	class tr:
		'''
		Top-right corners
		'''

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

			Bl: _L["╖"] = "╖"
			'''Box Drawings: **U+2556**( ``╖`` ) - down double and left single'''
			bL: _L["╕"] = "╕"
			'''Box Drawings: **U+2555**( ``╕`` ) - down single and left double'''
			BL: _L["╗"] = "╗"
			'''Box Drawings: **U+2557**( ``╗`` ) - double down and left'''

	class r:
		'''
		Right-side borders
		'''

		tlb: _L["┤"] = "┤"
		'''Box Drawings: **U+2524**( ``┤`` ) - light vertical and left'''
		Tlb: _L["┦"] = "┦"
		'''Box Drawings: **U+2526**( ``┦`` ) - up heavy and left down light'''
		tlB: _L["┧"] = "┧"
		'''Box Drawings: **U+2527**( ``┧`` ) - down heavy and left up light'''
		tLb: _L["┥"] = "┥"
		'''Box Drawings: **U+2525**( ``┥`` ) - vertical light and left heavy'''
		
		TlB: _L["┨"] = "┨"
		'''Box Drawings: **U+2528**( ``┨`` ) - vertical heavy and left light'''
		TLb: _L["┩"] = "┩"
		'''Box Drawings: **U+2529**( ``┩`` ) - down light and left up heavy'''
		tLB: _L["┪"] = "┪"
		'''Box Drawings: **U+252a**( ``┪`` ) - up light and left down heavy'''
		TLB: _L["┫"] = "┫"
		'''Box Drawings: **U+252b**( ``┫`` ) - heavy vertical and left'''

		class D:
			'''
			Right-side borders with double lines
			'''

			TlB: _L["╢"] = "╢"
			'''Box Drawings: **U+2562**( ``╢`` ) - vertical double and left single'''
			tLb: _L["╡"] = "╡"
			'''Box Drawings: **U+2561**( ``╡`` ) - vertical single and left double'''
			TLB: _L["╣"] = "╣"
			'''Box Drawings: **U+2563**( ``╣`` ) - double vertical and left'''

	class br:
		'''
		Bottom-right corners
		'''

		tl: _L["┘"] = "┘"
		'''Box Drawings: **U+2518**( ``┘`` ) - light up and left'''
		Tl: _L["┚"] = "┚"
		'''Box Drawings: **U+251a**( ``┚`` ) - up heavy and left light'''
		tL: _L["┙"] = "┙"
		'''Box Drawings: **U+2519**( ``┙`` ) - up light and left heavy'''
		TL: _L["┛"] = "┛"
		'''Box Drawings: **U+251b**( ``┛`` ) - heavy up and left'''
		
		A: _L["╯"] = "╯"
		'''Box Drawings: **U+256f**( ``╯`` ) - light arc up and left'''

		class D:
			'''
			Bottom-right corners with double lines
			'''

			Tl: _L["╜"] = "╜"
			'''Box Drawings: **U+255c**( ``╜`` ) - up double and left single'''
			tL: _L["╛"] = "╛"
			'''Box Drawings: **U+255b**( ``╛`` ) - up single and left double'''
			TL: _L["╝"] = "╝"
			'''Box Drawings: **U+255d**( ``╝`` ) - double up and left'''

	class b:
		'''
		Bottom-side borders
		'''

		ltr: _L["┴"] = "┴"
		'''Box Drawings: **U+2534**( ``┴`` ) - light up and horizontal'''
		Ltr: _L["┵"] = "┵"
		'''Box Drawings: **U+2535**( ``┵`` ) - left heavy and right up light'''
		ltR: _L["┶"] = "┶"
		'''Box Drawings: **U+2536**( ``┶`` ) - right heavy and left up light'''
		lTr: _L["┸"] = "┸"
		'''Box Drawings: **U+2538**( ``┸`` ) - up heavy and horizontal light'''
		
		LtR: _L["┷"] = "┷"
		'''Box Drawings: **U+2537**( ``┷`` ) - up light and horizontal heavy'''
		LTr: _L["┹"] = "┹"
		'''Box Drawings: **U+2539**( ``┹`` ) - right light and left up heavy'''
		lTR: _L["┺"] = "┺"
		'''Box Drawings: **U+253a**( ``┺`` ) - left light and right up heavy'''
		LTR: _L["┻"] = "┻"
		'''Box Drawings: **U+253b**( ``┻`` ) - heavy up and horizontal'''

		class D:
			'''
			Bottom-side borders with double lines
			'''

			LtR: _L["╧"] = "╧"
			'''Box Drawings: **U+2567**( ``╧`` ) - up single and horizontal double'''
			lTr: _L["╨"] = "╨"
			'''Box Drawings: **U+2568**( ``╨`` ) - up double and horizontal single'''
			LTR: _L["╩"] = "╩"
			'''Box Drawings: **U+2569**( ``╩`` ) - double up and horizontal'''


	class bl:
		'''
		Bottom-left corners
		'''

		tr: _L["└"] = "└"
		'''Box Drawings: **U+2514**( ``└`` ) - light up and right'''
		Tr: _L["┖"] = "┖"
		'''Box Drawings: **U+2516**( ``┖`` ) - up heavy and right light'''
		tR: _L["┕"] = "┕"
		'''Box Drawings: **U+2515**( ``┕`` ) - up light and right heavy'''
		TR: _L["┗"] = "┗"
		'''Box Drawings: **U+2517**( ``┗`` ) - heavy up and right'''
		
		A: _L["╰"] = "╰"
		'''Box Drawings: **U+2570**( ``╰`` ) - light arc up and right'''
		
		class D:
			'''
			Bottom-left corners with double lines
			'''

			Tr: _L["╙"] = "╙"
			'''Box Drawings: **U+2559**( ``╙`` ) - up double and right single'''
			tR: _L["╘"] = "╘"
			'''Box Drawings: **U+2558**( ``╘`` ) - up single and right double'''
			TR: _L["╚"] = "╚"
			'''Box Drawings: **U+255a**( ``╚`` ) - double up and right'''

	class l:
		'''
		Left-side borders
		'''

		trb: _L["├"] = "├"
		'''Box Drawings: **U+251c**( ``├`` ) - light vertical and right'''
		Trb: _L["┞"] = "┞"
		'''Box Drawings: **U+251e**( ``┞`` ) - up heavy and right down light'''
		trB: _L["┟"] = "┟"
		'''Box Drawings: **U+251f**( ``┟`` ) - down heavy and right up light'''
		tRb: _L["┝"] = "┝"
		'''Box Drawings: **U+251d**( ``┝`` ) - vertical light and right heavy'''
		
		TrB: _L["┠"] = "┠"
		'''Box Drawings: **U+2520**( ``┠`` ) - vertical heavy and right light'''
		TRb: _L["┡"] = "┡"
		'''Box Drawings: **U+2521**( ``┡`` ) - down light and right up heavy'''
		tRB: _L["┢"] = "┢"
		'''Box Drawings: **U+2522**( ``┢`` ) - up light and right down heavy'''
		TRB: _L["┣"] = "┣"
		'''Box Drawings: **U+2523**( ``┣`` ) - heavy vertical and right'''

		class D:
			'''
			Left-side borders with double lines
			'''

			TrB: _L["╟"] = "╟"
			'''Box Drawings: **U+255f**( ``╟`` ) - vertical double and right single'''
			tRb: _L["╞"] = "╞"
			'''Box Drawings: **U+255e**( ``╞`` ) - vertical single and right double'''
			TRB: _L["╠"] = "╠"
			'''Box Drawings: **U+2560**( ``╠`` ) - double vertical and right'''


	class tl:
		'''
		Top-left corners
		'''

		br: _L["┌"] = "┌"
		'''Box Drawings: **U+250c**( ``┌`` ) - light down and right'''
		Br: _L["┎"] = "┎"
		'''Box Drawings: **U+250e**( ``┎`` ) - down heavy and right light'''
		bR: _L["┍"] = "┍"
		'''Box Drawings: **U+250d**( ``┍`` ) - down light and right heavy'''
		BR: _L["┏"] = "┏"
		'''Box Drawings: **U+250f**( ``┏`` ) - heavy down and right'''
		
		A: _L["╭"] = "╭"
		'''Box Drawings: **U+256d**( ``╭`` ) - light arc down and right'''

		class D:
			'''
			Top-left corners with double lines
			'''
			
			Br: _L["╓"] = "╓"
			'''Box Drawings: **U+2553**( ``╓`` ) - down double and rightsingle'''
			bR: _L["╒"] = "╒"
			'''Box Drawings: **U+2552**( ``╒`` ) - down single and right double'''
			BR: _L["╔"] = "╔"
			'''Box Drawings: **U+2554**( ``╔`` ) - double down and right'''

	class tb:
		'''
		Top-to-bottom borders
		'''

		tb: _L["│"] = "│"
		'''Box Drawings: **U+2502**( ``│`` ) - light vertical'''
		Tb: _L["╿"] = "╿"
		'''Box Drawings: **U+257f**( ``╿`` ) - heavy up and light down'''
		tB: _L["╽"] = "╽"
		'''Box Drawings: **U+257d**( ``╽`` ) - light up and heavy down'''
		TB: _L["┃"] = "┃"
		'''Box Drawings: **U+2503**( ``┃`` ) - heavy vertical'''

		t_: _L["╵"] = "╵"
		'''Box Drawings: **U+2575**( ``╵`` ) - light up'''
		T_: _L["╹"] = "╹"
		'''Box Drawings: **U+2579**( ``╹`` ) - heavy up'''
		b_: _L["╷"] = "╷"
		'''Box Drawings: **U+2577**( ``╷`` ) - light down'''
		B_: _L["╻"] = "╻"
		'''Box Drawings: **U+257b**( ``╻`` ) - heavy down'''

		d2: _L["╎"] = "╎"
		'''Box Drawings: **U+254e**( ``╎`` ) - light double dash vertical'''
		d3: _L["┆"] = "┆"
		'''Box Drawings: **U+2506**( ``┆`` ) - light triple dash vertical'''
		d4: _L["┊"] = "┊"
		'''Box Drawings: **U+250a**( ``┊`` ) - light quadruple dash vertical'''
		D2: _L["╏"] = "╏"
		'''Box Drawings: **U+254f**( ``╏`` ) - heavy double dash vertical'''
		D3: _L["┇"] = "┇"
		'''Box Drawings: **U+2507**( ``┇`` ) - heavy triple dash vertical'''
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

		lr: _L["─"] = "─"
		'''Box Drawings: **U+2500**( ``─`` ) - light horizontal'''
		Lr: _L["╾"] = "╾"
		'''Box Drawings: **U+257e**( ``╾`` ) - heavy left and light right'''
		lR: _L["╼"] = "╼"
		'''Box Drawings: **U+257c**( ``╼`` ) - light left and heavy right'''
		LR: _L["━"] = "━"
		'''Box Drawings: **U+2501**( ``━`` ) - heavy horizontal'''

		l_: _L["╴"] = "╴"
		'''Box Drawings: **U+2574**( ``╴`` ) - light left'''
		L_: _L["╸"] = "╸"
		'''Box Drawings: **U+2578**( ``╸`` ) - heavy left'''
		r_: _L["╶"] = "╶"
		'''Box Drawings: **U+2576**( ``╶`` ) - light right'''
		R_: _L["╺"] = "╺"
		'''Box Drawings: **U+257a**( ``╺`` ) - heavy right'''

		d2: _L["╌"] = "╌"
		'''Box Drawings: **U+254c**( ``╌`` ) - light double dash horizontal'''
		d3: _L["┄"] = "┄"
		'''Box Drawings: **U+2504**( ``┄`` ) - light triple dashhorizontal'''
		d4: _L["┈"] = "┈"
		'''Box Drawings: **U+2508**( ``┈`` ) - light quadruple dash horizontal'''
		D2: _L["┅"] = "┅"
		'''Box Drawings: **U+2505**( ``┅`` ) - heavy triple dash horizontal'''
		D3: _L["╍"] = "╍"
		'''Box Drawings: **U+254d**( ``╍`` ) - heavy double dash horizontal'''
		D4: _L["┉"] = "┉"
		'''Box Drawings: **U+2509**( ``┉`` ) - heavy quadruple dash horizontal'''

		class D:
			'''
			Left-to-right borders with double lines
			'''

			LR: _L["═"] = "═"
			'''Box Drawings: **U+2550**( ``═`` ) - double horizontal'''

	class cr:
		'''
		"Cross" borders (all 4 directions)
		'''

		tlbr: _L["┼"] = "┼"
		'''Box Drawings: **U+253c**( ``┼`` ) - light vertical and horizontal'''
		Tlbr: _L["╀"] = "╀"
		'''Box Drawings: **U+2540**( ``╀`` ) - up heavy and down horizontal light'''
		tlBr: _L["╁"] = "╁"
		'''Box Drawings: **U+2541**( ``╁`` ) - down heavy and up horizontal light'''
		tLbr: _L["┽"] = "┽"
		'''Box Drawings: **U+253d**( ``┽`` ) - left heavy and right vertical light'''
		tlbR: _L["┾"] = "┾"
		'''Box Drawings: **U+253e**( ``┾`` ) - right heavy and left vertical light'''

		TlBr: _L["╂"] = "╂"
		'''Box Drawings: **U+2542**( ``╂`` ) - vertical heavy and horizontal light'''
		tLbR: _L["┿"] = "┿"
		'''Box Drawings: **U+253f**( ``┿`` ) - vertical light and horizontal heavy'''
		TLbr: _L["╃"] = "╃"
		'''Box Drawings: **U+2543**( ``╃`` ) - left up heavy and right down light'''
		tLBr: _L["╅"] = "╅"
		'''Box Drawings: **U+2545**( ``╅`` ) - left down heavy and right up light'''
		TlbR: _L["╄"] = "╄"
		'''Box Drawings: **U+2544**( ``╄`` ) - right up heavy and left down light'''
		tlBR: _L["╆"] = "╆"
		'''Box Drawings: **U+2546**( ``╆`` ) - right down heavy and left up light'''
		
		TLBr: _L["╉"] = "╉"
		'''Box Drawings: **U+2549**( ``╉`` ) - right light and left vertical heavy'''
		TlBR: _L["╊"] = "╊"
		'''Box Drawings: **U+254a**( ``╊`` ) - left light and right vertical heavy'''
		TLbR: _L["╇"] = "╇"
		'''Box Drawings: **U+2547**( ``╇`` ) - down light and up horizontal heavy'''
		tLBR: _L["╈"] = "╈"
		'''Box Drawings: **U+2548**( ``╈`` ) - up light and down horizontal heavy'''
		TLBR: _L["╋"] = "╋"
		'''Box Drawings: **U+254b**( ``╋`` ) - heavy vertical and horizontal'''

		class D:
			'''
			"Cross" borders (all 4 directions)
			'''

			TlBr: _L["╫"] = "╫"
			'''Box Drawings: **U+256b**( ``╫`` ) - vertical double and horizontal single'''
			tLbR: _L["╪"] = "╪"
			'''Box Drawings: **U+256a**( ``╪`` ) - vertical single and horizontal double'''
			TLBR: _L["╬"] = "╬"
			'''Box Drawings: **U+256c**( ``╬`` ) - double vertical and horizontal'''

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
