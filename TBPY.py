class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)
 

    def get_updates(self, offset=None, timeout=30):

        method = 'getUpdates'

        params = {'timeout': timeout, 'offset': offset}

        resp = requests.get(self.api_url + method, params)

        result_json = resp.json()['result']

        return result_json

    def send_message(self, chat_id, text):

        params = {'chat_id': chat_id, 'text': text}

        method = 'sendMessage'

        resp = requests.post(self.api_url + method, params)

        return resp

    def send_photo(self, chat_id, photo, caption:str = None):
        params = {'chat_id': chat_id}

        if caption:
            params['caption'] = caption

        files = {'photo': photo}

        method = 'sendPhoto'

        resp = requests.post(self.api_url + method, params, files=files)

        return resp

    def send_audio(self, chat_id, audio, caption:str = None, title:str = None):
        params = {'chat_id': chat_id}

        if caption:
            params['caption'] = caption
        if title:
            params['title'] = title

        files = {'audio': audio}

        method = 'sendAudio'

        resp = requests.post(self.api_url + method, params, files=files)

        return resp

    def send_voice(self, chat_id, voice, caption:str = None):
        params = {'chat_id': chat_id}

        if caption:
            params['caption'] = caption

        files = {'voice': voice}

        method = 'sendVoice'

        resp = requests.post(self.api_url + method, params, files=files)

        return resp

    def send_document(self, chat_id, document, caption:str = None):
        params = {'chat_id': chat_id}

        if caption:
            params['caption'] = caption

        files = {'document': document}

        method = 'sendDocument'

        resp = requests.post(self.api_url + method, params, files=files)

        return resp

    def send_video(self, chat_id, video, caption:str = None, supports_streaming: bool = True):
        params = {'chat_id': chat_id}

        if caption:
            params['caption'] = caption

        if supports_streaming:
            params['supports_streaming'] = supports_streaming

        files = {'video': video}

        method = 'sendVideo'

        resp = requests.post(self.api_url + method, params, files=files)

        return resp

    def get_last_update(self):

        get_result = self.get_updates()

        if len(get_result) > 0:

            last_update = get_result[-1]

        else:

            if get_result != []:
                last_update = get_result[len(get_result)]
            else:
                return []

        return last_update
