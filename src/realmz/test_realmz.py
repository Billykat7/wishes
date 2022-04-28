from .factory                                import GetInput


def test_birthday_wishes():
    """
    Tests the birthday functionality
    Asserts it to '1' which is the birthday corresponding choice selection
    :return:
    """

    resp = GetInput('1', crontab='Y').get_input_redirect()
    assert resp == '1'

    return resp


def test_anniversary_wishes():
    """
    Tests the anniversary functionality
    Asserts it to '2' which is the anniversary corresponding choice selection
    :return:
    """

    resp = GetInput('2', crontab='Y').get_input_redirect()
    assert resp == '2'

    return resp
