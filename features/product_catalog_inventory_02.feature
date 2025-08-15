Feature: Product Inventory Page
    Background:
        Given Sally has logged in with her account

    Scenario: Sally proceeds to checkout with items in her cart and completes the order
      Given Sally adds the following products to the cart
      | product                           |
      | Sauce Labs Backpack               |
      | Sauce Labs Bolt T-Shirt           |
      | Sauce Labs Fleece Jacket          |
      | Test.allTheThings() T-Shirt (Red) |
      | Sauce Labs Onesie                 |
      When Sally is ready to check out her products
      Then the shopping cart page should indicate all products picked for checkout
      | product                           | quantity | total  |
      | Sauce Labs Backpack               | 1        | $29.99 |
      | Test.allTheThings() T-Shirt (Red) | 1        | $15.99 |
      | Sauce Labs Bolt T-Shirt           | 1        | $15.99 |
      | Sauce Labs Fleece Jacket          | 1        | $49.99 |
      | Sauce Labs Onesie                 | 1        | $7.99  |

      When Sally begins the checkout process
      Then Sally fills in her personal information
      | first_name | last_name | postal_code |
      | Sally      | Shopper   | 12345       |
      And Sally continues to the overview page for review
      | product                           | quantity | total  |
      | Sauce Labs Backpack               | 1        | $29.99 |
      | Sauce Labs Bolt T-Shirt           | 1        | $15.99 |
      | Sauce Labs Fleece Jacket          | 1        | $49.99 |
      | Test.allTheThings() T-Shirt (Red) | 1        | $15.99 |
      | Sauce Labs Onesie                 | 1        | $7.99  |
      When Sally clicks on the finish button
      Then she should see the confirmation message

#    Scenario: Sally modifies her cart and proceeds to checkout then completes the order
#
#      When Sally removes the "Sauce Labs Backpack" from her cart
#      And Sally begins the checkout process
#      Then Sally fills in her personal information
#        | first_name | last_name | postal_code |
#        | Sally      | Shopper   | 12345       |
#      And Sally continues to the overview page for review
#        | product                           | quantity | total  |
#        | Sauce Labs Bolt T-Shirt           | 1        | $15.99 |
#        | Sauce Labs Fleece Jacket          | 1        | $49.99 |
#        | Test.allTheThings() T-Shirt (Red) | 1        | $15.99 |
#        | Sauce Labs Onesie                 | 1        | $7.99  |
#      When Sally clicks on the finish button
#      Then she should see the confirmation message
#