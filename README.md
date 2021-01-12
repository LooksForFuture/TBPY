# This is TBPY!

TBPY lets you write your own telegram bot with python with complete control. You can integrate it with any library and can make custom loops.


# Installation

You can easily download this library from github and use it.

# Usage

```python
from tbpy import BotHandler

bot = BotHandler(Your-Token)
new_offset = None
people = []
while True
    bot.get_updates(new_offset)
    last_update = bot.get_last_update()
    if last_update == []:
        continue
    last_update_id = last_update['update_id']
    last_chat_text = last_update['message']['text']
    last_chat_id = last_update['message']['chat']['id']
    last_chat_name = last_update['message']['chat']['first_name']

    if last_chat_text.lower() == '/start':
        if last_chat_id in people:
            bot.send_message(last_chat_id, ‘You are in my list’)
        else:
            people.append(last_chat_name)
            bot.send_message(last_chat_id, ‘Hey {}’.format(last_chat_name))
    elif len(last_chat_text) >= 15 and last_chat_text.lower()[:14] == ‘Tell me about ’:
        bot.send_message(last_chat_id, wikipedia.summary(last_chat_text.lower()[15:]))
    else:
        bot.send_message(last_chat_id, 'I can\'t understand what are you saying.')
    
```

## Tutorials

I will add a tutorials page in this repository soon.
