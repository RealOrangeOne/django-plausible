BASE_FILENAMES = ["plausible", "script", "analytics"]

BASE_VARIANTS = {
    "hash",
    "outbound-links",
    "exclusions",
    "compat",
    "local",
    "manual",
    "file-downloads",
    "dimensions",
}

KNOWN_FILENAMES = ["p.js", "plausible.js"]


def is_valid_plausible_script(filename: str) -> bool:
    """
    Validate a script name against allowed values


    See also https://plausible.io/docs/script-extensions
    """
    if filename in KNOWN_FILENAMES:
        return True

    try:
        base_name, *variants, extension = filename.split(".")
    except ValueError:
        return False

    if extension != "js" or base_name not in BASE_FILENAMES:
        return False

    return BASE_VARIANTS.issuperset(variants)
