import os
import difflib
from html_parser import MyHTMLParser

master_path = "./data/master/demos/"
dev_path = "./data/dev/demos/"
files = os.listdir(master_path)

master_url = 'https://pennylane.ai/qml/demos/'
dev_url = 'http://pennylane.ai-dev.s3-website-us-east-1.amazonaws.com/qml/demos/'

automatically_run = [f for f in files if f.startswith("tutorial_")]

output_file = open('diffs.md','w')
output_file.write(f'### Tutorials that differ: \n')

for filename in automatically_run:
    master_file = os.path.join(master_path, filename)

    f = open(master_file, "r")
    html_file_master = f.read()

    dev_file = os.path.join(dev_path, filename)

    g = open(dev_file, "r")
    html_file_dev = g.read()
    
    parser = MyHTMLParser()
    parser.feed(html_file_master)
    master_outputs = []
    for d in parser.data:
        if d != 'Out:':
            if '\n' in d:
                lines = [line for line in d.split("\n") if line != '']
                master_outputs.extend(lines)
            else:
                master_outputs.append(d)
                      
    parser = MyHTMLParser()
    parser.feed(html_file_dev)
    dev_outputs = []
    
    for d in parser.data:
        if d != 'Out:':
            if '\n' in d:
                lines = [line for line in d.split("\n") if line != '']
                dev_outputs.extend(lines)
            else:
                dev_outputs.append(d)

    first = False

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
        
        file_html = filename.replace('.py', '.html')
        master_file_url = master_url + file_html
        dev_file_url = dev_url + file_html
        
        output_file.write(f'`{filename}`: \n\n')
        output_file.write('---\n\n')
        
        if len(outputs_with_diffs) > 20:

            # Insert a dropdown option if too many outputs
            output_file.write(f'[Master]({master_file_url}):\n\n')
            output_file.write(f'<details> \n <summary>\n More \n </summary>\n')
            for idx in outputs_with_diffs:
                output_file.write(f'{master_outputs[idx]} <br>')
            output_file.write(f' </details>\n')
        else:
            output_file.write(f'[Master]({master_file_url}):\n\n')
            output_file.write(f'```\n')
            for idx in outputs_with_diffs:
                output_file.write(f'{master_outputs[idx]}\n')
            output_file.write(f'```\n')
                
        if len(outputs_with_diffs) > 20:
            
            # Insert a dropdown option if too many outputs
            output_file.write(f'\n[Dev]({dev_file_url}):\n\n')
            output_file.write(f'<details> \n <summary>\n More \n </summary>\n')
            for idx in outputs_with_diffs:
                output_file.write(f'{dev_outputs[idx]} <br>')
            output_file.write(f' </details>\n')
        else:
            output_file.write(f'\n[Dev]({dev_file_url}):\n\n')
            output_file.write(f'```\n')
            for idx in outputs_with_diffs:
                output_file.write(f'{dev_outputs[idx]}\n')
            output_file.write(f'```\n')
            
        output_file.write('\n---\n\n')
