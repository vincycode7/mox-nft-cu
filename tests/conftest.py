import pytest
from script.deploy_basic_nft import deploy

@pytest.fixture
def counter_contract():
    return deploy()