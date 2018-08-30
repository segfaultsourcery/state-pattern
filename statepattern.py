class State(dict):
    def assign(self, **kw):
        """
        This creates a new copy of the state object.
        You shouldn't be editing a state object directly,
        instead you should operate on copies.

        state1 = State({
            'dog': 'water',
            'horses': 5
        })

        state2 = state1.assign(dog='not water', cinnamon_toast='man')
        print(state1, state2)

        :rtype: State
        """

        return State(self, **kw)

    def discard(self, *keys):
        """
        Discard items from the state by key.

        state1 = State({
            'dog': 'water',
            'horses': 5
        })

        state2 = state1.discard('dog')
        print(state1, state2)

        :param keys: str, ...
        :return: State
        """

        return State({k: v for k, v in self.items() if k not in keys})

    def __getattr__(self, item):
        """
        This allows you to access members using dot notation.
        If a member isn't found, None is returned instead, allowing you
        to use "or" to use a default value.

        items = state.items or []
        """

        try:
            return self[item]
        except KeyError:
            return None

    def then(self, fn):
        """
        The function fn must take a State object as its only argument, and return a State object.

        def download_items(state: State) -> State:
            "You would download a house, a car, and a bear."
            items = state.items or []
            return state.assign(
                downloads=map(requests.get, items)
            )

        def show_downloads(state: State) -> State:
            "Show our bountiful booty."
            downloads = state.downloads or []
            pprint(downloads)
            return state

        state = (
            State({'items': ['hourse', 'car', 'bear']})
                .then(download_items)
                .then(show_downloads)
        )

        :rtype: State
        """

        return fn(self)
