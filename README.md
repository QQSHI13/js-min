# js-min

[![PyPI version](https://img.shields.io/pypi/v/min-js.svg)](https://pypi.org/project/min-js/)
[![Publish](https://github.com/QQSHI13/js-min/actions/workflows/publish.yml/badge.svg)](https://github.com/QQSHI13/js-min/actions/workflows/publish.yml)
[![CodeQL](https://github.com/QQSHI13/js-min/actions/workflows/codeql.yml/badge.svg)](https://github.com/QQSHI13/js-min/actions/workflows/codeql.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/QQSHI13/js-min/blob/master/LICENSE.txt)

A community fork of the [`jsmin`](https://github.com/tikitu/jsmin) JavaScript minifier.

- **GitHub:** https://github.com/QQSHI13/js-min
- **PyPI package:** `min-js`
- **Python module:** `js_min`

## Install

```bash
pip install min-js
```

## Usage

```python
from js_min import jsmin

with open('myfile.js') as js_file:
    minified = jsmin(js_file.read())
```

Command line:

```bash
python -m js_min myfile.js
```

> **Note:** `js-min` makes no attempt to be compatible with
> [ECMAScript 6 / ES.next / Harmony](http://wiki.ecmascript.org/doku.php?id=harmony:specification_drafts).

If you are minifying ES6 code, you can use the `quote_chars` parameter:

```python
from js_min import jsmin

with open('myfile.js') as js_file:
    minified = jsmin(js_file.read(), quote_chars="'\"`")
```

## Where to get it

- Install from PyPI: https://pypi.org/project/min-js/
- Latest release branch on GitHub: https://github.com/QQSHI13/js-min/tree/latest-release/js_min
- Development version on GitHub: https://github.com/QQSHI13/js-min/

## Python 2 support removed

Python 2 support was removed in version 3.0.0. If you need to support Python 2,
please use `jsmin` version 2.2.2 with `setuptools<58`.

## Contributing

[Issues](https://github.com/QQSHI13/js-min/issues) and
[Pull requests](https://github.com/QQSHI13/js-min/pulls) are welcome.

The upstream project used to be hosted
[on Bitbucket](https://bitbucket.org/dcs/jsmin/) and old issues can still be
found there.

If possible, please make separate pull requests for tests and for code: tests
will be added to the `latest-release` branch while code will go to `master`.

Unless you request otherwise, your GitHub identity will be added to the
contributor list below.

## Contributors

Historical contributors (chronological commit order):

- [Dave St.Germain](https://bitbucket.org/dcs) — original author
- [Hans weltar](https://bitbucket.org/hansweltar)
- [Tikitu de Jager](mailto:tikitu+jsmin@logophile.org) — upstream maintainer
- https://bitbucket.org/rennat
- [Nick Alexander](https://bitbucket.org/ncalexan)
- [Gennady Kovshenin](https://github.com/soulseekah)
- [Matt Molyneaux](https://github.com/moggers87)
- [Albert Wang](https://github.com/albertyw)
- [Ben Bradshaw](https://github.com/serenecloud)

## Users

If your project uses `js-min`, feel free to open a PR adding it to this list.

- *Your project here*
