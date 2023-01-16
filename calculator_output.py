import math

# Class works to takes in the Abstract Syntax Tree and outputs the y coordinates
class SyntaxAnalysis:
	def __init__(self, xs, AST):
		self.xs = xs
		self.AST = AST

	# For a single x-value what is the output 
	def solve(self, x_value, t_value, AST_node):
		match AST_node:
			case ('number-expression', n):
				return n
			case ('var-x', n):
				return n*x_value
			case ('var-t', n):
				return n*t_value
			case ('binary-expression', op, left, right):
				left = self.solve(x_value, t_value, left)
				right = self.solve(x_value, t_value, right)
				if op=='+':
					return left+right
				elif op=="-":
					return left-right
				elif op=="*":
					return left*right
				elif op=="/":
					if right==0:
						return -1000
					return left/right if left/right!=float("inf") else -1000
			case ('group-expression', expr):
				return self.solve(x_value, t_value, expr)
			case ('cos-function', amp, expr):
				return amp*math.cos(self.solve(x_value, t_value, expr))
			case ('sin-function', amp, expr):
				return amp*math.sin(self.solve(x_value, t_value, expr))
			case ('tan-function', amp, expr):
				return amp*math.tan(self.solve(x_value, t_value, expr))
			case _:
				raise Exception("Runtime Error")

	#Running solve for all xs
	def output(self, t):
		y = []
		for x in self.xs:
			y.append(self.solve(x, t, self.AST))
		return y