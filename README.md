# Kate - Python Utils
Python extensions for KDE Kate

## 🌐 Sources

* [GeeksForGeeks](https://www.geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/)
* [SQLParse](https://pypi.org/project/sqlparse/) | [SQLParse Documentation](https://sqlparse.readthedocs.io/en/latest/)
* [Pythonfusion](https://pythonfusion.com/table-on-console-python/#0-prettytable) | [StackOverFlow](https://stackoverflow.com/questions/24644656/how-to-print-pandas-dataframe-without-index) - for pretty print tables

## ⚙️ Settings

Go to: **Settings → Configure Kate... → External Tools**<br><br>
Add new Category: **Python Utils**<br><br>
![Screenshot_20221009_115429](https://user-images.githubusercontent.com/17882375/200059159-b0d28f97-127c-4483-9e14-84ba8926b1bc.png)


There are 2 ways for accomplish that goal:
 <br><br>___A) Universal way (works on any platform) is on the picture below___.<br>
|1.|Name|your script|
|--:|--:|:--|
|2.| **Executable**: |State `python` or `python_venv` path|
|3.| **Arguments** are:| `<your python script name>`  `%{Document:Selection_Text}`|<br><br>

<br><br>___B) Executable script (works on Linux)___.<br>
|1.|Name|your script|
|--:|--:|:--|
|2.| **Executable**: |**Prerequisites**<br><li> State `python path` in the script header<br><li>make script executable<br><br>write just script name|
|3.| **Arguments** are:|`%{Document:Selection_Text}`|<br><br>

![Screenshot_20221009_115446](https://user-images.githubusercontent.com/17882375/200059197-36a37b10-7d4e-4c68-8b65-4fddca54608e.png)



Finally, add keyboard shortcut for this tool.
![Screenshot_20221009_115528](https://user-images.githubusercontent.com/17882375/200059228-a0cd503f-3a88-4c64-8d50-0ea707149343.png)

