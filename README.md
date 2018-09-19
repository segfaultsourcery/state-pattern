# State pattern 

**The state pattern tries to deal with common state issues by making it immutable and utilizing copy-on-write.**

This pattern kind of emerged for me out of necessity while working with databases. I had inherited quite a bit of code that was analyzing, creating, editing, and removing data, all in a couple of quite large, borderline godlike, functions.

I can't get into too much detail, but more often than not, the same bit of data was fetched over and over, making it slow. Sometimes bits of the code was working on data that had already been edited by other bits of the code, and whenever there was an error, it tended to leave the data in a very iffy state.

I did not like this one bit.

Further reading: http://segfaultsourcery.com/post/state-pattern

## Installation

### Requirements
* Python 3.5 and up

`$ pip install statepattern`

## Usage

This example shows how to assign and reassign values in a `State` object.

```python
from statepattern import State as S

state1 = S(
    dog='water',
    horses=5,
)

state2 = state1.assign(dog='not water', cinnamon_toast='man')
print(state1, state2)
```


This example shows how to use a `State` object to chain function calls. A function must accept a `State` as its only argument and return a `State`.

```python
from statepattern import State as S


def increment(state: S) -> S:
    points = state.points or 0
    return state.assign(points=points + 1)


def double(state: S) -> S:
    points = state.points or 0
    return state.assign(points=points * 2)


before = S(points=0)

after = (
    before
        .then(increment)
        .then(double)
        .then(increment)
)

print(before, after)
```

This example shows how to discard a value by key.

```python
from statepattern import State as S

state1 = S(
    dog='water',
    horses=5,
)

state2 = state1.discard('dog')
print(state1, state2)
```


## Development
There are no dependencies at all, by design. I still recommend making a virtualenv to work in, however.
```
$ virtualenv venv
$ source venv/bin/activate
$ pip install -e .
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update (or write) tests as appropriate.

## License
[BSD 2-Clause License](https://tldrlegal.com/license/bsd-2-clause-license-(freebsd))