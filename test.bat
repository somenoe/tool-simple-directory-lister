@echo off
setlocal

set PYTHON=python
set MAIN_SCRIPT=main.py
set TEST_FOLDER="C:\Users\otash\Pictures"

echo Running tests for main.py...

echo.
echo Test 1: No arguments (current directory)
%PYTHON% %MAIN_SCRIPT%
echo Exit code: %ERRORLEVEL%
echo.

echo.
echo Test 2: List a specific directory - Test folder
%PYTHON% %MAIN_SCRIPT% "%TEST_FOLDER%"
echo Exit code: %ERRORLEVEL%
echo.

echo.
echo Test 4: Sort by Name - Test folder
%PYTHON% %MAIN_SCRIPT% "%TEST_FOLDER%" -s Name
echo Exit code: %ERRORLEVEL%
echo.

echo.
echo Test 5: Sort by Size - Test folder
%PYTHON% %MAIN_SCRIPT% "%TEST_FOLDER%" -s Size
echo Exit code: %ERRORLEVEL%
echo.

echo.
echo Test 6: Sort by Type - Test folder
%PYTHON% %MAIN_SCRIPT% "%TEST_FOLDER%" -s Type
echo Exit code: %ERRORLEVEL%
echo.

echo.
echo Test 7: Sort by Date Modified - Test folder
%PYTHON% %MAIN_SCRIPT% "%TEST_FOLDER%" -s Date
echo Exit code: %ERRORLEVEL%
echo.

echo.
echo Test 3: List a specific directory - Current Folder
%PYTHON% %MAIN_SCRIPT%
echo Exit code: %ERRORLEVEL%
echo.

echo.
echo Test 8: Sort by Name - Current Folder
%PYTHON% %MAIN_SCRIPT% -s Name
echo Exit code: %ERRORLEVEL%
echo.

echo.
echo Test 9: Sort by Size - Current Folder
%PYTHON% %MAIN_SCRIPT% -s Size
echo Exit code: %ERRORLEVEL%
echo.

echo.
echo Test 10: Sort by Type - Current Folder
%PYTHON% %MAIN_SCRIPT% -s Type
echo Exit code: %ERRORLEVEL%
echo.

echo.
echo Test 11: Sort by Date Modified - Current Folder
%PYTHON% %MAIN_SCRIPT% -s Date
echo Exit code: %ERRORLEVEL%
echo.

echo.
echo Test 12: Invalid argument
%PYTHON% %MAIN_SCRIPT% "%TEST_FOLDER%" -s Invalid
echo Exit code: %ERRORLEVEL%
echo.

echo.
echo Test 13: Non-existent directory
%PYTHON% %MAIN_SCRIPT% "NonExistentDirectory"
echo Exit code: %ERRORLEVEL%
echo.

echo.
echo Tests complete.

endlocal
