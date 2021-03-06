class ReturnInfo(object):
    def __init__(self, code, msg):
        self._code = code
        self._msg = msg

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        if not isinstance(value, int):
            raise ValueError('code must be an integer!')
        self._code = value

    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value
