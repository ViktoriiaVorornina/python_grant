class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def __str__(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        return "Список: " + " -> ".join(elements)

    def __contains__(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


def add_number(linked_list):
    num = int(input("Введіть число: "))
    current = linked_list.head
    while current:
        if current.data == num:
            print("Це число вже є у списку.")
            return
        current = current.next
    linked_list.append(num)



def remove_number(lst):
    num = int(input("Введіть число, яке потрібно видалити: "))
    prev = None
    current = lst.head
    while current:
        if current.data == num:
            if prev is None:
                lst.head = current.next
            else:
                prev.next = current.next
            current = current.next
        else:
            prev = current
            current = current.next

def show_list(lst):
    print("Список:", lst)


def check_number(lst):
    num = int(input("Введіть число, яке потрібно перевірити: "))
    if num in lst:
        print("Це число присутнє у списку.")
    else:
        print("Це число відсутнє у списку.")


def replace_number(lst):
    num = int(input("Введіть число, яке потрібно замінити: "))
    new_num = int(input("Введіть нове число: "))
    current = lst.head
    while current:
        if current.data == num:
            current.data = new_num
        current = current.next

def main():
    linked_list = LinkedList()
    while True:
        print("\nМеню:")
        print("1. Додати нове число до списку")
        print("2. Видалити усі входження числа зі списку")
        print("3. Показати вміст списку")
        print("4. Перевірити, чи є значення у списку")
        print("5. Замінити значення у списку")
        print("6. Вихід")
        choice = input("Виберіть опцію: ")

        if choice == "1":
            add_number(linked_list)
        elif choice == "2":
            remove_number(linked_list)
        elif choice == "3":
            show_list(linked_list)
        elif choice == "4":
            check_number(linked_list)
        elif choice == "5":
            replace_number(linked_list)
        elif choice == "6":
            break
        else:
            print("Невірний вибір опції. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
