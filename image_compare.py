import os

def main():
    """Parses two versions of the automatically run demonstrations from the QML
    repository, compares the output of each demo and writes to a file based on the
    differences found.
    """
    master_path = "images/master/images/"
    dev_path = "images/dev/images/"

    master_url = 'https://pennylane.ai/qml/_images/'
    dev_url = 'http://pennylane.ai-dev.s3-website-us-east-1.amazonaws.com/qml/_images/'

    # Get all the filenames
    master_files = os.listdir(master_path)
    dev_files = os.listdir(dev_path)

    #master_automatically_run = set([f for f in master_files if f.startswith("tutorial_")])
    #dev_automatically_run = set([f for f in dev_files if f.startswith("tutorial_")])

    #automatically_run = master_automatically_run.union(dev_automatically_run)

    output_file = open('image_compare.md','w')

    for f in master_files:

        # strip the Sphinx prefix ("sphx_glr_") and the image number and
        # extension suffix (e.g., "_001.png") to obtain the name of the demo
        demo_name = f[9:][:-8]
        image_number = f[-6:][:2]
        output_file.write(f'Demo: {demo_name}, image #: {image_number} \n\n')
        output_file.write(f'<img src="{master_url + f}" alt="alt text" title="image Title" height="150"/> \n\n')

        output_file.write(f'<img src="{dev_url + f}" alt="alt text" title="image Title" height="150"/>')
        output_file.write(f'\n\n---\n\n')

    return 0

if __name__ == '__main__':
    main()
