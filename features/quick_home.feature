Feature: A website's logo returns the user to the homepage

Scenario: Amazon
    Given that we have gone to www.amazon.com
    When we click on the logo in the top left corner
    Then we return to the www.amazon.com

Scenario: Ebay
    Given that we have gone to www.ebay.com
    When we click on the logo in the top left corner
    Then we return to the www.ebay.com

Scenario Outline: 
    Given that we have gone to a website
    When we click on the logo
    Then we return to the homepage

Examples: Various websites
    | website  | homepage         |
    | Hallmark | www.hallmark.com |
    | Walmart  | www.walmart.com  |
    | Domino's | www.dominos.com  |
