import app.io.input as input
import app.io.output as output


def main():
    input_1 = input.input_text()
    input_2 = input.read_from_file('input.txt')
    input_3 = input.read_with_pandas('customers.csv')

    output.print_to_console(input_1)
    output.write_to_file(input_2)
    output.write_pandas(input_3)


if __name__ == "__main__":
    main()