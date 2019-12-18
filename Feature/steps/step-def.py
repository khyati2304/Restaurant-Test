from behave import *
from pages.website import website

use_step_matcher("re")

@when("I search for Restaurants")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When I search for Restaurants')


@then("I should see some restaurants")
def step_impl(context):
    website.verify_rest()
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then I should see some restaurants')


@given('I want food in "(?P<pin>.+)"')
def step_impl(context, pin):
    """
    :type context: behave.runner.Context
    :type pin: str
    """
    website.search_pincode(pin)
    raise NotImplementedError(u'STEP: Given I want food in "<pin>"')


@given("20% off on Tuesday")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given 20% off on Tuesday')


@when("I click on show participating restaurants")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When I click on show participating restaurants')


@then("show all restaurants")
def step_impl(context):
    website.search_discount_rest()
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then show all restaurants')


@given("the website is loaded")
def step_impl(context):
    website.load_website()
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given the website is loaded')


@then("I see components (?P<components>.+)")
def step_impl(context, components):
    website.verify_component_exists(components)
    """
    :type context: behave.runner.Context
    :type components: str
    """
    raise NotImplementedError(u'STEP: Then I see components <components>')


@when('I will go to "Home Page" page')
def step_impl(context):
    website.goto_page()
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When I will go to "Home Page" page')