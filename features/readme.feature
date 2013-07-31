Feature: README.md
    An over-the-top description of what the README file should contain
    when a student submits it. More of a demonstration of how assignments
    will be specified and tested than anything.

    Scenario: Check the README for completeness
        Given the README.md file
        When we read the file
        Then we see the student's Name
        And the student's Email
        And the student's GitHub Username
        And the student's BitBucket Username
        But not my default information

    Scenario: Make sure the student accounts are real
        Given the README.md file
        When we read the file
        Then we find the GitHub Username on github.com
        And we find the BitBucket Username on bitbucket.org