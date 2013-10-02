Feature: README.md
    An over-the-top description of what the README file should contain
    when the appropriate edits are made. Mostly a demo.

    Scenario: Check the README for completeness
        Given the README.md file
        When we read the file
        Then we see the student's Name
        And the student's Email
        And the student's GitHub Username
        But not my default information

    Scenario: Make sure the student account is real
        Given the README.md file
        When we read the file
        Then we find the GitHub Username on github.com
