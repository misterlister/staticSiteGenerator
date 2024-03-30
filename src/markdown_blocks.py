BLOCK_TYPE_PARAGRAPH = "paragraph"
BLOCK_TYPE_HEADING = "heading"
BLOCK_TYPE_CODE = "code"
BLOCK_TYPE_QUOTE = "quote"
BLOCK_TYPE_U_LIST = "unordered_list"
BLOCK_TYPE_O_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    non_empty_blocks = []
    for block in blocks:
        stripped_block = block.strip()
        if len(stripped_block) > 0:
            non_empty_blocks.append(stripped_block)
    return non_empty_blocks

def block_to_block_type(block):
    lines = block.split("\n")
    
    if (
        block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")
    ):
        return BLOCK_TYPE_HEADING
    
    if (
        len(lines) > 1
        and lines[0].startswith("```")
        and lines[-1].startswith("```")
    ):
        return BLOCK_TYPE_CODE
    
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BLOCK_TYPE_PARAGRAPH
        return BLOCK_TYPE_QUOTE
    
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BLOCK_TYPE_PARAGRAPH
        return BLOCK_TYPE_U_LIST
    
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return BLOCK_TYPE_PARAGRAPH
        return BLOCK_TYPE_U_LIST
    
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BLOCK_TYPE_PARAGRAPH
            i += 1
        return BLOCK_TYPE_O_LIST
    
    return BLOCK_TYPE_PARAGRAPH