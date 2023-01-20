import argparse
import os
import json
import tempfile
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--key", help='Your key')
    parser.add_argument("--val", help='Your value')
    args = parser.parse_args()


    storage_path = Path("C:/Users/flora/PycharmProjects/pythonProject/storage.data")

    if os.path.exists(storage_path):
        if args.val:
            with open(str(storage_path), "r") as f:
                m = json.load(f)
                if args.key in m:
                    m[args.key] = m[args.key] + [args.val]
                else:
                    m.update({args.key: [args.val]})
            with open(str(storage_path), "w") as f:
                json.dump(m, f)
        else:
                with open(str(storage_path), "r") as f:
                    m = json.load(f)
                    if args.key in m:
                        if len(m[args.key]) > 1:
                            print(', '.join(m.get(args.key)))
                        else:
                            print(*m.get(args.key))
                    else:
                        print("None")
    else:
        d = {}
        with open(storage_path, "w") as f:
            if args.val:
                d = {args.key: [args.val]}
                json.dump(d, f)
            else:
                d = {args.key: None}
                print(None)


if __name__ == "__main__":
    main()