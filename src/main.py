from filemanip import delete_directory, copy_dir_contents
from generate_content import generate_pages_recursive

static_path = "./static"
public_path = "./public"
content_path = "./content"
template_path = "template.html"

def main():
    delete_directory(public_path)
    copy_dir_contents(static_path, public_path)
    generate_pages_recursive(content_path, template_path, public_path)

if __name__ == '__main__':
    main()