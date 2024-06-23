from tests import format_name

def test_format_name():
    formatted_name = format_name('anish', 'sharma')
    assert formatted_name == 'Your name: Anish Sharma'