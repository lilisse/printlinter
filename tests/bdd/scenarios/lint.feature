Feature: Lint

    # TODO: When we add config option in command line, add scenario for this


    # Files
    Scenario: Lint an existing file with print and ignore inline
        Given I want lint a file
        And That exist
        And Contains print
        And Contains ignore inline
        When I launch the linter
        Then The linter end without error
        And 0 errors have been found

    Scenario: Lint an existing file with print and ignore block
        Given I want lint a file
        And That exist
        And Contains print
        And Contains ignore block
        When I launch the linter
        Then The linter end without error
        And 0 errors have been found

    Scenario: Lint an existing file with print and ignore file
        Given I want lint a file
        And That exist
        And Contains print
        And Contains ignore file
        When I launch the linter
        Then The linter end without error
        And 0 errors have been found

    Scenario: Lint an existing file with print and ignore next line
        Given I want lint a file
        And That exist
        And Contains print
        And Contains ignore next line
        When I launch the linter
        Then The linter end without error
        And 0 errors have been found

    Scenario: Lint an existing file with print without ignore
        Given I want lint a file
        And That exist
        And Contains print
        And Does not contains ignore
        When I launch the linter
        Then The linter end without error
        And 1 errors have been found

    Scenario: Lint an existing file with print and a default full config file
        Given I want lint a file
        And That exist
        And Contains print
        And Does not contains ignore
        And take a default full config file
        When I launch the linter
        Then The linter end without error
        And 0 errors have been found

    Scenario: Lint an existing file with print and a default partial config file
        Given I want lint a file
        And That exist
        And Contains print
        And Does not contains ignore
        And take a default partial config file
        When I launch the linter
        Then The linter end without error
        And 1 errors have been found

    Scenario: Lint an existing file with print and a custom full config file
        Given I want lint a file
        And That exist
        And Contains print
        And Does not contains ignore
        And take a custom full config file
        When I launch the linter
        Then The linter end without error
        And 0 errors have been found

    Scenario: Lint an existing file with print and a custom partial config file
        Given I want lint a file
        And That exist
        And Contains print
        And Does not contains ignore
        And take a custom partial config file
        When I launch the linter
        Then The linter end without error
        And 1 errors have been found

    Scenario: Lint an existing file without print
        Given I want lint a file
        And That exist
        And Does not contains print
        When I launch the linter
        Then The linter end without error
        And 0 errors have been found

    Scenario: Lint a file doesn't exist
        Given I want lint a file
        And That does not exist
        When I launch the linter
        Then The linter end with an error

    # Folders
    Scenario: Lint an existing folder with print and ignore inline
        Given I want lint a folder
        And That exist
        And Contains print
        And Contains ignore inline
        When I launch the linter
        Then The linter end without error
        And 2 errors have been found

    Scenario: Lint an existing folder with print and ignore block
        Given I want lint a folder
        And That exist
        And Contains print
        And Contains ignore block
        When I launch the linter
        Then The linter end without error
        And 2 errors have been found

    Scenario: Lint an existing folder with print and ignore file
        Given I want lint a folder
        And That exist
        And Contains print
        And Contains ignore file
        When I launch the linter
        Then The linter end without error
        And 2 errors have been found

    Scenario: Lint an existing folder with print and ignore next line
        Given I want lint a folder
        And That exist
        And Contains print
        And Contains ignore next line
        When I launch the linter
        Then The linter end without error
        And 2 errors have been found

    Scenario: Lint an existing folder with print without ignore
        Given I want lint a folder
        And That exist
        And Contains print
        And Does not contains ignore
        When I launch the linter
        Then The linter end without error
        And 3 errors have been found

    Scenario: Lint an existing folder with print and a default full config file
        Given I want lint a folder
        And That exist
        And Contains print
        And Does not contains ignore
        And take a default full config file
        When I launch the linter
        Then The linter end without error
        And 2 errors have been found

    Scenario: Lint an existing folder with print and a default partial config file
        Given I want lint a folder
        And That exist
        And Contains print
        And Does not contains ignore
        And take a default partial config file
        When I launch the linter
        Then The linter end without error
        And 3 errors have been found

    Scenario: Lint an existing folder with print and a custom full config file
        Given I want lint a folder
        And That exist
        And Contains print
        And Does not contains ignore
        And take a custom full config file
        When I launch the linter
        Then The linter end without error
        And 2 errors have been found

    Scenario: Lint an existing folder with print and a custom partial config file
        Given I want lint a folder
        And That exist
        And Contains print
        And Does not contains ignore
        And take a custom partial config file
        When I launch the linter
        Then The linter end without error
        And 3 errors have been found

    Scenario: Lint an existing folder without print
        Given I want lint a folder
        And That exist
        And Does not contains print
        When I launch the linter
        Then The linter end without error
        And 0 errors have been found

    Scenario: Lint a folder doesn't exist
        Given I want lint a folder
        And That does not exist
        When I launch the linter
        Then The linter end with an error

    #  Current work directory "."
    Scenario: Lint the current work directory with print and ignore inline
        Given I want lint the current work directory
        And Contains print
        And Contains ignore inline
        When I launch the linter
        Then The linter end without error
        And 2 errors have been found

    Scenario: Lint the current work directory with print and ignore block
        Given I want lint the current work directory
        And That exist
        And Contains print
        And Contains ignore block
        When I launch the linter
        Then The linter end without error
        And 2 errors have been found

    Scenario: Lint the current work directory with print and ignore file
        Given I want lint the current work directory
        And That exist
        And Contains print
        And Contains ignore file
        When I launch the linter
        Then The linter end without error
        And 2 errors have been found

    Scenario: Lint the current work directory with print and ignore next line
        Given I want lint the current work directory
        And That exist
        And Contains print
        And Contains ignore next line
        When I launch the linter
        Then The linter end without error
        And 2 errors have been found

    Scenario: Lint the current work directory with print without ignore
        Given I want lint the current work directory
        And Contains print
        And Does not contains ignore
        When I launch the linter
        Then The linter end without error
        And 3 errors have been found

    Scenario: Lint the current work directory without print
        Given I want lint the current work directory
        And Does not contains print
        When I launch the linter
        Then The linter end without error
        And 0 errors have been found
