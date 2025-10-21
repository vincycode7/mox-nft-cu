from src import BasicNFT as BNFT
from moccasin.boa_tools import VyperContract

PUG_URI = "QmW16U98JrY9HBY36rQtUuUtDnm6LdEeNdAAggmrx3thMa"

def deploy_basic_nft() -> VyperContract:
    bnft = BNFT.deploy()
    print(f"Deployed BasicNFT at address: {bnft.address}\n")
    
    # Mint the first NFT
    print(f"Minting NFT with URI: {PUG_URI} .....\n")
    bnft.mint(PUG_URI)
    
    # Now we can get the token URI
    token_uri = bnft.tokenURI(0)
    print(f"Token URI for token ID 0: {token_uri}\n")
    
    return bnft    

def moccasin_main() -> VyperContract:
    return deploy_basic_nft()
