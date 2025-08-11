# swag-labs-python-playwright-cucumber

A sample **Python Playwright Cucumber Test** project managed with Maven.

This project demonstrates how to set up and run Playwright tests using Python and Maven.  
It includes a basic test suite for the Sauce Labs 'Swag Labs' site, an ecommerce web app used for testing purposes. For a comprehensive list of practice sites check out [the list](https://www.linkedin.com/pulse/best-test-demo-sites-practicing-software-automation-mark-nicoll-bjsme/).

## Features

- Automated UI testing with Playwright for Python
- Easy build and test execution with Maven
- Example test suite for Swag Labs
- Allure reporting integration (optional)
- GitHub Actions workflow for CI

## Prerequisites

- Python 3.8 or higher

## Setup

1. Clone the repository:
   ```sh
   git clone git@github.com:sahlas/swag-labs-python-playwright-cucumber.git
   cd swag-labs-python-playwright-cucumber
    ```

## Run Tests and Generate Reports

To run the tests and generate reports, execute:

```sh

```

To view the Allure report, you can run:

```sh

```

## Project Structure

```plaintext

```
## Continuous Integration (CI) with GitHub Actions

This project includes a GitHub Actions workflow for automated testing and reporting. The workflow file is located at `.github/workflows/build-test-publish.yml`.

#### Workflow Key Features

- Runs tests on every push and pull request
- Generates and uploads Allure reports as artifacts
- Publishes test reports to GitHub Pages
- Archives Playwright trace files for failed tests
- Supports manual and scheduled workflow triggers

### Manual Trigger

You can also manually trigger the workflow using the "Run workflow" button in the GitHub Actions tab.

### Artifacts and Reports

### Python Playwright Documentation
- [Playwright for Python](https://playwright.dev/python/docs/intro)
- [Playwright Python API Reference](https://playwright.dev/python/docs/api/class-playwright)
