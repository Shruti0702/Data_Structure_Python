class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
        self.temp=None
    def insert(self):
        if self.head==None:
            self.temp=self.head=Node(int(input("enter data to your list")))
        else:
            self.temp.next=Node(int(input("enter data to your list")))
            self.temp=self.temp.next
    def display(self):
        nodes=[]
        if self.head==None:
            print("list is empty")
        else:
            self.temp=self.head
            while(self.temp!=None):
                nodes.append(self.temp.data)
                print(self.temp.data,end="->")
                self.temp=self.temp.next
ll=Linkedlist()
print("press 1: for inserting values to your list:")
choice=int(input())
while(choice==1):
    ll.insert()
    choice = int(input())
ll.display()





