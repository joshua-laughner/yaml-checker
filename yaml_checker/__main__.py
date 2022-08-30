from argparse import ArgumentParser
import yaml
from pprint import pprint


def parse_yaml(yaml_file):
    with open(yaml_file) as f:
        doc = yaml.safe_load(f)
    pprint(doc)


def main():
    p = ArgumentParser(description='Parse and reprint a YAML document to check its correctness')
    p.add_argument('yaml_file', help='The YAML file to check')
    args = p.parse_args()
    parse_yaml(args.yaml_file)


if __name__ == '__main__':
    main()

