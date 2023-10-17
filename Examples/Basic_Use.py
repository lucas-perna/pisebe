from sys import path
path.append("..")
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