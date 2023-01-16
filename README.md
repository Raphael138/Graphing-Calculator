# Graphing-Calculator

## Libraries

It uses PLY in order to interpret the input text and pygame to draw the graphics.

## File Architecture
1. `calculator_lexer.py` is the lexer file
2. `calculator_parser.py` is the parser file which creates the AST
3. `calculator_output.py` returns the y coordinates for a given AST and a given list of x and t inputs
5. `calculator.py` combines all the input comprehension files and some pygame code to create a graph and calculator GUI.
