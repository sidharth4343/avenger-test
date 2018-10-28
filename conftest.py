
def pytest_addoption(parser):
    parser.addoption('--browser',default="chrome")
    parser.addoption('--system',default="test")