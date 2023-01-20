from jinja2 import Environment, FileSystemLoader
import json

# Loading JSON data from file
with open('data.json', 'r') as file:
    data = json.load(file)

# Creating Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('templates.html')

# Render the template
html = template.render(crate_table=data['crate_table'], sku_table=data['sku_table'], supplier=data['supplier'], supplier_name=data['supplier_name'])

# Output
with open('output.html', 'w') as file:
    file.write(html)