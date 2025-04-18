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
## Test Scenarios

### 1. Valid Login
- **Test**: Verifies successful login with valid credentials.
- **Scenario**: User enters valid username and password.

### 2. Invalid Username
- **Test**: Verifies that login fails with an invalid username.
- **Scenario**: User enters an invalid username and valid password.

### 3. Invalid Password
- **Test**: Verifies that login fails with an incorrect password.
- **Scenario**: User enters a valid username and an incorrect password.

### 4. Empty Password
- **Test**: Verifies that login fails when no password is provided.
- **Scenario**: User enters a valid username but leaves the password field empty.

## Notes
- Uses Page Object Model
- No hardcoded credentials or URLs
- Supports `.env` for secure config
- Cross-browser testing: Chrome, Firefox, Edge
- Easy CLI switch via --browser option

## Possible Improvements

- The alternative login journey via the footer can be implemented to cover all the scenarios tested for the main login page.
- Add Docker support for consistent and isolated test execution
- Integrate with CI/CD (e.g., GitHub Actions, GitLab CI) for automated test runs
- Enable parallel test execution using to speed up test suites
- Archive and visualize test reports (e.g., HTML, Allure) in CI pipelines
- Improve logging and debugging with screenshots on failure
