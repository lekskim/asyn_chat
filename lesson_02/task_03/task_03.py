import yaml

DATA_IN = {'data_client': ['first_name', 'last_name', 'birth_date', 'gender'],
           'experience': 5,
           'data_credits': {'first_name': 'Ivan',
                           'last_name': 'Ivanov',
                           'birth_date': '01.01.2000',
                           'gender': 'male'}
           }

with open('file.yaml', 'w', encoding='utf-8') as f_in:
    yaml.dump(DATA_IN, f_in, default_flow_style=False, allow_unicode=True, sort_keys=False
)

with open("file.yaml", 'r', encoding='utf-8') as f_out:
    DATA_OUT = yaml.load(f_out, Loader=yaml.SafeLoader)

print(DATA_IN == DATA_OUT)
