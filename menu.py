from interface import Interface
import sys

class Menu:

    def printDetails(self, titles, chapter):
        print(self.section + chapter)
        for title in titles:
            print(title)
    def __init__(self):
        self.objInterface = Interface()
        self.intro = "Python Cookbook code examples"
        self.description = "\nThis code has been written while learning Python 3."
        self.chapter = "\nPlease choose chapter. [1-15]: "
        self.section = "\nPlease choose section for "
        self.sectionTitles = [
            [
                '1.1. Unpacking a Sequence into Separate Variables',
                '1.2. Unpacking Elements from Iterables of Arbitrary Length',
                '1.3. Keeping the Last N Items',
                '1.4. Finding the Largest or Smallest N Items',
                '1.5. Implementing a Priority Queue',
                '1.6. Mapping Keys to Multiple Values in a Dictionary',
                '1.7. Keeping Dictionaries in Order',
                '1.8. Calculating with Dictionaries',
                '======== From here unavailable',
                '1.9. Finding Commonalities in Two Dictionaries',
                '1.10. Removing Duplicates from a Sequence while Maintaining Order',
                '1.11  Naming a Slice',
                '1.12. Determining the Most Frequently Occurring Items in a Sequence',
                '1.13. Sorting a List of Dictionaries by a Common Key',
                '1.14. Sorting Objects Without Native Comparison Support',
                '1.15. Grouping Records Together Based on a Field',
                '1.16. Filtering Sequence Elements',
                '1.17. Extracting a Subset of a Dictionary',
                '1.18. Mapping Names to Sequence Elements',
                '1.19. Transforming and Reducing Data at the Same Time',
                '1.20. Combining Multiple Mappings into a Single Mapping'
            ]
        ]

        print(self.intro, self.description)
        chapter = input(self.chapter)
        # Why 25? Well, there are 25 prewritten, default methods like __init__ for each class.
        self.printDetails(self.sectionTitles[int(chapter)-1], chapter)
        section = input(self.section + chapter + '. [1-'+str(len(self.objInterface.MethodsCount(chapter))-25) + ']: ')
        print("\n\n--------------Chapter %s, Section %s--------------\n" % (chapter, section))
        getattr(self.objInterface.objDataStructures, "section%s_%s" % (chapter, section))()


menu = Menu();
