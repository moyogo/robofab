from fontTools.pens.basePen import BasePen

class QuartzPen(BasePen):

	"""Pen to draw onto a Quartz drawing context (Carbon.CG).

		- OSX specific.

	"""

	def __init__(self, glyphSet, quartzContext):
		BasePen.__init__(self, glyphSet)
		self._context = quartzContext

	def _moveTo(self, pt):
		(x, y) = pt
		self._context.CGContextMoveToPoint(x, y)

	def _lineTo(self, pt):
		(x, y) = pt
		self._context.CGContextAddLineToPoint(x, y)

	def _curveToOne(self, pt1, pt2, pt3):
		(x1, y1) = pt1
		(x2, y2) = pt2
		(x3, y3) = pt3
		self._context.CGContextAddCurveToPoint(x1, y1, x2, y2, x3, y3)

	def _closePath(self):
		self._context.closePath()
