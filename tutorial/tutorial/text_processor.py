import json
import re

if __name__ == '__main__':
    try:
        with open("text.json") as json_file:
            dumped = json.loads(json_file.read())
        with open("output.txt", "w") as output_file:
            for line in dumped:
                for line in line['text'].splitlines(True):
                    if re.match(r'^\s*\[.*\]', line) or re.match(r'^\s*\(.*\)', line) or re.match(r'^\s*$',
                                                                                                  line) or re.match(
                        r'^(R|r)(E|e)(F|f)', line):
                        continue
                    if re.search(r'\.$', line):
                        output_file.write(line.lstrip()[:-2] + '\n')
                        continue
                    if re.search(r',$', line):
                        output_file.write(line.lstrip()[:-2] + '\n')
                        continue


                    output_file.write(line.lstrip())
    except Exception as e:
        print(e)

    try:
        with open("output.txt") as input_file:
            dumped = input_file.read()
        with open("output2.txt", "w") as output_file:
            for line in dumped.splitlines(True):

                if re.match(r'^\s*\[.*\]', line) or re.match(r'^\s*\(.*\)', line) or re.match(r'^\s*$',
                                                                                              line) or re.match(
                    r'^(R|r)(E|e)(F|f)', line):
                    continue
                if re.search(r'\.$', line):
                    output_file.write(line.lstrip()[:-2] + '\n')
                    continue
                if re.search(r',$', line):
                    output_file.write(line.lstrip()[:-2] + '\n')
                    continue


                output_file.write(line.lstrip())


    except Exception as e:
        print(e)
