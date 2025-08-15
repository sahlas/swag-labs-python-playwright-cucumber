Feature: Login Validation Errors

  Scenario Outline: Entering user details and checking for errors
    Given I navigate to the user details page
    When I enter "<username>" and "<password>" and submit the form
    Then I should see a "<message>"

    Examples: Valid and invalid inputs
      | username      | password        | message                                                     |
      | standard_user | no_secret_sauce | Username and password do not match any user in this service |
      | stupid_user   | secret_sauce    | Username and password do not match any user in this service |
      | NULL          | NULL            | Username is required                                        |
      | standard_user | NULL            | Password is required                                        |
      | NULL          | secret_sauce    | Username is required                                        |

