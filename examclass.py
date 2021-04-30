

class Chapter:
    def __init__(self, Subject: str, Name: str, Pages: int, Marks: int):
        self.Subject = Subject
        self.Name = Name
        self.Pages = Pages
        self.Marks = Marks

    def __repr__(self):
        return self.Subject + " with " + self.Name


class Exam:
    def __init__(self, examName: str, chapterList: list):
        self.examName = examName
        self.chapterList = chapterList

    def __str__(self) -> str:
        return self.examName + " " + str(self.chapterList)

    def marksList(self):
        MarksofChapters = []
        for chapter in self.chapterList:
            MarksofChapters.append(chapter.Marks)
        return MarksofChapters

    def findMaximumChapterByPage(self):
        PagesofChapters = []
        for chapter in self.chapterList:
            PagesofChapters.append(chapter.Pages)
        index = PagesofChapters.index(max(PagesofChapters))
        return self.chapterList[index]

    def sortChapterByMarks(self):
        chapterList = self.chapterList
        finalChapters = []
        MarksofChapters = self.marksList()
        sortedMarksofChapters = sorted(self.marksList())
        indexes = []
        for number in sortedMarksofChapters:
            indexes.append(MarksofChapters.index(number))
        # return indexes
        for i in indexes:
            finalChapters.append(chapterList[i])
        return finalChapters


if __name__ == "__main__":
    # n = int(input("Enter the number of Chapters : "))
    # listOfChapters = []
    # for i in range(n):
    #     print("Enter record no. "+str(i+1))
    #     chapterSubject = input("Enter the Subject : ")
    #     chapterName = input("Enter the Name : ")
    #     chapterPages = int(input("Enter the pages : "))
    #     chapterMarks = int(input("Enter the marks : "))
    #     listOfChapters.append(
    #         Chapter(chapterSubject, chapterName, chapterPages, chapterMarks))
    # print(listOfChapters)

    listOfChapters = [Chapter('Science', 'Bio', 34, 90), Chapter(
        'Maths', 'Geometry', 20, 71), Chapter('English', 'Jofra', 12, 89)]
    print(listOfChapters)

    # ExamName = input("Enter exam name : ")

    ExamName = "Final"
    exam1 = Exam(ExamName, listOfChapters)
    print(exam1)
    print(exam1.marksList())
    print(exam1.findMaximumChapterByPage())
    print(exam1.sortChapterByMarks())
