import os
import re

for filename in os.listdir("."):
    if not filename.endswith(".md") or not filename.startswith("0"): continue
    if filename == "07_APPENDICES.md": continue # Exclude 07 if it doesn't have a standard References section
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Clean up trailing bad mermaid blocks in Part 2
    if "`{.mermaid" in content:
        # Find the first occurrence of `{.mermaid and truncate the file there
        idx = content.find("`{.mermaid")
        if idx != -1:
            content = content[:idx].rstrip() + "\n"

    # 2. Force ## References to start on a new page
    # First, let's make sure we don't duplicate \newpage if it's already there
    content = content.replace("\\newpage\n\n## References", "## References")
    content = content.replace("\\newpage\n## References", "## References")
    
    # Now replace ## References with \newpage \n\n ## References
    content = content.replace("## References", "\\newpage\n\n## References")
    
    # 3. Ensure the references themselves are properly separated by blank lines (just to be absolutely certain)
    # The previous script already did this, but let's re-verify.
    ref_idx = content.find("## References")
    if ref_idx != -1:
        part1 = content[:ref_idx]
        part2 = content[ref_idx:]
        
        # We need to make sure every [X] starts on a new line and has a blank line above it
        # Actually, the previous script changed `\n\[` to `\n\n\[`.
        # Just to be safe, if there's any `\n[` that isn't `\n\n[`, fix it.
        part2 = re.sub(r'([^\n])\n(\[\d+\] )', r'\1\n\n\2', part2)
        content = part1 + part2

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("done")
