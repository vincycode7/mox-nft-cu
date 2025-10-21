from src import MoodNFT as MNFT
from moccasin.boa_tools import VyperContract
import base64

def deploy_mood_nft() -> VyperContract:
    happy_svg_uri = ""
    sad_svg_uri = ""
    
    # Read the SVG files
    with open("./images/happy.svg", "r") as happy_file:
        happy_svg = happy_file.read()
        happy_svg_uri = svg_base64(happy_svg)

    # Read the sad SVG file
    with open("./images/sad.svg", "r") as sad_file:
        sad_svg = sad_file.read()
        sad_svg_uri = svg_base64(sad_svg)

    mnft = MNFT.deploy(happy_svg_uri, sad_svg_uri)
    mnft.mint_nft()
    mnft.flip_mood(0)
    print(f"Token URI: {mnft.token_uri(0)}")
    return mnft

def moccasin_main() -> VyperContract:
    return deploy_mood_nft()

def svg_base64(svg_str: str) -> str:
    """Convert an SVG string to a base64-encoded data URI."""
    svg_bytes = svg_str.encode('utf-8')
    base64_bytes = base64.b64encode(svg_bytes)
    base64_str = base64_bytes.decode('utf-8')
    return f"data:image/svg+xml;base64,{base64_str}"