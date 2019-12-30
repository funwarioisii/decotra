import decotra
import toml


def test_version():
    dict_toml = toml.load(open('pyproject.toml'))
    assert dict_toml['tool']['poetry']['version'] == decotra.__version__
