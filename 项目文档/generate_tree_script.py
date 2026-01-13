import os

root_dir = "/Users/taobe/Documents/GitHub/ObsidianVault/项目文档/跃入迷城"
output_file = "/Users/taobe/Documents/GitHub/ObsidianVault/项目文档/跃入迷城目录结构.md"

def get_tree_string(path, prefix=""):
    try:
        entries = os.listdir(path)
    except PermissionError:
        return ""
        
    # Filter hidden files/dirs
    entries = sorted([e for e in entries if not e.startswith('.')])
    
    tree_output = ""
    
    for entry in entries:
        full_path = os.path.join(path, entry)
        
        if os.path.isdir(full_path):
            tree_output += f"{prefix}- **{entry}/**\n"
            tree_output += get_tree_string(full_path, prefix + "  ")
        else:
            tree_output += f"{prefix}- {entry}\n"
            
    return tree_output

try:
    print(f"Generating tree for {root_dir}...")
    content = f"# 跃入迷城 目录结构\n\n"
    # Add root files first? Or just the tree.
    # The prompt asks for directory structure of the folder.
    # Usually we list the contents.
    
    content += get_tree_string(root_dir)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Successfully generated tree at {output_file}")
except Exception as e:
    print(f"Error: {e}")
