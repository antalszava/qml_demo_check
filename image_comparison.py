import os
import sys
import difflib

import pytz
from datetime import datetime
from html_parser import DemoOutputParser

TIMEZONE = pytz.timezone("America/Toronto")

def parse_demo_outputs(filename):
    """Parse the outputs produced by a demonstration from the QML repository.

    Args:
        filename (str): the name of the demonstration file. The file is
            expected to be in HTML format.

    Returns:
        list: the list of demonstration outputs
    """
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

def write_file_diff(file_obj, qml_version, file_url, outputs, diff_indices):
    """Parse the outputs produced by a demonstration from the QML repository.

    Args:
        file_obj (object): the file object used to write the diffs found for a
            specific qml_version
        qml_version (str): the version of the QML repository for which results
            are written; e.g., Master or Dev
        file_url (str): the URL for the demo; either a page on the PennyLane
            website or a page on the hosted dev version of the PennyLane website
        outputs (list): the list of demo outputs
        diff_indices (set): the set of indices where a difference was found
    """
    # Write the version name with the associated URL pointing to the demo
    file_obj.write(f'[{qml_version}]({file_url}):\n\n')

    if len(diff_indices) > 20:

        # Insert a dropdown option if too many outputs
        # Note: html tags are being used that are compatible with GitHub
        # markdown
        file_obj.write(f'<details> \n <summary>\n More \n </summary>\n <pre>\n <code>\n')

        # Dump the outputs
        for idx in diff_indices:
            file_obj.write(f'{outputs[idx]}\n')

        file_obj.write(f' </code>\n </pre>\n </details>\n\n')

    else:

        # Create a code block
        file_obj.write(f'```\n')

        # Dump the outputs
        for idx in diff_indices:
            file_obj.write(f'{outputs[idx]}\n')
        file_obj.write(f'```\n\n')


def main():
    """Parses two versions automatically run demonstrations from the QML
    repository, compares the output of each demo and writes a file based on the
    differences found.
    """
    # need to unzip the demo files
    master_path = "/master/tmp/qml_demos/demos/images"
    dev_path = "/dev/tmp/qml_demos/demos/images"

    master_url = 'https://pennylane.ai/qml/demos/'
    dev_url = 'http://pennylane.ai-dev.s3-website-us-east-1.amazonaws.com/qml/demos/'

    # Get all the image files
    master_files = os.listdir(master_path)
    dev_files = os.listdir(dev_path)

    master_images = set([f for f in master_files if f.endswith(".png")])
    dev_images = set([f for f in dev_files if f.endswith(".png")])

    all_images = master_automatically_run.union(dev_automatically_run)

    output_file = open('image_comparison.md','w')

    # Write a time update
    update_time = pytz.utc.localize(datetime.utcnow())
    update_time = update_time.astimezone(TIMEZONE)
    update_time_str = update_time.strftime("%Y-%m-%d  %H:%M:%S")
    output_file.write(f"Last update: {update_time_str} (All times shown in Eastern time)\n")

    demos_with_diffs = []
    database_of_differences = {}
    for filename in all_images:
        # 1. Add the master image to the left
        # 2. Add the dev image to the right
        output_file.write(f"Last update: {update_time_str} (All times shown in Eastern time)\n")

    return 0

if __name__ == '__main__':
    sys.exit(main())
