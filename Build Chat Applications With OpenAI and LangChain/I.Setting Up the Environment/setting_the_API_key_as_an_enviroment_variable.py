import os

print(os.environ.items())

for key, value in os.environ.items():
    print(f"{key}:{value}")

os.environ['OPENAI_API_KEY'] = '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'
# os.environ['OPENAI_API_KEY'] = '...' # Execute the cell

for key, value in os.environ.items():
    if key == 'OPENAI_API_KEY':
        print(f"{key}:{value}")

# # magic coments - %
# %load_ext dotenv
# %dotenv
# But, I don't know they do. They don't work

# You can add multiple key-value pairs inside the file to set them as enviroment variables
