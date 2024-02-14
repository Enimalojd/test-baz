from gendiff.differ import generate_diff
from gendiff.data.get_data import save_data
from gendiff.cli import get_reference


def main():
    args = get_reference()
    res = generate_diff(args.format)
    print(res)
    save_data(res)
    print("Data saved successfully.")


if __name__ == "__main__":
    main()