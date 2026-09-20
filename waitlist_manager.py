# Create a Node class to represent each customer in the waitlist
class Node:

    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''
    #Initialized a new Node with the customer's name and initialized the next
    # pointer with a value of None    
    def __init__(self, name):
        self.name = name
        self.next = None

        #----Code for Testing Functionality----#
# example_node = Node("Jessica")
# print(example_node.name)
# print(example_node.next)

# Create a LinkedList class to manage the waitlist
class LinkedList:
    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''
    #Initialized an empty linked list with the head initialized with a value
    #of None
    def __init__(self):
        self.head = None
    #Defined a method to add names to the front of the linked list
    #It creates a new node with the customer's name, points the new node to the head,
    #and makes the new node the first node
    def add_front(self, name):
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node
    #Defined a method to add names to the end of the linked list
    #It creates a new node with the customer's name and if the list is empty,
    #it makes the new node the head. If the list is not empty, it loops through the list
    #to find the last node and connects it to the new node
    def add_end(self, name):
        new_node = Node(name)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    #Defined a method to remove a customer from the linked list by name
    #It starts at the head and keeps track of the current and previous nodes as it loops through
    #the list. If the list is empty or the name is not found, it returns a message.
    #If the customer's name is the first node, the head is moved to the next node, or if 
    #the customer is elsewhere in the list, it connects the previous node to the
    #node after the customer, removing the customer node from the linked list
    def remove(self, name):
        current = self.head
        previous = None
        if not current:
            return f"Cannot remove '{name}' because the list is empty"
        if current.name == name:
            self.head = current.next
            return
        while current is not None and current.name != name:
            previous = current
            current = current.next
        if current is None:
            return f"'{name}' not found"
        previous.next = current.next
        return
    #Defined a method to print the full waitlist
    #It starts at the head and loops through and prints each customer node.
    #If there are no names in the list, prints a message
    def print_list(self):
        current = self.head
        if not current:
            print("The waitlist is empty")
        else:
            while current:
                print(current.name)
                current = current.next

            #----Code for Testing Functionality----#
# example_list = LinkedList()
# print(example_list.head)
# example_list.print_list()

# example_list.add_end("Jessica")
# example_list.add_end("Daryl")
# print(example_list.head.name)

# example_list.remove("Jessica")
# print(example_list.head.name)

# example_list.add_front("Mary")
# example_list.add_front("Michael")
# example_list.add_front("Melina")

# example_list.print_list()

# example_list.remove("Michael")
# example_list.print_list()

# print(example_list.remove("Somebody"))

def waitlist_generator():
    # Create a new linked list instance
    waitlist = LinkedList()
    
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ")

        if choice == "1":
            name = input("Enter customer name to add to front: ")
            # Call the add_front method
            waitlist.add_front(name)

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            # Call the add_end method
            waitlist.add_end(name)

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            # Call the remove method and store returned messages to print for user visability
            message = waitlist.remove(name)
            if message:
                print(message)

        elif choice == "4":
            print("Current waitlist:")
            # Print out the entire linked list using the print_list method.
            waitlist.print_list()

        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")

# Call the waitlist_generator function to start the program
waitlist_generator()

'''
Design Memo: Write Your Design Memo Include a 200–300 word response in your code or in a .txt file:
- How does your list work?
- What role does the head play?
- When might a real engineer need a custom list like this?
'''
#The waitlist works by using a linked list to store customer names in individual nodes. 
#Each node contains a customer’s name and a next pointer that references the next node in 
#the list. The nodes do not need to be stored next to each other in memory, allowing the 
#list to grow dynamically as new nodes are added. The LinkedList class manages the 
#waitlist and contains a head that points to the first node. It also includes methods to 
#add nodes to the front and end of the waitlist, remove nodes, and print the full waitlist. 
#The methods use pointers to connect the nodes, and some methods use loops to traverse the 
#list. For example, the remove() method starts at the head and moves through the nodes 
#using their next pointers until it finds the customer name that needs to be removed. 
#The waitlist_generator() function makes the program interactive by creating a LinkedList 
#instance and allowing the user to choose whether to add a customer to the front or end, 
#remove a customer, or print the current waitlist. The head plays an important role because 
#it points to the first node and provides a starting point for traversing the list. It is 
#also used when adding a new node to the beginning of the list. For example, the add_end() 
#method uses the head to determine whether the list is empty. If it is empty, the new node 
#becomes the head. If it is not empty, the method starts at the head and follows the next 
#pointers until it reaches the last node, where it connects the new node. A real engineer 
#might use a custom linked list when they do not know how many elements will need to be 
#stored or when an application requires frequent additions and removals. Examples could 
#include managing a waitlist, task queue, or other collection that changes frequently.
