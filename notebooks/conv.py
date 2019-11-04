import mistune

def get_md(p='log/01.md'):
    with open(p) as f:
        md = mistune.markdown(f.read())
    return md

if __name__ == '__main__':
    md = get_md()
    print(md)
