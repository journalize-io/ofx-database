import os

import jinja2
import yaml

# Template for each OFX data point
TEMPLATE_FILE = "ofx_template.md"

# Input directory of YAML files containing OFX data
INPUT_DIR = "ofx"

# Output folder for mkdocs
OUTPUT_DIR = "docs/Connections"

# Initialize Jinja template
templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
template = templateEnv.get_template(TEMPLATE_FILE)

# Iterate through YAML files and convert to markdown using template
for filename in os.listdir(INPUT_DIR):
    if filename == 'readme.txt':
        continue

    # Parse YAML
    yaml_path = os.path.join(INPUT_DIR, filename)
    parsed_yaml = yaml.load(open(yaml_path, "r"), Loader=yaml.Loader)

    # Use Jinja to generate output
    outputText = template.render(**parsed_yaml)

    # Save new markdown file
    file_root, file_ext = os.path.splitext(filename)
    out_fd = os.path.join(OUTPUT_DIR, file_root + ".md")
    with open(out_fd, "w") as fh:
        fh.write(outputText)