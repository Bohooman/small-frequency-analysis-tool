# small-frequency-analysis-tool
My project made to solve krypton 3 -> 4.

## What it does

The script reads a text file, removes all spaces and line breaks, and splits the text into consecutive blocks of a length you choose (1 = single letters, 2 = bigrams, 3 = trigrams, ...). It then counts how often each block appears and prints every block that occurs more than once, most frequent first.

This helps with breaking classical ciphers: frequent blocks in the ciphertext often hint at frequent blocks in the plaintext or at repeating patterns.

## Usage

```sh
python krypton.py '<path_to_file>' '<length>'
```

- `<path_to_file>`: path to the file containing the ciphertext
- `<length>`: block size as a whole number

Put the path in quotation marks so that spaces or special characters don't cause errors.

## Example

```sh
python krypton.py 'ciphertext.txt' 3
```

Example output (block, count):

```
ABC 4
XYZ 2
```

## Notes

- Blocks do not overlap and always start at position 0, so the results depend on the starting offset.
- Requires Python 3, no external libraries.
