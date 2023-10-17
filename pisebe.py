from json import dump as json_dump

class Project():
    def __init__(self,url=None,name=None):
        self.data = {"id": "_", "version": "2.0", "name": "Custom Project", "url": "", "tests": [], \
                     "suites": [{"id": "_", "name": "_Suite_", "persistSession": False,"parallel": False,"timeout": 300,"tests": []}],\
                     "urls": [],"plugins": []}
        if url: self.set_url(url)
        if name: self.set_name(name)
    
    def set_url(self,url):
        assert type(url) == str, "url must be type str"
        self.data["url"] = url
        
    def set_name(self,name):
        assert type(name) == str, "name must be type str"
        self.data["name"] = name
        
    def add_test(self,test_name):
        assert type(test_name) == str, "test_name must be type str"
        return self.__Test(name=test_name,project=self)
    
    def export(self,file_name="custom.side"):
        assert type(file_name) == str, "file_name must be type str"
        with open(file_name,"w") as file:
            json_dump(self.data,file)
            
    class __Test():
        def __init__(self,name,project):
            self.project = project
            self.__test_index = len(self.project.data["tests"])
            self.data = {"id": f"{name}_id", "name": name,"commands": []}
            
            suite_tests = self.project.data["suites"][0]["tests"]
            assert f"{name}_id" not in suite_tests, "a test with that name already exists in project"
            suite_tests.append(f"{name}_id")
            self.project.data["tests"].append(self.data)
            
        def update_project(self):
            self.project.data["tests"][self.__test_index] = self.data
            
        def add(self,command,target=None,value=None):
            if not value: value = ""
            if not target: target = ""
            assert type(command) == str, "command must be type str"
            assert type(target) in [int,float,str], "target must be type int, float, or str"
            assert type(value) in [int,float,str], "value must be type int, float, or str"
            
            new_command = {"id": len(self.data["commands"]), "comment": "", "command": command}

            new_command["target"] = target
            new_command["targets"] = []
            new_command["value"] = value
            self.data["commands"].append(new_command)
            self.update_project()          