# Created by khyat at 2019-12-17
Feature: Website
  # Enter feature description here

  Scenario Outline: Search for Restaurants in an area
    # Enter steps here
          Given I want food in "<pin>"
          When I search for Restaurants
          Then I should see some restaurants
    Examples:
      |pin|
      |AR51 1AA|

    Scenario: search for all restaurants having 20% off
    # Enter steps here
          Given 20% off on Tuesday
          When I click on show participating restaurants
          Then show all restaurants

      Scenario Outline: load website
        Given the website is loaded
        When I will go to "Home Page" page
        Then I see components <components>
        Examples:
        | components |
        | Login      |
        | Help       |
        | Search     |
