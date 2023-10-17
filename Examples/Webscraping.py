from sys import path
path.append("..")
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
#NOTE: https://docs.python.org/robots.txt tells us we have permission to webscrape on https://docs.python.org/3/

main = p.add_test("main")
for library in ["random","fractions","math","pickle","csv","os","time","re"]:
    main.add("open", f"https://docs.python.org/3/library/{library}.html")
    main.add("runScript", snippet)

p.export() #default export file name is 'custom.side'