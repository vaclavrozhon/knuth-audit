#!/usr/bin/env python3
"""Distinguish allocated trie nodes from terminal word ranks on 4B p.36."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent


def counts(words):
    n = len(words[0])
    assert all(len(w) == n for w in words) and len(set(words)) == len(words)
    by_length = [len({w[:k] for w in words}) for k in range(n+1)]
    # A second count walks distinct edges of an independently constructed tree.
    tree = {}
    for word in words:
        node = tree
        for letter in word:
            node = node.setdefault(letter, {})
    def walk(node):
        return 1 + sum(walk(child) for child in node.values())
    all_nodes = walk(tree)
    assert all_nodes == sum(by_length)
    proper = sum(by_length[:-1])
    assert all_nodes-proper == len(words)
    return dict(word_length=n, words=len(words), prefixes_by_length=by_length,
                nodes_for_printed_closed_range=all_nodes,
                nodes_for_corrected_half_open_range=proper,
                extra_terminal_nodes=len(words))


def main():
    path = ROOT / 'sources/wordlists/words6-from-OSPD4'
    small = counts(['a'])
    large = counts(path.read_text().splitlines())
    assert small['nodes_for_printed_closed_range'] == 2
    assert small['nodes_for_corrected_half_open_range'] == 1
    assert large['nodes_for_corrected_half_open_range'] == 23667
    assert large['nodes_for_printed_closed_range'] == 39394
    result = dict(verified=True, checked_at_utc=datetime.now(timezone.utc).isoformat(),
                  dictionary=str(path.relative_to(ROOT)),
                  dictionary_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                  minimal_example=small, six_letter_dictionary=large,
                  correction='For allocated 26-entry nodes on p.36, use 0 <= l < n.',
                  scope='The printed count 23667 and terminal-rank convention are correct.')
    (ROOT / 'results/word_rectangles/prefix-range-verified.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
