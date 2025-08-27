Project Latihan Automation Sauce Demo


RUN TEST

1. all test
   - pytest --html=reports/full_report.html --self-contained-html -s
2. basic auth
   - pytest tescases/test_login.py --html=reports/basic_auth_report.html --self-contained-html -s
3. logout
   -  pytest tescases/test_logout.py --html=reports/logout_basic_report.html --self-contained-html -s
