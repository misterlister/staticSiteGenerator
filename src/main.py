from textnode import TextNode
from filemanip import delete_directory, copy_dir_contents

static_path = "./static"
public_path = "./public"

def main():
    delete_directory(public_path)
    copy_dir_contents(static_path, public_path)

if __name__ == '__main__':
    main()