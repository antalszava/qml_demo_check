import os
import sys
import difflib
from html_parser import DemoOutputParser

def parse_demo_outputs(filename):
    f = open(filename, "r")
    html_file = f.read()

    parser = DemoOutputParser()
    parser.feed(html_file)

    outputs = []
    for d in parser.data:
        if d != 'Out:':

            if '\n' in d:
                # If there are newlines in the string, then extract each line
                # by splitting and only keep the non-empty ones
                lines = [line for line in d.split("\n") if line != '']
                outputs.extend(lines)
            else:
                outputs.append(d)
    return outputs

def write_file_diff(file_obj, branch, file_url, outputs, diff_indices):

    file_obj.write(f'[{branch}]({file_url}):\n\n')
    if len(diff_indices) > 20:

        # Insert a dropdown option if too many outputs
        file_obj.write(f'<details> \n <summary>\n More \n </summary>\n <pre>\n <code>\n')
        for idx in diff_indices:
            file_obj.write(f'{outputs[idx]}\n')
        file_obj.write(f' </code>\n </pre>\n </details>\n')
    else:
        file_obj.write(f'```\n')
        for idx in diff_indices:
            file_obj.write(f'{outputs[idx]}\n')
        file_obj.write(f'```\n')


def main():
    master_path = "./data/master/demos/"
    dev_path = "./data/dev/demos/"
    files = os.listdir(master_path)

    master_url = 'https://pennylane.ai/qml/demos/'
    dev_url = 'http://pennylane.ai-dev.s3-website-us-east-1.amazonaws.com/qml/demos/'

    automatically_run = [f for f in files if f.startswith("tutorial_")]

    output_file = open('diffs.md','w')

    no_diffs = True
    for filename in automatically_run:
        master_file = os.path.join(master_path, filename)
        master_outputs = parse_demo_outputs(master_file)

        dev_file = os.path.join(dev_path, filename)
        dev_outputs = parse_demo_outputs(dev_file)

        outputs_with_diffs = set()
        for out_idx, (a,b) in enumerate(zip(master_outputs, dev_outputs)):

            demo_name = filename
            for i,s in enumerate(difflib.ndiff(a, b)):
                if s[0]==' ':
                    continue
                elif s[0]=='-':
                    outputs_with_diffs.add(out_idx)

                elif s[0]=='+':
                    pass

        if outputs_with_diffs:
            if no_diffs:
                no_diffs = False

            file_html = filename.replace('.py', '.html')
            master_file_url = master_url + file_html
            dev_file_url = dev_url + file_html

            output_file.write(f'`{filename}`: \n\n')
            output_file.write('---\n\n')

            write_file_diff(output_file, "Master", master_file_url, master_outputs, outputs_with_diffs)
            write_file_diff(output_file, "Dev", dev_file_url, dev_outputs, outputs_with_diffs)

            output_file.write('\n---\n\n')

    if no_diffs:
        output_file.write(f'### No differences found between the tutorial outputs. 🎉\n')

    return 0

if __name__ == '__main__':
    sys.exit(main())
