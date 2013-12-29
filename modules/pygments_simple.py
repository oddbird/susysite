# -*- coding: utf-8 -*-
"""
Simple support for pygments.

Based on pygments module by Armin Ronacher, but takes no responsibility for
styles or CSS.

"""
from __future__ import absolute_import

from docutils import nodes
from docutils.parsers.rst import Directive, directives

from pygments import highlight
from pygments.lexers import get_lexer_by_name, TextLexer
from pygments.formatters import HtmlFormatter


html_formatter = HtmlFormatter()


class CodeBlock(Directive):
    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False

    def run(self):
        try:
            lexer = get_lexer_by_name(self.arguments[0])
        except ValueError:
            lexer = TextLexer()
        code = u'\n'.join(self.content)
        formatted = highlight(code, lexer, html_formatter)
        return [nodes.raw('', formatted, format='html')]


def setup(builder):
    directives.register_directive('code-block', CodeBlock)
    directives.register_directive('sourcecode', CodeBlock)
