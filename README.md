rfooConsoleUtil
===============

Note that this project now embeds `rfoo` as that project has not been updated
in 6 years and Google Code is shutting down.

Example usage:

1. In application start-up:

    import rfooConsoleUtil
    rfooConsoleUtil.spawnServer()

2. To debug:
    
    python -c "import rfooConsoleUtil; rfooConsoleUtil.connect(port[, host])"

    >>> showStacks()  # Prints out threads; can use either name or thread ID
                      # number for subsequent getFrame()
    >>> q = getFrame('Main')
    >>> q
    Frame 1
    ...Stack trace...
    >>> q.locals()
    {'prompt': '...',
        'self': <IPython.frontend...>}
    >>> q['self']
    <IPython.frontend...>
    >>> q.up()
    Frame 2
    ...Stack trace...
    >>> q.down()
    Frame 1
    ...Stack trace...

