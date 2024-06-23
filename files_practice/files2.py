from pathlib import Path
import json

numbers = [1, 2, 5, 3, 9, 16]
content = json.dumps(numbers)
path = Path('numbers.json')
path.write_text(content)
if path.exists():
    json_contents = path.read_text()
    print(json.loads(json_contents))