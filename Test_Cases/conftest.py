import pytest

# PYTEST HTML REPORT

# A HOOK TO ADD THE ENVIRONMENT INFORMATION TO THE HTML REPORT
def pytest_configure(config):
    config._metadata['Device Name'] = 'Android'
    config._metadata['Project Name'] = 'Mobile Automation Framework'
    config._metadata['Module Name'] = 'Dev Application'
    config._metadata['AppPackage'] = 'com.connectedcontrols.ccdev'
    config._metadata['AppActivity'] = 'com.connectedcontrols.view.activity.onboarding.SplashActivity'
    config._metadata['Tester'] = 'Lakshmi Narayana'


# A HOOK TO DELETE/MODIFY THE ENVIRONMENT INFORMATION FROM THE HTML REPORT
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
