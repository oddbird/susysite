public: yes
meta_title: Susy


Power tools for the web
=======================


No Opinions
-----------

In a world of agile development
and super-tablet-multi-magic-laptop-phones,
the best layouts can't be contained
in a single framework or technique.
CSS Libraries are a bloated mess of opinions
about how to do your job.
Stop letting the table-saw tell you where to put the kitchen.

*You draw the blueprints,
we'll do the heavy lifting.*


Rapid Prototypes, Rapid Production
----------------------------------

We know that rapid prototypes
are only the start to a long process
of development, changes, handoffs, and maintanance.
Susy is built for the long haul.

Get started quickly
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


In The Wild
-----------

.. wrap:: figure
  :class: gallery screenshots

  .. image:: /static/screenshots/sasslang.jpg
    :alt: Sass
    :target: http://sass-lang.com

  .. image:: /static/screenshots/squaremarket.jpg
    :alt: Square Market
    :target: http://squareup.com/market

  .. image:: /static/screenshots/slickbag.jpg
    :alt: Slickbag
    :target: http://slickbag.se/

  .. image:: /static/screenshots/viggle.jpg
    :alt: Viggle
    :target: http://www.viggle.com/

  .. image:: /static/screenshots/avoidpaydayloans.jpg
    :alt: Avoid Payday Loans
    :target: http://avoidpaydayloans.com/

  .. image:: /static/screenshots/turnitresponsive.jpg
    :alt: Turn It Responsive
    :target: http://turnitresponsive.com/

  .. wrap:: figcaption
    :class: gallery-caption

    See more `sites using Susy`_,
    or `add your own`_ »

.. _sites using Susy: /sites-using-susy/#everyone
.. _add your own: https://github.com/ericam/susysite/tree/master/content/sites-using-susy.rst


Better Together
---------------

*Responsive Design* —
Susy integrates smoothly with `Breakpoint`_
with powerul media-query controls
for responsive layouts.
See the `documentation`_ for details.

*Vertical Rhythms* —
If you're using the `Compass`_
vertical rhythms module,
we give you controls to show/hide your basline
along with any Susy grids you've defined.

*Package Managers* —
We love `Compass`_ and highly recommend it,
but you can use Susy anywhere `Sass`_ is compiled.
Susy plays well with `Bundler`_, `Bower`_/`Yeoman`_, and `Bourbon`_,
or copied into your sass directory.

.. _Breakpoint: http://breakpoint-sass.com
.. _Compass: http://compass-style.org/
.. _Sass: http://sass-lang.com/
.. _Bundler: http://bundler.io/
.. _Bower: http://bower.io/
.. _Yeoman: http://yeoman.io/
.. _Bourbon: http://bourbon.io/
.. _documentation: http://susydocs.oddbird.net/


Community Effort
----------------

Susy was originaly based on Natalie Downe's `CSS Systems`_,
and then pushed and proded by the community
to become something larger.
Along the way,
projects have split off
with their own interesting ideas.
We hope to keep that conversation going.

For Susy 2.0,
we merged with the `Salsa`_ project,
and borrowed additional ideas from
`Singularity`_, `Zen Grids`_, and elsewhere,
to create a more flexible layout language,
with all the tools in one belt.
We'd love to `hear your ideas`_ as well.
Questions, suggestions, pull requests,
and plugins are always welcome.

.. _CSS Systems:
.. _Salsa: http://tsi.github.io/Salsa/
.. _Singularity: http://singularity.gs/
.. _Zen Grids: http://next.zengrids.com/
.. _hear your ideas: http://github.com/ericam/susy/issues
