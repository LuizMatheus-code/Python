from types import resolve_bases


block_atributes = ('block_accesskey', 'block_id')
ul_atributes = ('ul_id', 'ul_style')


def tag_block(content, *args, clas='success', inline=False, **new_atributes):
    tag = 'span' if inline else 'div'
    html = content if not callable(content) else content(*args)
    atributes = get_atributes(new_atributes, block_atributes)
    return f'<{tag} {atributes} class"{clas}">{html}</{tag}>'


def get_atributes(information, tolerable):
    return ' '.join(f'{k.split("_")[-1]}="{v}"'
        for k, v in information.items() if k in tolerable) 
 

def tag_list(*itens, **new_atributes):
    lis = ''.join((f'<li>{item}</li>' for item in itens))
    return f'<ul> {get_atributes(new_atributes, ul_atributes)}>{lis}</ul>'


if __name__ == '__main__':
    '''print(tag_block('block'))
    print(tag_block('inline and class', 'info', inline=True))
    print(tag_block('inline', inline=True))
    print(tag_block(inline=True, content='inline'))
    print(tag_block('failure', clas='error'))
    print(tag_block(tag_list('item 1', 'item 2'), clas='info'))
    print(tag_block(tag_list, 'Sunday', 'Saturday', clas='info', inline=True))
    print(tag_block(tag_list, 'item 1', 'item 2', clas='info', block_acceskey='m', block_id='content', ul_id='list'))'''


    def log(func):
        def decorator(*args, **kwargs):
            print(f'call {func.__name__}')
            print(f'args: {args}')
            print(f'kwargs: {kwargs}')
            result = func(*args, **kwargs)
            print(f'result {result}')
            return result
        return decorator

    @log
    def sum1(x, y):
        return x + y
    
    @log
    def subtraction(x, y):
        return x - y


    sum1(5, 7)
    subtraction(5, y=7)
