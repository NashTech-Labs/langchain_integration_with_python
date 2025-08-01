Feature: Login Page Functionality

  Scenario: login into Swag Labs
    Given I launch the browser
    When I enters username and password
    Then I should see the inventory page
