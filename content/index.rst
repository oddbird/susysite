public: yes
meta_title: Susy
before:
  - include: 'modules/_release.html'
  - include: 'modules/_intro.html'
  - include: 'modules/_screenshots.html'
    title: In The Wild
    id: in-the-wild
    more: True
  - include: 'modules/_quotes.html'
  - include: 'modules/_news.html'


Power tools for the web
=======================


Rapid Prototypes, Built to Scale
--------------------------------

Rapid prototypes
are only the start to a long process
of development, changes, handoffs, and maintenance.
Susy is built to evolve with your project for the long haul.

`Get started`_ quickly
with the flexible ``span`` mixin:

.. code-block:: scss

  nav { @include span(25%); }
  main { @include span(75%); }

Then stick around for fully customizable grids:

.. code-block:: scss

  $susy: (
    columns: 12,
    gutter-position: inside,
    math: fluid,
    output: float,
    flow: rtl,
  );

And take complete control of the math
when you need it:

.. code-block:: scss

  nav {
    float: left;
    width: span(3);
    margin-right: gutter();
  }

  main {
    @include span(isolate 9 at 4 no-gutters);
  }

.. _Get started: http://susydocs.oddbird.net/en/latest/install/


Better Together
---------------

*Responsive Design* —
Susy integrates smoothly with `Breakpoint`_
for powerful media-query controls.
See the `documentation`_ for details.

*Vertical Rhythms* —
If you're using the `Compass`_,
we add support for ``$rem-with-px-fallback``,
and show your baseline grids for debugging.

*Package Managers* —
We love `Compass`_ and highly recommend it,
but you can use Susy 2 anywhere `Sass`_ is compiled.
Try it with `Bundler`_, `Bower`_, `Yeoman`_, `Bourbon`_,
or copied directly into your project.
Then check out `Sache.in`_ for more great Sass extensions.

*Community Effort* —
Susy was originaly based on Natalie Downe's `CSS Systems`_,
but has grown much more powerful and flexible than any one system.
For Susy 2 we joined forces with `Salsa`_,
and borrowed back from `Singularity`_, `Zen Grids`_, and elsewhere.
We'd love to `hear your ideas`_ as well.

.. _Breakpoint: http://breakpoint-sass.com
.. _documentation: http://susydocs.oddbird.net/
.. _Compass: http://compass-style.org/
.. _Sass: http://sass-lang.com/
.. _Bundler: http://bundler.io/
.. _Bower: http://bower.io/
.. _Yeoman: http://yeoman.io/
.. _Bourbon: http://bourbon.io/
.. _`Sache.in`: http://sache.in/
.. _CSS Systems: http://www.slideshare.net/nataliedowne/css-systems-presentation
.. _Salsa: http://tsi.github.io/Salsa/
.. _Singularity: http://singularity.gs/
.. _Zen Grids: http://next.zengrids.com/
.. _hear your ideas: http://github.com/oddbird/susy/issues


Read the Book!
--------------

`Zell Liew`_ wrote a great book to get you started with Susy.
You can even `Get the first five chapters for free`_!
Here are some of the things that you'll learn:

.. or use the discout code ``oddbirds`` for 20% off the entire package!


|book|

- How to use the **Span Mixin**
- How to output the **Background Grid**
- How to configure the **Global Settings** to your needs
- How to do **mobile-first responsive coding** with Susy and Breakpoint
- How different **gutter-positions** affect your layout
- How to build **asymmetric layouts** without breaking a sweat
- How to use the **isolation to prevent subpixel rounding** errors


.. _Zell Liew: http://zell-weekeat.com/
.. _Get the first five chapters for free: http://zell-weekeat.com/learnsusy/#signup
.. |book| raw:: html

  <figure data-media="left">
    <a href="http://zell-weekeat.com/learnsusy/#signup">
      <img src="http://zell-weekeat.com/learnsusy/images/book-dark-cover.png" />
    </a>
  </figure>
