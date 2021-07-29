rem pytest -v -m "regression" --html=./Reports/reportsanity.html testCases/ --browser chrome

rem pytest -v -m "regression" --html=./Reports/reportsanity.html testCases/ --browser firefox

rem pytest -v -m "regression" --html=./Reports/reportsanity.html testCases/

rem pytest -v -m "sanity" --html=./Reports/reportsanity.html testCases/ --browser chrome

rem pytest -v -m "sanity" --html=./Reports/reportsanity.html testCases/ --browser firefox

pytest -v -m "sanity" --html=./Reports/reportsanity.html testCases/