# SQLAlchemy

It can be a bit confusing to understand *which* problems SQLAlchemy is trying to solve.

- Core
- 
- (ORM) Models
- Tables
- Dialects/Language (MS SQL, MySQL, PostgresQL)

One thing which SQLAlchemy doesn't provide is networking.

Each Database system can have its own login strategy,
or support alternative login methods like "Windows Authentication" or mediums like Unix Sockets.

By allowing the drivers to be 'pluggable' according to an API (like PEP 248/249),
this layer can be swapped out quite easily.


- [PEP-249 - Python Database API Specification v2.0](https://peps.python.org/pep-0249/)
- [PEP-248 - Python Database API Specification v1.0](https://peps.python.org/pep-0248/)