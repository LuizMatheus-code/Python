def tag_block(content, clas='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class"{clas}">{content}</{tag}>'


def tag_list(*itens):
    lis = ''.join((f'<li>{item}</li>' for item in itens))
    return f'<ul>{lis}</ul>'


if __name__ == '__main__':
    print(tag_block('block'))
    print(tag_block('inline and class', 'info', True))
    print(tag_block('inline', inline=True))
    print(tag_block(inline=True, content='inline'))
    print(tag_block('failure', clas='error'))
    print(tag_block(tag_list('item 1', 'item 2'), clas='info'))
