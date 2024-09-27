from typing import Optional
from secrets import token_bytes
from abc import ABC, abstractmethod

# AES-GCM
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# ChaCha20
from cryptography.hazmat.primitives import poly1305
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import ChaCha20

# Abstract class
class CypherAlgorithm(ABC):
    def __init__(self,
                key_bit: int, # Key length
                nonce_bit: int, # Nonce length
                assoc_data: Optional[ str | None ], # Associated data
                ) -> None:

        self.key = token_bytes(key_bit // 8)
        self.nonce = token_bytes(nonce_bit // 8)
        self.assoc_data = assoc_data
    
    @abstractmethod
    def set_assoc_data(self, assoc_data: str):
        '''
            Optional method:
                If Associated data are required, it can be specified
                Else Associated data is set to None
        '''
        self.assoc_data = assoc_data
    
    @abstractmethod
    async def encrypt(self) -> bytes:
        ...
    
    @abstractmethod
    async def decrypt(self) -> hex:
        ...

class AES_GCM(CypherAlgorithm):
    def __init__(self,
                key_bit: int, # 32 bytes
                nonce_bit: int, # 12 bytes
                assoc_data: Optional[ str | None ]
                ) -> None:
        super().__init__(key_bit, nonce_bit, assoc_data)

    def set_assoc_data(self, assoc_data: str):
        return super().set_assoc_data(assoc_data)
    
    async def encrypt(self) -> bytes:
        print(self.assoc_data)
    
    async def decrypt(self) -> hex:
        ...


class ChaCha20(CypherAlgorithm):
    def __init__(self,
                key_bit: int, # 32 bytes
                nonce_bit: int, # 8 bytes
                assoc_data: Optional[ str | None ]
                ) -> None:
        super().__init__(key_bit, nonce_bit, assoc_data)
    
    def set_assoc_data(self, assoc_data: str):
        return super().set_assoc_data(assoc_data)
    
    async def encrypt(self) -> bytes:
        ...
    
    async def decrypt(self) -> hex:
        ...
