# Kate - Python Utils
Python extensions for KDE Kate

## 🌐 Sources

* [GeeksForGeeks](https://www.geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/)
* [SQLParse](https://pypi.org/project/sqlparse/) | [SQLParse Documentation](https://sqlparse.readthedocs.io/en/latest/)
* [Pythonfusion](https://pythonfusion.com/table-on-console-python/#0-prettytable) | [StackOverFlow](https://stackoverflow.com/questions/24644656/how-to-print-pandas-dataframe-without-index) - for pretty print tables

## ⚙️ Settings

Go to: **Settings → Configure Kate... → External Tools**<br>
Add new Category: **Python Utils** and new tool: **Remove duplicate lines**<br>
![screenshot_20210805-235901](https://user-images.githubusercontent.com/17882375/136116471-5fb364c2-c29a-4cef-9623-8fffed0a239d.png)

There are 2 ways for accomplish that goal:
1. State **python** or **python_venv** path in Executable, then Python script and %{Document:Selection_Text} as arguments
    This is universal (works on any platform) and it is on picture above.
2. State python path in the script headers, make script executable, and then state just script will full path as executable and %{Document:Selection_Text} - for Linux environment
![screenshot_20210805-235921](https://user-images.githubusercontent.com/17882375/136116510-8ceab7b9-9c52-46e3-b845-3cd5ca339db2.png)


Finally, add keyboard shortcut for this tool.
![screenshot_20210805-235949](https://user-images.githubusercontent.com/17882375/136116555-9b81b8e6-5b90-444b-99e0-858fdadb351b.png)
