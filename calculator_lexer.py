import ply.lex as lex
import math
# List of token names

tokens = (
    'X',
    'T',
    'COS',
    'SIN',
    'TAN',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIV',
    'LPAREN',
    'RPAREN',
)
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIV = r'\/'
t_LPAREN = r'\('
t_RPAREN = r'\)'


def t_COS(t):
    r'(((\d+)(\.)(\d+))cos)|((\d+)cos)|(cos)'
    if t.value == 'cos':
        t.value = 1.
    else:
        t.value = float(t.value[:-3])
    return t


def t_SIN(t):
    r'(((\d+)(\.)(\d+))sin)|((\d+)sin)|(sin)'
    if t.value == 'sin':
        t.value = 1.
    else:
        t.value = float(t.value[:-3])
    return t


def t_TAN(t):
    r'(((\d+)(\.)(\d+))tan)|((\d+)tan)|(tan)'
    if t.value == 'tan':
        t.value = 1.
    else:
        t.value = float(t.value[:-3])
    return t


def t_X(t):
    r'(((\d+)(\.)(\d+))x)|((\d+)x)|(x)'
    if t.value == 'x':
        t.value = 1.
    else:
        t.value = float(t.value[:-1])
    return t


def t_T(t):
    r'(((\d+)(\.)(\d+))t)|((\d+)t)|(t)'
    if t.value == 't':
        t.value = 1.
    else:
        t.value = float(t.value[:-1])
    return t


def t_NUMBER(t):
    r'((\d+)(\.)(\d+))|\d+|\((p)(i)\)'
    if t.value == '(pi)':
        t.value = math.pi
    else:
        t.value = float(t.value)
    return t


def t_error(t):
    raise Exception("Invalid syntax")


lexer = lex.lex()
