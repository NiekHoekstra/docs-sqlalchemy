import json
from collections import defaultdict
from pathlib import Path


def get_relative_name(root: Path, file: Path):
    obj: Path = file.relative_to(root)
    return '/'.join(obj.parts)


def tags_for_notebook(nb: dict) -> set:
    tags = set()
    for cell in nb.get('cells', []):
        for tag in cell.get('metadata', {}).get('tags', []):
            tags.add(tag)
    return tags


def run(src: Path, virtual_root: Path = None):
    if virtual_root is None:
        virtual_root = src
    files = sorted(src.rglob('*.ipynb'), key=lambda path: path.name)
    result = defaultdict(list)
    for file in files:
        if '.ipynb_checkpoints' in file.parts:
            continue
        text = file.read_text(encoding='utf-8')
        nb_json = json.loads(text)
        name = get_relative_name(virtual_root, file)
        for tag in tags_for_notebook(nb_json):
            result[tag].append(name)

    for tag in sorted(result):
        yield tag, result[tag]


def main():
    src = Path(__file__).with_name('notebooks')
    dst = Path(__file__).with_name('index.md')
    index = ['# Alphabetical Index']
    for tag, files in run(src, src.parent):

        lines = [tag, '']
        for file in files:  # type: str
            name = file.split('/')[-1]
            file = file.replace(' ', '%20')
            lines.append(f'- [{name}](./{file})')
        lines.append('')
        index.append('\n'.join(lines))

    dst.write_text('\n'.join(index))


main()
