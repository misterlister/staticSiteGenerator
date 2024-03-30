import os
from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("Error: No title heading in markdown file")
        

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using the template {template_path}")
    try:
        f = open(from_path, 'r')
        markdown = f.read()
        f.close()
    except Exception:
        print("Error: Could not read from source file")
        return
    try:
        t = open(template_path, 'r')
        template = t.read()
        t.close()
    except Exception:
        print("Error: Could not read from template file")
        return
    htmlNode = markdown_to_html_node(markdown)
    html = htmlNode.to_html()
    title = extract_title(markdown)
    html_with_title = template.replace("{{ Title }}", title)
    full_html = html_with_title.replace("{{ Content }}", html)
    dest_path_dir = os.path.dirname(dest_path)
    os.makedirs(dest_path_dir, exist_ok=True)
    try:
        d = open(dest_path, 'w')
        d.write(full_html)
        d.close()
    except Exception:
        print("Error: Could not write to destination file")
        return
    