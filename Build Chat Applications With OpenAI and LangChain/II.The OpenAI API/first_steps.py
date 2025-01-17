# %load_ext env
# %dotenv
# Again.

from dotenv import load_dotenv

load_dotenv('.env')

import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')

client = openai.OpenAI()
#
completion = client.chat.completions.create(model='gpt-3.5-turbo',
                                             messages=[{},
                                                       {}])

# 1.model - model that we use

# 'role': 'system'
#         'user'
#         'assistant'
#         'tool'

# 'content': questions
#            instructions
#            ...



# v Visit OpenAI's website
# v Pick a language model.
# v Write the model's name as a string.
# v Opt for a cost-sensitive variant.

# System Message:
# You will be provided with a tweet, and your task is to classify its sentiment
# as positive, neutral, or negative.

# 1.User Message:
# This new movie is extraordinary!

# Assistant Message:
# Positive

# 2.User Message:
# This new album is all right.

# Assistant Message:
# Neutral

# 3.User Message:
# This new book could not have benn written worse!

# Assistant Message:
# Negative

# User Message: This new song blew my mind!
# Assistant Message:
# That's great to hear! Music has such a powerful impact.
# What's the song, and what did you find most striking about it?
# Assistant Message:
# Positive

# client.chat.complections
# Instruct the chatbot to answer questions sarcastically through a system message.

# Pass our question as a user-role message.

# Let's get into it!

completion = client.chat.completions.create(model='gpt-3.5-turbo',
                                             messages=[{'role':'system',
                                                        'content':'''You are Marv, a chatbot that reluctantly
                                                                    answers questions with sarcastic responses'''},
                                                       {'role':'user',
                                                        'content':'''I've recently adopted a dog.
                                                        Could you suggest some dog names?'''}])

print(completion)

print(completion.choices[0].message.content)

completion = client.chat.completions.create(model='gpt-3.5-turbo',
                                             messages=[{'role':'system',
                                                        'content':'''You are Marv, a chatbot that reluctantly
                                                                    answers questions with sarcastic responses'''},
                                                       {'role':'user',
                                                        'content':'''Could you explan brifly what a black hole is?'''}],
                                            max_tokens=250)

print(completion)

print(completion.choices[0].message.content)

# Parameter Affecting a Model's Response
# Maximum number of completion tokens
# Temperature Є [0, 2]
# The opton to streaam a response

completion = client.chat.completions.create(model='gpt-3.5-turbo',
                                             messages=[{'role':'system',
                                                        'content':'''You are Marv, a chatbot that reluctantly
                                                                    answers questions with sarcastic responses'''},
                                                       {'role':'user',
                                                        'content':'''Could you explan brifly what a black hole is?'''}],
                                            max_tokens=250,
                                            temperature=0)

print(completion)

print(completion.choices[0].message.content)

# Here, the turned out the same

# Models with lower temperatures can be used when creating a chatbot for educational purpores

completion = client.chat.completions.create(model='gpt-3.5-turbo',
                                             messages=[{'role':'system',
                                                        'content':'''You are Marv, a chatbot that reluctantly
                                                                    answers questions with sarcastic responses'''},
                                                       {'role':'user',
                                                        'content':'''Could you explan brifly what a black hole is?'''}],
                                            max_tokens=250,
                                            temperature=2)

print(completion)

print(completion.choices[0].message.content)

completion = client.chat.completions.create(model='gpt-3.5-turbo',
                                             messages=[{'role':'system',
                                                        'content':'''You are Marv, a chatbot that reluctantly
                                                                    answers questions with sarcastic responses'''},
                                                       {'role':'user',
                                                        'content':'''Could you explan brifly what a black hole is?'''}],
                                            max_tokens=250,
                                            temperature=0,
                                            seed=365)

print(completion)

print(completion.choices[0].message.content)

# Parameters Affecting a Model's Responese
# Maximum number of completion tokens
# Level of randomness
# Print out the output continuously

completion = client.chat.completions.create(model='gpt-3.5-turbo',
                                             messages=[{'role':'system',
                                                        'content':'''You are Marv, a chatbot that reluctantly
                                                                    answers questions with sarcastic responses'''},
                                                       {'role':'user',
                                                        'content':'''Could you explan brifly what a black hole is?'''}],
                                            max_tokens=250,
                                            temperature=0,
                                            seed=365,
                                            stream=True)

print(completion)

print(completion.choices[0].message.content)

for i in completion:
    print(i.choices[0].delta.content, end="")