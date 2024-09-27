import os
import asyncio
from typing import Optional
from dataclasses import dataclass

# Parsing arguments
def parse_args() -> None:
    from argparse import ArgumentParser

    parser = ArgumentParser()
    
    # Group for file
    file_choose = parser.add_argument_group("Choose file/files")
    file_choose.add_argument("--path",
                            type=str,
                            help="For set the file path.")
    file_choose.add_argument("--all",
                            action="store_true",
                            help="For select all the files in specified path.")
    file_choose.add_argument("--files",
                            nargs="+",
                            help="For individual file names in specified path, separate by a space.")
    
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
    
    # Argument for associated data
    parser.add_argument("-ad",
                        "--associated_data",
                        metavar="",
                        type=str,
                        required=False,
                        default=None,
                        help="Optional: Associated data for the encryption algorithm to increase the security of encrypted data.")
    
    # Group for max buffer size and unit
    size_unit = parser.add_argument_group("Set max file buffer size")
    size_unit.add_argument("-bs",
                           "--max_buffer_size",
                           metavar="",
                           type=Optional[int | float],
                           default=256*10**6,
                           help="For set the maximum file size to be placed in RAM for encryption/decryption. (Default: 256 mb.)")
    size_unit.add_argument("-bytes",
                           action="store_true",
                           help="To set unit size to bytes. (Set as default)")
    size_unit.add_argument("-mb",
                           action="store_true",
                           help="To set unit size to megabytes.")
    size_unit.add_argument("-gb",
                           action="store_true",
                           help="To set unit size to gigabytes.")
    
    # Argument for web interface
    parser.add_argument("--web",
                       action="store_true",
                       help="To launch web interface.")
    
    args = parser.parse_args()
    
    # If --all: all files in path
    if args.all == True:
        args.files = os.listdir(args.path)
    
    # If size_unit not specified: set size_unit to bytes
    if not(args.bytes or args.mb or args.gb):
        args.bytes = True
    
    return args

@dataclass
class AlgorithmParams:
    key_bit: int
    nonce_bit: int
    assoc_data: Optional[ str | None ]
    path: str
    files: Optional[ list[str] | None ]

# To create a dataclass
async def set_algo_params(algorithm: str,
                          assoc_data: Optional[ str | None ],
                          path: str,
                          files: Optional[ list[str] | None ]
                          ) -> AlgorithmParams | ValueError:
    match algorithm:
        case "AES-GCM":
            config_args = {
                "algorithm": algorithm,
                "key_bit": 256,
                "nonce_bit": 96,
                "assoc_data": assoc_data,
                "path": path,
                "files": files
            }
            return AlgorithmParams(**config_args)
        
        case "ChaCha20":
            config_args = {
                "algorithm": algorithm,
                "key_bit": 256,
                "nonce_bit": 64,
                "assoc_data": None,
                "path": path,
                "files": files
            }
            return AlgorithmParams(**config_args)
        
        case _:
            raise ValueError(f"Unsupported algorithm: {algorithm}")

class FileHandling:
    import aiofiles
    from cypher import AES_GCM, ChaCha20
    def __init__(self) -> None:
        ...
    

async def main(args) -> None:
    match args.web:
        case True:
            print("Web version")
            exit()
        case _:
            ...

if __name__ == "__main__":
    args = parse_args()
    asyncio.run(main(args))
