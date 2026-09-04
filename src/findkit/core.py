from pathlib import Path

def find(root: str|Path, pattern="*") -> list[str]: return sorted(str(p) for p in Path(root).rglob(pattern))
def find_suffix(root: str|Path, suffix: str) -> list[str]:
    if not suffix.startswith("."): suffix="."+suffix
    return sorted(str(p) for p in Path(root).rglob(f"*{suffix}"))
