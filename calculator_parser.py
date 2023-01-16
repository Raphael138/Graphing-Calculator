import ply.yacc as yacc

from calculator_lexer import tokens


def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIV expression'''
    p[0] = ('binary-expression', p[2], p[1], p[3])


def p_cos_function(p):
    '''expression : COS LPAREN expression RPAREN'''
    p[0] = ('cos-function', p[1], p[3])


def p_sin_function(p):
    '''expression : SIN LPAREN expression RPAREN'''
    p[0] = ('sin-function', p[1], p[3])


def p_tan_function(p):
    '''expression : TAN LPAREN expression RPAREN'''
    p[0] = ('tan-function', p[1], p[3])


def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = ('group-expression', p[2])


def p_expression_number(p):
    'expression : NUMBER'
    p[0] = ('number-expression', p[1])


def p_expression_x(p):
    'expression : X'
    p[0] = ('var-x', p[1])


def p_expression_t(p):
    'expression : T'
    p[0] = ('var-t', p[1])


def p_error(p):
    raise Exception("Compile Time Error")

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIV'),
)

parser = yacc.yacc()
