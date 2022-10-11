# README for noidy

Experimental.

Implements a NOID generator based on EZID and N2T NOID code.

Persists the generator state to JSON.

## Installation

```
git clone https://github.com/datadavev/noidy.git
poetry install 
```

## Operation

```
$ noid --help
Usage: noid [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  mint  Mint next sequence of identifiers for given NAAN and prefix.
```

Mint five NOIDs:

```
$ noid mint 99999 fk4 -n 5
ark:99999/fk44w2s
ark:99999/fk4159p
ark:99999/fk4wc7r
ark:99999/fk4rp4j
ark:99999/fk4mw2m
```

State is persisted to the JSON file "noid_NAAN-SHOULDER.json"

