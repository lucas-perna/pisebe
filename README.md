
# PI-SeBE: Python Interface for Selenium-Browser-Extension

## Description
PI-SeBE is a small python library that lets you create Selenium-Browser-Extension (SeBE) projects and tests from within Python

Links: [Selenium](https://www.selenium.dev) &nbsp; [Selenium-Browser-Extension](https://www.selenium.dev/selenium-ide/)


## Basic Usage

Basic usage is shown below
```python
import pisebe

# Create a project object. Assign the project a new test
p = pisebe.Project()
p.set_url("https://www.example.com")
test = p.add_test("Test 1")

# Add instructions for the test to do
test.add("open","/")
test.add("pause",4000)
test.add("close")

# Export the project as a .side file (which can then be executed by SeBE)
p.export("open_pause_close_example.side")
```
## Advanced Usage: Webscraping
Another good use case is with webscraping. For example, you can use PI-SeBE to make a SeBE test that webscrapes a set of documentation pages from python.org. Below is an example implementation of this.
```python
import pisebe

# Write a javascript snippet that will download the entire html of a webpage when ran
snippet = '''
const txt = document.documentElement.outerHTML; 
var element = document.createElement('a'); 
element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(txt)); 
element.setAttribute('download', 'page.html'); 
element.style.display = 'none'; 
document.body.appendChild(element); 
element.click(); 
document.body.removeChild(element);
'''

# Create a SeBE project to download a set of pages
p = pisebe.Project()
p.set_url("https://docs.python.org/")

main = p.add_test("main")
for library in ["random","fractions","math","pickle","csv","os","time","re"]:
    main.add("open", f"https://docs.python.org/3/library/{library}.html")
    main.add("runScript", snippet)

p.export()
```

## Purpose: Why I made this
I made PI-SeBE while working on a data science project in which I needed to webscrape a website using Selenium. The problem I encountered was that the Selenium-WebDriver needs an internet browser, but I was working from a remote headless server (no internet browser and no graphical interface installed). My solution was to use the Selenium-Browser-Extension (SeBE) from my local desktop and then upload the webscraped data to where it was needed. SeBE already has a built-in IDE, but PI-SeBE connects the two so that you can make your SeBE projects all from within Python.
