public: yes
meta_title: Susy
before:
  - include: 'modules/_release.html'
  - include: 'modules/_intro.html'
  - include: 'modules/_screenshots.html'
    title: In The Wild
    id: in-the-wild
    more: true


Power tools for the web
=======================


Rapid Prototypes, Built to Scale
--------------------------------

|note|

.. |note| raw:: html

  <em>
  These instructions are for the upcoming Susy 2.0 release,
  which is feature-complete,
  but requires the pre-release version of Sass.
  The full
  <a href="http://susydocs.oddbird.net/en/latest/susyone/">Susy One documentation</a>
  is still available,
  along with
  <a href="http://susydocs.oddbird.net/en/latest/upgrade/">upgrade instructions</a>,
  and <a href="/demos/">tutorials</a>.
  In fact,
  the entire Susy One syntax is available as a language option
  in the Susy Two gem.
  </em>

We know that rapid prototypes
are only the start to a long process
of development, changes, handoffs, and maintanance.
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
