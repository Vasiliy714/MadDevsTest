from bs4 import BeautifulSoup
from typing import Generator

MAX_LEN = 4096


def split_message(source: str, max_len: int = MAX_LEN) -> Generator[str, None, None]:

    soup = BeautifulSoup(source, 'html.parser')

    blocks = []
    current_block = []
    current_length = 0

    for element in soup.recursiveChildGenerator():

        element_str = str(element)
        element_len = len(element_str)

        if current_length + element_len > max_len:
            if current_block:
                blocks.append("".join(str(e) for e in current_block))
            current_block = [element]
            current_length = element_len
        else:
            current_block.append(element)
            current_length += element_len

    if current_block:
        blocks.append("".join(str(e) for e in current_block))

    for block in blocks:
        yield block


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 3:
        print("Usage: python main.py <max_len> <html_file>")
        sys.exit(1)

    max_len = int(sys.argv[1])
    html_file = sys.argv[2]

    with open(html_file, 'r', encoding='utf-8') as file:
        source = file.read()

    for idx, fragment in enumerate(split_message(source, max_len)):
        print(f"Fragment #{idx + 1}: {len(fragment)} chars")
        print(fragment)
        print("-" * 20)

        if len(fragment) > max_len:
            raise ValueError("Message fragment is too large to be split.")

