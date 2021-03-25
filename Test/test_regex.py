import unittest
import re

lstFiles = [
    r"E:\Mipony\C# Machine Learning Projects.rar",
    r"E:\Mipony\Concurrency in C# Cookbook, 2nd Edition.rar",
    r"E:\Mipony\Hands-On Design Patterns with C# and .NET Core.rar",
    r"E:\Mipony\Hands-On Microservices with C# 8 and .NET Core 3.0.pdf",
    r"E:\Mipony\Hands-On Object-Oriented Programming with C#.mp4",
    r"E:\Mipony\Microsoft Visual C# Step by Step, 9th Edition.pdf",
    r"E:\Mipony\Programming C# 8.0..rar",
    r"E:\Mipony\Starting out with Visual C#, 4th Edition.rar",
    r"E:\Mipony\C#\Beginning C# 7 Programming...o 2017.rar",
    r"E:\Mipony\C#\C# Programming for Absolute Beginners.pdf",
    r"E:\Mipony\C#\Gray Hat C#.mp4",
    r"E:\Mipony\C#\Microsoft Visual C# Step by Step, 8th Edition.part",
    r"E:\Mipony\C#\Professional C# 7 and .NET....part2.rar",
    r"E:\Mipony\organizar\C# EF - Insert Update Delete.zip",
    r"E:\Mipony\windows 8\Design Patterns in C#, 2nd Edition.pdf",
    r"E:\Mipony\windows 8\Proga\pdf\LinqtoObjects\Microsoft Visual C# Step by Step, 9th Edition.pdf",
    r"E:\Mipony\Core Java Volume I Fundamentals, 10th Edition.part1.rar",
    r"E:\Mipony\Core Java Volume I Fundamentals, 11th Edition.part1.part",
    r"E:\Mipony\Core Java Volume II Advanced Features, 10th Edition.part2.pdf",
    r"E:\Mipony\Core Java Volume II Advanced Features, 11th Edition.part1.rar",
    r"E:\Mipony\Developing Java Applications with Spring and Spring Boot.rar",
    r"E:\Mipony\Hands-On Enterprise Java Microservices with Eclipse MicroProfile.mp4",
    r"E:\Mipony\Introducing Jakarta EE CDI Contexts and Dependency Injection for Enterprise Java Development.pdf",
    r"E:\Mipony\Introduction to Java Programming and Data Structures, Comprehensive Version, 11th Edition.zip",
    r"E:\Mipony\Java 11 Cookbook - Second Edition.epub",
    r"E:\Mipony\Java 11 Programming for Beginners [Video].part2.rar",
    r"E:\Mipony\Java A Beginner's Guide, 8...dition.zip",
    r"E:\Mipony\Java Coding Problems.zip",
    r"E:\Mipony\Java EE 8 Recipes.part"
]


def rar(file):
    regex = re.compile(r'.*\.rar$', re.IGNORECASE)
    
    if(regex.match(file)):
        return True
    return False


lstFilesRAR = filter(rar, lstFiles)



class TettRegex(unittest.TestCase):

    def setup():
        pass

    def tearDown(self) -> None:
        pass

    def test_one_extension(self):
        regex = re.compile(r'.*\.rar$', re.IGNORECASE)
        for name in lstFilesRAR:
            self.assertRegex(name, regex)

    def test_multiple_extension(self):
        regex = re.compile(r'.*\.(rar|pdf|zip|mp4|part|epub)$', re.IGNORECASE)
        for name in lstFiles:

            self.assertRegex(name, regex)
            


if __name__ == "__main__":
    unittest.main()
