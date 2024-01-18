import yaml

with open('config.yaml', encoding='utf8') as f :
    config = yaml.load(f, Loader=yaml.SafeLoader)

print(config['credentials'])
print(config['preauthorized'])