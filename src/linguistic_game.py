from typing import List


def read_from_file(file_name: str) -> List[str]:
    """
    Reads words from a file, skipping the first line and returns them as a list.

    Args:
        file_name (str): The name of the file to read from.

    Returns:
        List[str]: A list of words from the file, stripped of leading and trailing whitespace.
    """
    with open(file_name, "r") as file:
        lines = file.readlines()
        words = [line.strip() for line in lines[1:]]
    return words


def write_to_file(file_name: str, result: int):
    """
    Writes the result to a file.

    Args:
        file_name (str): The name of the file to write to.
        result (int): The result to write to the file.
    """
    with open(file_name, "w") as file:
        file.write(str(result) + "\n")


def len_of_max_chain(readfile: str, writefile: str):
    """
    Finds the length of the longest word chain and saves the result to a file.

    A word chain is formed by removing one character from the previous word to form the next.

    Arguments:
        readfile (str): The name of the input file to read the words.
        writefile (str): The name of the output file to write the result to.
    """
    words_list = read_from_file(readfile)
    words_list.sort(key=len)

    max_chain_len = 1
    dp = {word: 1 for word in words_list}

    for word in words_list:
        for symbol in range(len(word)):
            previous = word[:symbol] + word[symbol + 1:]
            if previous in dp:
                dp[word] = max(dp[word], dp[previous] + 1)
                max_chain_len = max(max_chain_len, dp[word])

    write_to_file(writefile, max_chain_len)


input_file = "wchain.in"
output_file = "wchain.out"
len_of_max_chain(input_file, output_file)
