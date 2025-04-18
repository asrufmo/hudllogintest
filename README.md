# Hudl Login Automation

A simple Selenium-based login test for Hudl using Python + Pytest.

## Setup

1. Clone this repo.
2. Create a `.env` file:
   ```
   BASE_URL=https://www.hudl.com
   HUDL_USERNAME=your_email
   HUDL_PASSWORD=your_password
   ```

3. Install requirements:
   ```
   pip install -r requirements.txt
   ```

4. Run tests:
   ```
   pytest --browser=chrome --html=report.html
   pytest --browser=firefox --html=report.html
   ```

## Notes
- Uses Page Object Model
- No hardcoded credentials or URLs
- Supports `.env` for secure config
- Cross-browser testing: Chrome, Firefox, Edge
- Easy CLI switch via --browser option

## Possible Improvements

- Add Docker support for consistent and isolated test execution
- Integrate with CI/CD (e.g., GitHub Actions, GitLab CI) for automated test runs
- Enable parallel test execution using to speed up test suites
- Archive and visualize test reports (e.g., HTML, Allure) in CI pipelines
- Improve logging and debugging with screenshots on failure