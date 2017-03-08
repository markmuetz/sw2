import nose.tools as ns
import main


def test_names():
    ns.assert_true(main.get_name() == 'bob')