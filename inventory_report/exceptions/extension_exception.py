class ExtensionException(Exception):
    def __init__(self, correct_type):
        super().__init__('Wrong file type. ' +
                         'Please, use a {} file.' .format(correct_type))
