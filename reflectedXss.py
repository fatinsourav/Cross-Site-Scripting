class xssReflected(Attack):
    def vulnerable(self,handler):
        params = handler.params

        content = params.get('msg', '')
        if len(content):
            content = content[0]

        else:
            content = 'Better luck next time'

        return content
