"""Mobile Screen feature tests."""


import pytest

from Base_Capabilities.Driver_Initialization import *

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('LoginScenarios.feature', 'Verify the login screen components')
def test_verify_the_login_screen_components():
    """Verify the login screen components."""
    return


@given('The application is launched')
def the_application_is_launched():
    """The application is launched."""
    pass



@when('Current Screen Is Mobile Screen')
def current_screen_is_login_screen():
    """Current Screen Is Mobile Screen."""
    pass


@then('01 Verify the Email Field Place Holder')
def verify_the_email_field_place_holder():
    """01 Verify the Email Field Place Holder."""
    # if Fetch_Desired_Capabilities.confirm_platform() != "Android":
    #     loginscreen = __login_i
    #
    # else:
    #     loginscreen = __login_a

    loginscreen.click_Login_Button()

