def main():
    try:
        with open('./input.txt') as f:
            # Gotta remove start/end white space otherwise list comprehension breaks.
            calories_file = f.read().strip()
            newline_delim = "\r\n" if calories_file.find(
                "\r\n\r\n") != -1 else "\n"
            elf_calories_strings = calories_file.split(newline_delim * 2)

            str_calories = [x.split(newline_delim)
                            for x in elf_calories_strings]

            sum_calories = [sum([int(y) for y in x]) for x in str_calories]

            sum_calories.sort(reverse=True)
            print(sum(sum_calories[:3]))

    except EnvironmentError:
        print('Error opening input.txt')


if __name__ == "__main__":
    main()
