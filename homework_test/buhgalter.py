documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}

def get_person_by_document_number(doc_number):
    for document in documents:
        if document["number"] == doc_number:
            return document["name"]
    return "Документ не найден"

def get_shelf_by_document_number(doc_number):
    for shelf, docs in directories.items():
        if doc_number in docs:
            return shelf
    return "Документ не найден на полках"

def list_all_documents():
    for document in documents:
        print(f'{document["type"]} "{document["number"]}" "{document["name"]}"')

def add_document(doc_type, doc_number, doc_name, shelf_number):
    if shelf_number not in directories:
        return "Такой полки не существует"
    
    new_document = {"type": doc_type, "number": doc_number, "name": doc_name}
    documents.append(new_document)
    directories[shelf_number].append(doc_number)
    return "Документ успешно добавлен"

def main():
    while True:
        command = input("Введите команду (p, s, l, a) или q для выхода: ").strip().lower()

        if command == 'p':
            doc_number = input("Введите номер документа: ").strip()
            print(get_person_by_document_number(doc_number))

        elif command == 's':
            doc_number = input("Введите номер документа: ").strip()
            print(get_shelf_by_document_number(doc_number))

        elif command == 'l':
            list_all_documents()

        elif command == 'a':
            doc_type = input("Введите тип документа: ").strip()
            doc_number = input("Введите номер документа: ").strip()
            doc_name = input("Введите имя владельца: ").strip()
            shelf_number = input("Введите номер полки: ").strip()
            print(add_document(doc_type, doc_number, doc_name, shelf_number))

        elif command == 'q':
            break

        else:
            print("Неверная команда. Попробуйте снова.")

if __name__ == "__main__":
    main()
