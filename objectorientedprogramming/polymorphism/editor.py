
# abc.py
# class ABC
# 

#Editor -> create_module_and_package -> edit -> execute -> debug
# property
# abstractmethod

from abc import ABC

from abc import abstractmethod

class Editor(ABC):

    @abstractmethod
    def create_module_and_package(self):
        pass

    @abstractmethod
    def edit(self):
        pass

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def debug(self):
        pass

class VsCode(Editor):

    def create_module_and_package(self):
        print("vs code create module and package")

    def edit(self):
        print("vscode dit")

    def execute(self):
        print("vsc execute")

    def debug(self):
        print("vscode debug")

    def extensions(self):

        print("vsc extension")



vscode_instance = VsCode()

vscode_instance.create_module_and_package()


# ABC,abstractmethod