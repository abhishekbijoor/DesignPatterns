from abc import ABC,abstractmethod
# The Composite Pattern is a structural pattern used when you need to treat a group of objects uniformly as a single object. It allows you to compose objects into tree structures to represent part-whole hierarchies.
# 🔹 When to Use?

# ✅ When a single object and a group of objects should be treated the same way.
# ✅ When you need to model a hierarchical structure, like:

#     File System (Folders & Files)
#     UI Components (Buttons, Panels, Frames)
#     Organizational Hierarchies (CEO → Managers → Employees)


class FileComponents(ABC):
    def showdetails(self):
        pass

class File(FileComponents):
    def __init__(self,name,size):
        self.name = name
        self.size = size
    
    def showdetails(self,intent=0):
        print(" "*intent+f"File: {self.name} and size: {self.size}")

class Folder(FileComponents):
    def __init__(self,name):
        self.name = name
        self.children = []
    
    def add(self, component:FileComponents):
        self.children.append(component)

    def showdetails(self,intent = 0):
        print(" "*intent+f"Folder:{self.name}")
        for child in self.children:
            child.showdetails(intent+4)

if __name__ == "__main__":
    file1 = File("resume.pdf",200)
    file2 = File("Photo.jpg",300)
    file3 = File("report.jpg",100)

    root = Folder("root")
    documents = Folder("Documents")
    pictures = Folder("Pictures")

    root.add(documents)
    root.add(pictures)

    documents.add(file1)
    documents.add(file3)

    pictures.add(file2)

    root.showdetails()
                