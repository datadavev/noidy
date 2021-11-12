"""
Commandline app for interacting with fark
"""
import sys
import os
import click
import logging
import json
import fark.n2tminter

@click.group()
@click.pass_context
def main(ctx):
    logging.basicConfig(level=logging.INFO)
    ctx.ensure_object(dict)
    return 0


@main.command()
@click.pass_context
@click.argument("naan")
@click.argument("prefix")
@click.option("-n", "--count", help="Number of identifiers to mint", default=1)
def mint(ctx, naan, prefix, count):
    """
    Mint next sequence of identifiers for given NAAN and prefix.

    \b
    Args:
        naan:  Name Assigning Authority Number
        prefix: NAAN/prefix{MINTED}
        count: Number of identifiers to mint (1)

    \b
    Returns:
        Identifiers, one per line of stdout

    """
    shoulder = f"{naan}/{prefix}"
    minter = fark.n2tminter.N2TMinter(shoulder)
    state_file = f"fark_{naan}~{prefix}.json"
    if os.path.exists(state_file):
        with open(state_file, "r") as inf:
            state = json.load(inf)
        minter.fromDict(state)

    res = minter.mint(count=count)
    for ark in res:
        print(f"ark:{shoulder}{ark}")

    with open(state_file, "w") as outf:
        json.dump(minter.asDict(), outf)
    print(f"state persisted to {state_file}")


if __name__ == "__main__":
    sys.exit(main())
