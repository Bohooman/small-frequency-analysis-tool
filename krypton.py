import sys


def analyse(path_to_file: str, length: int) -> None:
    """
    N-gram frequency analysis for classical ciphers (e.g. OverTheWire
    Krypton level 3 -> 4).

    Reads a file, removes all whitespace, cuts the text into consecutive
    blocks of `length` characters and counts how often each block occurs.
    Blocks that appear more than once are printed, most frequent first.

    Why this helps: in a substitution cipher, frequent ciphertext blocks
    usually correspond to frequent plaintext blocks (e.g. "THE", "ING"),
    which gives you a starting point for breaking the cipher.

    Args:
        path_to_file: Path to the text file with the ciphertext.
        length: Block size (1 = single letters, 2 = bigrams, 3 = trigrams ...).

    Note: The text is split into NON-overlapping blocks, starting at
    position 0. Blocks therefore depend on the starting offset.
    """

    # Read the whole file and remove all spaces and line breaks.
    # split() without arguments splits at any whitespace, join() glues
    # the pieces back together, so we get one long string without gaps.
    with open(path_to_file, "r") as f:
        text = "".join(f.read().split())

    # Cut the text into blocks of `length` characters.
    # Example: "ABCDEFG" with length 3 -> ["ABC", "DEF", "G"]
    # (the last block may be shorter if the text doesn't divide evenly)
    blocks = [text[i:i + length] for i in range(0, len(text), length)]

    # Count how often each distinct block occurs.
    # set() gives us every block exactly once, count() tells us how
    # often it appears in the full list.
    counts = {block: blocks.count(block) for block in set(blocks)}

    # Sort by count, highest first, and only print blocks that occur
    # more than once (single occurrences are not useful for analysis).
    for block, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
        if count > 1:
            print(block, count)


def main() -> None:
    # sys.argv[0] is the script name, so we expect exactly 3 entries:
    # script name, file path, block length
    if len(sys.argv) != 3:
        print("usage: python krypton.py '<path_to_file>' '<length>'")
        return
    analyse(sys.argv[1], int(sys.argv[2]))


if __name__ == "__main__":
    main()
