"""#8 - Hashing"""

class ProbHash:
    def __init__(self, cap):
        self.hashtable = cap * [None]
        self.n = cap

    def hashFunction(self, mykey):
        return int((int(mykey))%(int(self.n)))

    def rehashFunction(self, hashkey):
        return int((int(hashkey)+1)%(int(self.n)))

    def insertData(self, student_obj):
        key = student_obj.getId()
        while (self.hashtable)[self.hashFunction(student_obj.getId())] is not None:
            student_obj.id = self.rehashFunction(student_obj.getId())
        (self.hashtable)[(self.hashFunction((student_obj.getId())))] = [key, student_obj.getName(), student_obj.getGpa()]
        
    def searchData(self, key):
        if (self.hashtable)[self.hashFunction(key)] is not None:
            i = 0
            while True:
                if i+1 > len(self.hashtable):
                    break
                elif ((self.hashtable)[i]) is not None and ((self.hashtable)[i])[0] == int(key):
                    print("Found "+ str(key) +" at index "+ str(i)+".")
                    return Student(((self.hashtable)[i])[0], ((self.hashtable)[i])[1], ((self.hashtable)[i])[2])
                i += 1
        print(str(key) + " does not exist.")

    def printtable(self):
        if self.n == 0:
            print("No Hash Table")
            return
        else:
            print("")
            print("-------------------------------------------------------")
            for i in range(0, self.n):
                exstring = ""
                dddstring = ""
                if (self.hashtable)[i] is not None:
                    string = "| "
                    for j in (self.hashtable)[i]:
                        dddstring += str(j)+" "
                    dstring = dddstring.center(50, " ")
                    if i <= 9:
                        string += str(i)+dstring+" |"
                    else:
                        string += str(i)+dstring+"|"
                    print(string)
                else:
                    string = "| "
                    dstring = exstring.center(50, " ")
                    if i <= 9:
                        string += str(i)+dstring+" |"
                    else:
                        string += str(i)+dstring+"|"
                    print(string)
                print("-------------------------------------------------------")

class Student:
    def __init__ (self, id, name, gpa):
        self.id = id
        self.name = name
        self.gpa = gpa

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getGpa(self):
        return self.gpa

    def printDetail(self):
        print("ID: "+str(self.id))
        print("Name: "+str(self.name))
        print("GPA: "+str(self.gpa))

s1 = Student(65070001, "Sandee Boonmak", 3.05)
s2 = Student(65070077, "SomsakJaidee", 2.78)
s3 = Student(65070021, "SomsriJaiyai", 3.44)
s4 = Student(65070042, "SommaiMeeboon", 2.89)
# s5 = Student(65070153, "Pitchayadit Wasinanon", 0.00)

myHash = ProbHash(20)
myHash.insertData(s1)
myHash.printtable()
myHash.insertData(s2)
myHash.printtable()
myHash.insertData(s3)
myHash.printtable()
myHash.insertData(s4)
myHash.printtable()

print(str(myHash.hashtable))

std = myHash.searchData(65070077)
std.printDetail()
print("-------------------------")
std = myHash.searchData(65070021)
std.printDetail()
print("-------------------------")
std = myHash.searchData(65070042)
std.printDetail()
print("-------------------------")


std = myHash.searchData(65070032)
