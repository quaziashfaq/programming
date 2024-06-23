#!/usr/bin/env python3

from pathlib import Path
import json

numbers = [i**3 for i in range(1, 11)]
path = Path('numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)

