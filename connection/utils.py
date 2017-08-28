import re


def _extract_to_list(s):
    '''called by get_method_list'''
    number_list = re.search("(?<={).*(?=})", s).group(0).split("|")
    return [re.sub('{.*}', n, s) for n in number_list]


def get_method_list(s):
    '''called by scripts/init_data_method.shell.py'''
    import re
    items = [item for item in re.findall('[\w{}:|-]+', s)
             if not re.search('[A-Z]', item)
             and not re.search('^\d', item)]

    results = []
    for item in items:
        if '{' in item:
            results += _extract_to_list(item)
        else:
            results.append(item)

    return results
