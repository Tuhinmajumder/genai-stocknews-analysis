import re
PATTERN = re.compile(r"^\d .*", re.M)

def validate_reply(text: str) -> bool:
    return len(PATTERN.findall(text)) >= 5          # five numbered bullets
