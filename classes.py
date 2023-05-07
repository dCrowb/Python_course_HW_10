from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, name, phone):
        new_user = Record(name)
        new_user.add_phone(phone)
        self.data.update({new_user.name_obj.contact_name: new_user})
        return self.data
        

class Record():
    def __init__(self, name):
        self.name_obj = Name(name)
        self.phone_objs = []
        
    def add_phone(self,phone):
        self.phone_objs.append(Phone(phone))
        print(self.phone_objs)

    def change_phone(self, phone, new_phone):
        for object in self.phone_objs:
            if phone == object.phone:
                object.phone = new_phone

    def remove_phone(self, phone):
        for object in self.phone_objs:
            if phone == object.phone:
                self.phone_objs.remove(object)

        
    def show_all_pnone(self):
        for object in self.phone_objs:
            if object is self.phone_objs[0]:
                phone_list = ''
                phone_list += object.phone
            else:
                phone_list += ', ' + object.phone
        return phone_list
        
    def get_list_phones(self):
        phones_list = []
        for object in self.phone_objs:
            phones_list.append(object.phone)
        return phones_list


class Field():
    pass


class Name(Field):
    def __init__(self, name):
        self.contact_name = name


class Phone(Field):
    def __init__(self, phone):
        self.phone = phone



if __name__ == '__main__':
    address_dict = AddressBook()

    user_1_name = Name('Sasha')
    user_2_name = Name('Jeck')

    user_date_1 = Record(user_1_name)
    user_date_2 = Record(user_2_name)

    address_dict.update({user_date_1.name_obj.contact_name: user_date_1})
    address_dict.update({user_date_2.name_obj.contact_name: user_date_2})

    print(address_dict)
    user_1_phone = '+380673528473'
    user_2_phone = '+380677284032'
    user_date_1.add_record(user_1_phone)
    user_date_1.add_record(user_2_phone)
    print(user_date_1.phone)