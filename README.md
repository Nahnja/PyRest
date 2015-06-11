# PyRest
Use REST-APIs as if they were objects.

Basically, this supplies a class whose instances have some custom behaviour on `__getattr__` and `__getitem__`. That way typing something like

    PyRest("www.twitter.com").statuses.show[123].get()

results in a get request to `www.twitter.com/statuses/show/123`.

The class should be easily extensible to allow the addition of various kinds of authentication methods on creation.

However, since `__getattr__` and `__getitem__` are overwritten, careless subclassing may result in tricky endless loops. So maybe this whole thing is a pretty bad idea?
