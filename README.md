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
   pytest --html=report.html
   ```

## Notes
- Uses Page Object Model
- No hardcoded credentials or URLs
- Supports `.env` for secure config
# test
