public: yes
template: demo.html


Mobile-First Magic Grids
========================


Fluid + Elastic == Magic
------------------------

My favorite of the Susy One options is
what I call the Magic Grid.
Fluid on the inside and elastic on the outside,
the magic grid responds to both font and window size
while keeping you in control of typographic line lengths.

This demo will lay out the steps
for building a mobile-first layout
based on Susy's default Magic Grid.


Basic Settings
--------------

Let's start by defining
our mobile-first grid:

.. code-block:: scss

    $total-columns  : 7;
    $column-width   : 4.25em;
    $gutter-width   : 1em;
    $grid-padding   : $gutter-width;

In this case I decided that ``7`` columns at ``4.25em``
was a good line-length for the main content.
While that's larger than most mobile devices,
the site will flex to fit them as well.

We've set ``$column-width: 4.25em``,
but Susy doesn't apply that directly.
That will be used to determine the outer container width
(using ``max-width`` unless `otherwise instructed`_),
and then to figure out percentages internally.

Think of these settings as a max-width
for your initial layout.

.. _otherwise instructed: http://susydocs.oddbird.net/en/latest/susyone/#container-override-settings


Mobile Layout
-------------

The first step in applying our Susy grid is to
define our `container`_:

.. code-block:: scss

    .page { @include container; }

I wrote the source order in a way
that makes sense to me
even when the sidebars move inline with the main content.

.. code-block:: yaml

    - .page
      - .banner
      - .pagenav
      - .main
        - .summary
        - .content
      - .contentinfo

We're going to keep the mobile layout simple and linear,
but I want the footer to have a red background
that encompasses the `grid-padding`_.
In order to do that,
I apply negative margins equal to ``$grid-padding``,
and add it back in as padding to the footer,
using the ``bleed()`` mixin:

.. code-block:: scss

    .contentinfo {
      @include bleed($grid-padding);
    }

Add in some style and typography,
and we're done with `the mobile layout`_.

.. _container: http://susydocs.oddbird.net/en/latest/susyone/#container
.. _grid-padding: http://susydocs.oddbird.net/en/latest/susyone/#grid-padding
.. _the mobile layout: http://sassmeister.com/gist/8381773


Breakpoints
-----------

I'm only adding one layout `breakpoint`_ to this page,
although you can add as many as you want.

As soon as there is enough room for 12 columns,
we'll jump to a 12-column grid,
and bring our two sidebars into play.

Let's set that breakpoint as a variable,
since we'll need it several times:

.. code-block:: scss

    $break: 12;

We could get more complex,
switching to 12 columns at an arbitrary min-width (``$break: 40em 12``),
or adding a fallback class for older versions of IE (``$break: 12 lt-ie9``),
but I don't think we need either one in this case.

Let's update the container
to respond to our new breakpoint:

.. code-block:: scss

    .page {
      @include container($total-columns, $break);
    }

We're using the shortcut here,
setting multiple containers in a single command.
The first argument uses the default layout (``$total-columns``)
which doesn't trigger any media-queries,
the second uses our 12-column breakpoint.
This serves the same function as the longhand
using `at-breakpoint`_:

.. code-block:: scss

    .page {
      @include container;
      @include at-breakpoint($break) {
        @include container;
      }
    }

However, the shorthand also performs some optimizations for us,
using ``set-container-width`` instead of ``container`` inside the breakpoint.
Since we know the other container settings are already in place,
all we need to override is the container's width.
you can also do that longhand too, if you like:

.. code-block:: scss

    .page {
      @include container;
      @include at-breakpoint($break) {
        @include set-container-width;
      }
    }

The longhand can be useful
if you have other operations to perform inside the breakpoint.
In our case, we can move on to laying out our 12-column grid.

.. _breakpoint: http://susydocs.oddbird.net/en/latest/susyone/#media-layouts
.. _at-breakpoint: http://susydocs.oddbird.net/en/latest/susyone/#at-breakpoint


Large-Screen Layout
-------------------

Let's start with the banner.
It should span the full width,
but have 2 of 12 columns `prefixed`_ as padding on the left.

Since the banner didn't have any layout styles
in our mobile layout,
we can place the entire selector block
inside a breakpoint:

.. code-block:: scss

    @include at-breakpoint($break) {
      .banner { @include prefix(2,$break); }
    }

Notice that I'm using ``$break`` as the ``context`` argument.
That way if I decide to change it,
I won't have to worry about updating all the contexts.

Next comes the pagenav,
which we want to set as a sidebar
`spanning`_ 2 of the available 12 columns.
We can add that to the same breakpoint block
we already created.

.. code-block:: scss

    @include at-breakpoint($break) {
      .banner { @include prefix(2,$break); }
      .pagenav { @include span-columns(2,$break); }
    }

The main content will fill the remaining space,
spanning 10 of 12 columns,
including the final right-most "`omega`_" column.
Adding that to what we have:

.. code-block:: scss

    @include at-breakpoint($break) {
      .banner { @include prefix(2,$break); }
      .pagenav { @include span-columns(2,$break); }
      .main { @include span-columns(10 omega, $break); }
    }

Inside the main content
we have a summary (which becomes a second sidebar),
and content that occupies the main area.
The content spans 7 of the main 10,
while the summary spans the remaining 3 (omega) of 10:

.. code-block:: scss

    @include at-breakpoint($break) {
      .banner { @include prefix(2,$break); }
      .pagenav { @include span-columns(2,$break); }
      .main {
        $main-columns: 10;
        @include span-columns($main-columns omega, $break);
        .content { @include span-columns(7,$main-columns) }
        .summary { @include span-columns(3 omega, $main-columns) }
      }
    }

(Again, notice I'm using ``$main-columns`` for defining columns and contexts.)

That works, even though the summary comes first in our source.
Applying ``omega`` to an element
automatically pushes it to the end.

All we have left is the footer.
With 12 columns available now,
we can replace the grid-padding trick
with a few columns of padding on either side.
Let's create a new breakpoint block for that
inside the footer block we already have.
We also need to clear the floated content above,
which is easy enough with plain CSS:

.. code-block:: scss

    .contentinfo {
      @include bleed($grid-padding);
      @include at-breakpoint($break) {
        clear: both;
        margin: 0;
        @include pad(2,3,$break);
      }
    }

And `we're done`_. The rest is a matter of design.

.. _prefixed: http://susydocs.oddbird.net/en/latest/susyone/#prefix
.. _spanning: http://susydocs.oddbird.net/en/latest/susyone/#span-columns
.. _omega: http://susydocs.oddbird.net/en/latest/susyone/#omega
.. _`we're done`: http://sassmeister.com/gist/8381814


Complete Layout Styles
----------------------

In the end,
we have an entirely responsive layout
defined in just a few simple and meaningful lines,
without doing any math at all:

.. code-block:: scss

    // Settings

    $total-columns  : 7;
    $column-width   : 4.25em;
    $gutter-width   : 1em;
    $grid-padding   : $gutter-width;

    $break          : 12;

    // Container

    .page {
      @include container($total-columns, $break);
    }

    // Layout

    @include at-breakpoint($break) {
      .banner { @include prefix(2,$break); }
      .pagenav { @include span-columns(2,$break); }
      .main {
        $main-columns: 10;
        @include span-columns($main-columns omega, $break);
        .content { @include span-columns(7,$main-columns) }
        .summary { @include span-columns(3 omega, $main-columns) }
      }
    }

    .contentinfo {
      clear: both;
      @include bleed($grid-padding);
      @include at-breakpoint($break) {
        margin: 0;
        @include pad(2,3,$break);
      }
    }

**Note**:
Due to a known Sass bug,
if you are using an IE fallback class,
you can not apply ``at-breakpoint`` at the document root.
This should be fixed soon.
In the meantime,
breakpoints with fallback classes must be nested
inside another selector.
We're not using the fallback,
so we're ok.
