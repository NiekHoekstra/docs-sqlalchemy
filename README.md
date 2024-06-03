# docs-sqlalchemy

This is an alternative piece of documentation for SQLAlchemy.

## Why?

The examples provided by SQLAlchemy do work, and are absolutely serviceable.
I like SQLAlchemy, the team has done great work to support a wide spectrum of features,
and supporting them *well*.

Therein also lies the problem.

SQLAlchemy has more features than it can (comfortably) explore in its own documentation.
If anyone from the SQLAlchemy team reads this, please see this as a sign of my enthusiasm, and not as criticism.

This repository will host a lot of Jupyter Notebooks people can play with,
demonstrating various table structures,
and applying knowledge to a few intricate examples. 
This approach might be more serviceable for those who learn better from a hands-on approach.

## Running it

```bash
python -m notebook
```

## Requirements

The ``requirements.in`` file states the core (interesting) dependencies.

The list of packages in requirements.txt are pinned to the version they are expected to work with.
This is just a documentation repository, not really looking for contributions.

Please feel encouraged to fork this repository for your own purposes.
Developers can upgrade (or downgrade) these packages to their own requirements for testing purposes.

Requirements may change in the future, but that will be based on my personal needs.

## Structure



### markdown

This directory contains basic alternative docs.
Markdown is pretty easy to search through, and websites can get bogged down with all the nuts and bolts.

### notebooks

This directory contains (Jupyter) notebooks which can run for learning, experimentation, and compatibility testing.

