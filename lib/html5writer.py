"""
A docutils HTML5 writer based on the built-in html4css1 writer.

Work in progress.

"""
from docutils.writers import html4css1


class Writer(html4css1.Writer):
    def __init__(self):
        html4css1.Writer.__init__(self)
        self.translator_class = HTML5Translator


class HTML5Translator(html4css1.HTMLTranslator):
    def visit_section(self, node):
        self.section_level += 1
        self.body.append(
            self.starttag(node, 'section'))


    def depart_section(self, node):
        self.section_level -= 1
        self.body.append('</section>\n')


    def visit_topic(self, node):
        self.body.append(self.starttag(node, 'section'))
        self.topic_classes = node['classes']


    def depart_topic(self, node):
        self.body.append('</section>\n')
        self.topic_classes = []


    def visit_list_item(self, node):
        self.body.append(self.starttag(node, 'li', ''))


    def visit_literal_block(self, node):
        self.body.append(self.starttag(node, 'pre'))


    def visit_literal(self, node):
        self.body.append(self.starttag(node, 'code', suffix=''))


    def depart_literal(self, node):
        self.body.append('</code>')


    def visit_container(self, node):
        elem_name = getattr(node, 'element_name', 'div')
        self.body.append(self.starttag(node, elem_name))


    def depart_container(self, node):
        elem_name = getattr(node, 'element_name', 'div')
        self.body.append('</%s>\n' % elem_name)
