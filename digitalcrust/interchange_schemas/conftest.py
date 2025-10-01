def pytest_addoption(parser):
    parser.addoption("--spot", action="store", help="Path to StraboSpot JSON")
    parser.addoption("--checkin", action="store", help="Path to Rockd checkin JSON")
