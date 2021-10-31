def tag_block(text, clas='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class"{clas}">{text}</{tag}>'


if __name__ == '__main__':
    print(tag_block('block'))
    print(tag_block('inline and class', 'info', True))
    print(tag_block('inline', inline=True))
    print(tag_block(inline=True, text='inline'))
    print(tag_block('failure', clas='error'))
