#!/usr/bin/env python
"""Takes a dataset and writes it to three paths for training, development, and testing."""


import argparse

from typing import Iterator, List

import random



def read_tags(path: str) -> Iterator[List[List[str]]]:
    with open(path, "r") as source:
        lines = []
        for line in source:
            line = line.rstrip()
            if line:  # Line is contentful.
                lines.append(line.split())
            else:  # Line is blank.
                yield lines.copy()
                lines.clear()
    # Just in case someone forgets to put a blank line at the end...
    if lines:
        yield lines



def main(args: argparse.Namespace) -> None:
    # TODO: do the work here.
    print(args)
    corpus = list(read_tags(args.input))

    random.seed(args.seed)

    makeitfun = random.shuffle(corpus)
    size = len(corpus)
    
    eightypercent = int(size * .8)
    ninetypercent = int(size * .9)
    trainslice = corpus[:eightypercent]
    devslice = corpus[eightypercent:ninetypercent]
    testslice = corpus[ninetypercent:]
    
    
    with open(args.train, 'w') as sink:
        for item in trainslice:
            for detail in item:
                single = " ".join([str(elem) for elem in detail])
                print(single, file=sink)
    with open(args.dev, 'w') as sink:
        for item in devslice:
            for detail in item:
                single = " ".join([str(elem) for elem in detail])
                print(single, file=sink)
    with open(args.test, 'w') as sink:
        for item in testslice:
            for detail in item:
                single = " ".join([str(elem) for elem in detail])
                print(single, file=sink)

    ...


if __name__ == "__main__":
    # TODO: declare arguments.
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, required=True, help="path to write the training data to")
    parser.add_argument("input", help="path to write the file to")
    parser.add_argument("train", help="path to write the training data to")
    parser.add_argument("dev", help="path to write the dev data to")
    parser.add_argument("test", help="path to write the test data to")
    # TODO: parse arguments and pass them to `main`.
    main(parser.parse_args())
    ...
