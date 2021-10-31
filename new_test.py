def tag_block(content, *args, clas='success', inline=False):
    tag = 'span' if inline else 'div'
    html = content if not callable(content) else content(*args)
    return f'<{tag} class"{clas}">{html}</{tag}>'


def tag_list(*itens):
    lis = ''.join((f'<li>{item}</li>' for item in itens))
    return f'<ul>{lis}</ul>'


if __name__ == '__main__':
    '''print(tag_block('block'))
    print(tag_block('inline and class', 'info', inline=True))
    print(tag_block('inline', inline=True))
    print(tag_block(inline=True, content='inline'))
    print(tag_block('failure', clas='error'))
    print(tag_block(tag_list('item 1', 'item 2'), clas='info'))
    print(tag_block(tag_list, 'Sunday', 'Saturday', clas='info', inline=True))'''


    def result_f1(first, second, third):
        print(f'1 {first}')
        print(f'2 {second}')
        print(f'3 {third}')


    podium = {'first' : 'j', 'second' : 'k', 'third' : 'r'}
    result_f1(**podium)

