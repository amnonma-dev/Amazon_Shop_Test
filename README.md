# Amazon Shop Test Project

## Porpose
Test various major functionalities of the Amazon shopping application.

## Description

This project tests automation of the Amazon app, using the **Appium mobile testing framework. The tests simulates user actions on the user side.

## Scope

The following functions have been **Implemented**:
1. Login - 1 positive and 1 negative scenarios
2. Navigation - two kinds of navigatings to page and going back
3. Cart actions - Add item to cart test, and empty cart from items test


## Usage
To invoke tests, download the python project, and setup venv with the requirements provided.

When ready, invoke tests with `pytest` command from project root folder.


## Misc
1. The project was developed on a slow machine, which made the SDK emulator unstable. Hence, various explicit sleeps were added to tests, which might not be needed in normal env.

