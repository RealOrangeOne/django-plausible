from itertools import combinations

import pytest

from plausible import utils


@pytest.mark.parametrize(
    "script_name",
    utils.KNOWN_FILENAMES,
)
def test_known_filenames(script_name):
    assert utils.is_valid_plausible_script(script_name)


@pytest.mark.parametrize(
    "script_name",
    [
        "left-pad.js",
        "plausible.io",
        "plausible..js",
        "plausible.nothing.js",
        "plausible.hash",
        "hash.js",
        "file",
        "/plausible.js",
    ],
)
def test_invalid_filenames(script_name):
    assert not utils.is_valid_plausible_script(script_name)


@pytest.mark.parametrize(
    "variant",
    [
        ".".join(sorted(v))
        for n in range(1, len(utils.BASE_VARIANTS))
        for v in combinations(utils.BASE_VARIANTS, n)
    ],
)
@pytest.mark.parametrize(
    "base_filenames",
    utils.BASE_FILENAMES,
)
def test_variants(variant, base_filenames):
    assert utils.is_valid_plausible_script(f"{base_filenames}.{variant}.js")
