import pulsecheck


def test_package_exposes_version():
    assert pulsecheck.__version__ == "0.1.0"
