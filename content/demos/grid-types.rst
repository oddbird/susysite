public: yes
template: demo.html
styles: grid-types.css


Different Grid Types
====================


Customizing Susy
----------------

You can build grids of all kinds with Susy.
Define your grid using any unit of measurement
(ems, pixels, percentages, inches, etc.)
and then determine how and when
you want that grid to respond to the viewport.

By default,
Susy converts all internal grid-widths into percentages
with an outer container set in the units you choose,
but you can override that to generate grids in any unit you like.

Here are a few examples
of grids with different container styles.


The Magic Grid
--------------

.. raw:: html

  <aside class="demo magic-container">
    <h3>.magic-container</h3>
    <p>
      10 columns,
      4em width,
      1em gutters,
      1em padding.
      Magic.
    </p>
  </aside>

The default grid in Susy is what I call "the magic grid".
Fluid on the inside,
with an elastic container max-width.
The em-width makes it responsive to font sizes,
while the max-width setting makes it responsive to window sizes.

.. code-block:: scss

    // Setting up the Magic Grid
    $total-columns: 10; // 10 columns
    $column-width: 4em; // columns are 4em wide
    $gutter-width: 1em; // with 1em gutters
    $grid-padding: 1em; // and 1em padding on the grid container

    .magic-container { @include container; }

What we've defined is a simple elastic grid,
but by default the outer container width
will be set as a max-width,
making this a magic grid.

You can also have px-based magic grids,
and so on,
though I find them somewhat less magical.
What makes it a magic grid
is the fact that it collapses with the browser at smaller sizes,
but remains set-width at larger sizes.

There is a more complete
`mobile-first magic grid demo </demos/magic/>`_
if you are interested.


The Fluid Grid
--------------

.. raw:: html

  <aside class="demo fluid-container">
    <h3>.fluid-container</h3>
    <p>
      12 columns,
      60px initial width,
      20px initial gutters,
      10px initial padding.
      Fluid.
    </p>
  </aside>

There are many ways to build a fluid grid with Susy.
You could simply replace all the em-widths above
with percentage widths.
But that's actually the hard way,
unless you know exactly what percentages you want to use.
Let me show you some easier options.

Say you want to build a fluid grid
based on the `960gs <http://960.gs/>`_ dimensions:

.. code-block:: scss

    // A Fluid Grid based on 960gs
    $total-columns: 12;
    $column-width: 60px;
    $gutter-width: 20px;
    $grid-padding: 10px;

That's a good start.
We now have a 960px magic grid.
Turning that into a fluid grid is simple:

.. code-block:: scss

    // Make it fluid!
    $container-style: fluid;

    .fluid-container { @include container; }

That's it.
You have a fluid grid
based on the dimensions of the 960gs.
By default the fluid container is set to 100% width,
but you can override that as well:

.. code-block:: scss

    // Make it smaller
    $container-width: 80%;


The Static Grid
---------------

.. raw:: html

  <aside class="demo static-container">
    <h3>.static-container</h3>
    <p>
      10 columns,
      4em width,
      1em gutters,
      1em padding.
      Static.
    </p>
  </aside>

Perhaps you don't want your grid to respond
to the size of the viewport at all.
By telling Susy you want a "static" grid,
Susy will apply your container-width
directly to the "width" property.

This is your more standard grid type.
Most "elastic" and "fixed" grids fit this category.
Unlike the magic grid, it doesn't collapse.

Let's take our first grid and make it static:

.. code-block:: scss

    // Setting up the Static Grid
    $total-columns: 10;
    $column-width: 4em;
    $gutter-width: 1em;
    $grid-padding: 1em;

    $container-style: static;

    .static-container { @include container; }


Mixing and matching
-------------------

Using those same 4 basic settings,
and the two advanced override settings,
you can create nearly any grid without doing any math.

Want the 960 grid system
updated to 1140px?

.. code-block:: scss

    // The 960gs in 1140px
    $total-columns: 12;
    $column-width: 60px;
    $gutter-width: 20px;
    $grid-padding: 10px;

    $container-style: static;
    $container-width: 1140px;

    .larger-960-container { @include container; }

Why not make it elastic and magic?

.. code-block:: scss

    // The 960gs in ems
    $total-columns: 12;
    $column-width: 60px;
    $gutter-width: 20px;
    $grid-padding: 10px;

    $container-style: magic;
    $container-width: 60em;

    .elastic-960-container { @include container; }

Or we can make a magic-elastic grid,
defined in percentages:

.. code-block:: scss

    // Elastic grid as percentages
    $total-columns: 12;
    $column-width: 6%;
    $gutter-width: 2%;
    $grid-padding: 1%;

    $container-style: magic;
    $container-width: 50em;

    .elastic-percentage-container { @include container; }

Play around.
Start to add breakpoints,
with different grids at different sizes,
or just pick the grid best suited for your site:
magic-elastic,
magic-fixed,
static-elastic,
static-fixed,
fluid,
defined as one but displayed as another...
The possibilities are endless.
Have fun!
