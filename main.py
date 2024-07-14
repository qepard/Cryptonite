# Parsing arguments
def parse_args() -> None:
    from argparse import ArgumentParser

    parser = ArgumentParser()
    
    # Group for file
    file_choose = parser.add_mutually_exclusive_group(required=False)
    file_choose.add_argument("--all",
                            action="store_true",
                            help="For select all the files in folder. Selected by default.")
    file_choose.add_argument("--files",
                            nargs="+",
                            help="For individual file names, separate by a space.")
    file_choose.add_argument("--path",
                            type=str,
                            help="For the file path.")
    
    # Argument for algorithm
    parser.add_argument("--algo",
                        type=str,
                        required=False,
                        choices=["AES-GCM", "ChaCha20"],
                        default="AES-GCM",
                        help="Choose an encryption/decryption algorithm (Default: AES-GCM).")
    
    # Group for operating mode
    mode_choose = parser.add_mutually_exclusive_group(required=False)
    mode_choose.add_argument("--encrypt",
                            action="store_true",
                            help="Select encryption mode.")
    mode_choose.add_argument("--decrypt",
                            action="store_true",
                            help="Select decryption mode.")
    
    return parser.parse_args()

def main(args) -> None:
    pass

if __name__ == "__main__":
    args = parse_args()
    main(args)
