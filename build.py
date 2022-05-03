import os
import os.path
import json
from jinja2 import Template

def load_template():
    with open('template.html') as template_file:
        template_html = template_file.read()

        return template_html

def load_locales():
    locales = []
    locale_files = os.listdir('locales')
    
    for locale_file in locale_files:
        locale_name = locale_file.split('.')[0]
        locale_file_path = os.path.join('locales', locale_file)

        with open(locale_file_path) as locale_file:
            locale_dictionary = json.load(locale_file)

            locales.append({
                'name': locale_name,
                'dictionary': locale_dictionary,
            })
    
    return locales

def build():
    template_html = load_template()
    locales = load_locales()
    
    for locale in locales:
        index_html = Template(template_html).render(locale['dictionary'])
        locale_name = locale['name']
        index_file_path = 'index-' + locale_name + '.html'

        with open(index_file_path, 'w') as index_file:
            index_file.write(index_html)
        
        if locale_name == 'en_US':
            with open('index.html', 'w') as index_file:
                index_file.write(index_html)

if __name__ == '__main__':
    build()
