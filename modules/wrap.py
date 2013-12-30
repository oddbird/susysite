# -*- coding: utf-8 -*-
"""
Add a generic ``wrap`` reST directive to wrap content in an HTML element.

To use, include ``wrap`` in the list of modules in your ``config.yml``.

The directive has two optional arguments: ``class`` and ``id``, which map
directly to the HTML attributes of the same name.

Example::

    .. wrap:: figure
       :class: simple
       :id: figure-1

       Here is the figure:

       .. image:: images/figure1.gif

"""
from __future__ import absolute_import
from docutils import nodes
from docutils.parsers.rst import Directive, directives


def identifier(argument):
    if argument is not None:
        return nodes.make_id(argument)


def identifier_list(argument):
    names = argument.split()
    class_names = []
    for name in names:
        class_name = nodes.make_id(name)
        if not class_name:
            raise ValueError('cannot make "%s" into a class name' % name)
        class_names.append(class_name)
    return class_names


class Wrap(Directive):
    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        'class': identifier_list,
        'id': identifier,
    }

    def run(self):
        self.assert_has_content()
        text = '\n'.join(self.content)
        node = nodes.container(text)
        node.element_name = self.arguments[0]
        element_id = self.options.get('id', None)
        if element_id is not None:
            node['ids'].append(element_id)
        cls = self.options.get('class')
        if cls:
            node['classes'].extend(cls)
        self.add_name(node)
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


def setup(builder):
    directives.register_directive('wrap', Wrap)
