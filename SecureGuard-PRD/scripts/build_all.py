import os
from build_prd_pages import page_wrapper, base_dir
from generate_part1 import pages_data as p1
from generate_part2 import pages_data as p2
from generate_part3 import pages_data as p3

all_pages = {}
all_pages.update(p1)
all_pages.update(p2)
all_pages.update(p3)

count = 0
for rel_path, (title, section_name, content_body) in all_pages.items():
    full_path = os.path.join(base_dir, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    rendered_html = page_wrapper(title, section_name, rel_path, content_body)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(rendered_html)
    count += 1

print(f"Successfully generated {count} PRD HTML documents in {base_dir}.")
