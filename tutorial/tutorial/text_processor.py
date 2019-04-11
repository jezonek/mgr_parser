import json
import re

if __name__ == '__main__':
    try:
        with open("text.json") as json_file:
            dumped = json.loads(json_file.read())
        with open("output.txt", "w") as output_file:
            for song in dumped:
                for line in song['text'].splitlines(True):
                    if re.match(r'^\s*\[.*\]', line) or re.match(r'^\s*\(.*\)', line) or re.match(r'^\s*$',
                                                                                                  line) or re.match(
                            r'^(R|r)(E|e)(F|f)', line):
                        continue
                    output_file.write(line.lstrip())

    except Exception as e:
        print(e)
