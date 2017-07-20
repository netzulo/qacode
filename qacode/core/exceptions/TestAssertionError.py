class TestAssertionError(AssertionError):
    def __init__(self, actual, expected, cause, message):
        super(TestAssertionError, self).__init__(self, actual, expected, cause, message)
