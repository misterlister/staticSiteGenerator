from textnode import TextNode
from filemanip import delete_directory, copy_dir_contents
from generate_content import generate_page

static_path = "./static"
public_path = "./public"
content_path = "./content"
template_path = "template.html"

def main():
    delete_directory(public_path)
    copy_dir_contents(static_path, public_path)
    generate_page(content_path+"/index.md", template_path, public_path+"/index.html")

if __name__ == '__main__':
    main()