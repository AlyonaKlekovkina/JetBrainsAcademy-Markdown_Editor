import os

def form_header_markdown(marked_down_text):
    level = int(input('Level: '))
    if level < 1 or level > 6:
        print('The level should be within the range of 1 to 6')
        level = int(input('Level: '))
    text = input('Text: ')
    markup = '#'*level
    result = "{} {}".format(markup, text)
    marked_down_text.append(result)
    return marked_down_text


def form_plain_markdown(marked_down_text):
    text = input('Text: ')
    marked_down_text.append(text)
    return marked_down_text


def form_bold_markdown(marked_down_text):
    text = input('Text: ')
    result = "**{}**".format(text)
    marked_down_text.append(result)
    return marked_down_text


def form_italic_markdown(marked_down_text):
    text = input('Text: ')
    result = "*{}*".format(text)
    marked_down_text.append(result)
    return marked_down_text


def form_inlinecode_markdown(marked_down_text):
    text = input('Text: ')
    result = '`{}`'.format(text)
    marked_down_text.append(result)
    return marked_down_text


def form_newline_markdown(marked_down_text):
    marked_down_text.append('\n')
    return marked_down_text


def form_link_markdown(marked_down_link):
    label = input('Label: ')
    url = input('URL: ')
    result = '[{}]({})'.format(label, url)
    marked_down_link.append(result)
    return marked_down_link


def form_list_markdown(info):
    n_rows = int(input('Number of rows: '))
    if n_rows <= 0:
        print('The number of rows should be greater than zero')
        n_rows = int(input('Number of rows: '))
    result = ''
    for i in range(1, n_rows + 1):
        element = input('Row #{}: '.format(i))
        if info == 'ordered-list':
            result = '{}. {}\n'.format(i, element)
        if info == 'unordered-list':
            result = '* {}\n'.format(element)
        marked_down_text.append(result)


def write_to_file():
    if os.path.exists('output.md'):
        os.remove('output.md')
        file = open('output.md', 'w', encoding='utf-8')
        for i in marked_down_text:
            file.write(i)
        file.close()
    else:
        file = open('output.md', 'w', encoding='utf-8')
        for i in marked_down_text:
            file.write(i)
        file.close()


marked_down_text = []
list_of_formatters = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'new-line', 'unordered-list', 'ordered-list']
list_of_special_commands = ['!help', '!done']
while True:
    ask_for_formatter = input('Choose a formatter: ')
    if ask_for_formatter == '!help':
        print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
        print("Special commands: !help !done")
    if ask_for_formatter == '!done':
        write_to_file()
        break
    if ask_for_formatter not in list_of_formatters and ask_for_formatter not in list_of_special_commands:
        print('Unknown formatting type or command')
    if ask_for_formatter == 'plain':
        form_plain_markdown(marked_down_text)
        print(''.join(marked_down_text))
    if ask_for_formatter == 'bold':
        form_bold_markdown(marked_down_text)
        print(''.join(marked_down_text))
    if ask_for_formatter == 'italic':
        form_italic_markdown(marked_down_text)
        print(''.join(marked_down_text))
    if ask_for_formatter == 'header':
        form_header_markdown(marked_down_text)
        for i in marked_down_text:
            print(i)
        print('')
        marked_down_text.append('\n')
    if ask_for_formatter == 'link':
        form_link_markdown(marked_down_text)
        print(''.join(marked_down_text))
    if ask_for_formatter == 'inline-code':
        form_inlinecode_markdown(marked_down_text)
        print(''.join(marked_down_text))
    if ask_for_formatter == 'new-line':
        form_newline_markdown(marked_down_text)
        print(''.join(marked_down_text))
    if ask_for_formatter == 'ordered-list':
        form_list_markdown('ordered-list')
        print(''.join(marked_down_text))
    if ask_for_formatter == 'unordered-list':
        form_list_markdown('unordered-list')
        print(''.join(marked_down_text))
