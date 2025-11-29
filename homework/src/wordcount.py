# Ejemplo para casos de uso
# python3 -m homework data/input data/output


import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Count Word in files.")
    parser.add_argument(
        "input", type=str, help="Path to the input folder containing files to process."
    )
    parser.add_argument(
        "output",
        type=str,
        help="Path to the output folder containing files to process.",
    )

    parsed_args = parser.parse_args()

    return parsed_args.input, parsed_args.output


def main():
    input, output = parse_args()
    print(f"input: {input}")
    print(f"output: {output}")
