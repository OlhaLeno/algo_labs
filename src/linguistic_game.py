from typing import List


def read_from_file(file_name: str) -> List[str]:
    with open(file_name, "r") as file:
        lines = file.readlines()
        words = [line.strip() for line in lines[1:]]
    return words


def write_to_file(file_name: str, result: int):
    with open(file_name, "w") as file:
        file.write(str(result) + "\n")


def len_of_max_chain(readfile: str, writefile: str):
    words_list = read_from_file(readfile)
    words_list.sort(key=len)

    max_chain_len = 1
    dp = {word: 1 for word in words_list}

    for word in words_list:
        for i in range(len(word)):
            previous = word[:i] + word[i + 1:]
            if previous in dp:
                dp[word] = max(dp[word], dp[previous] + 1)
                max_chain_len = max(max_chain_len, dp[word])

    write_to_file(writefile, max_chain_len)


input_file = "wchain.in"
output_file = "wchain.out"
len_of_max_chain(input_file, output_file)
