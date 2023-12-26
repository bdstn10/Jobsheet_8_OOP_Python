class Contact:
    def __init__(self, name, phone):
        # Definisikan atribut/variabel dari fungsi init.
        self.name = name
        self.phone = phone

    def get_name(self):
        # Lengkapi metode ini untuk mengembalikan nama kontak
        return self.name

    def get_phone(self):
        # Lengkapi metode ini untuk mengembalikan nomor telepon kontak
        return self.phone

    def __str__(self):
        return f"{self.get_name()}: {self.get_phone()}"

class ContactList:
    def __init__(self):
        # Definisikan atribut/variabel daftar kontak dari fungsi init sebagai List.
        self.contacts = []

    def add_contact(self, contact):
        # Lengkapi metode ini untuk menambahkan kontak ke dalam daftar kontak
        self.contacts.append(contact)

    def delete_contact(self, name):
        # Lengkapi metode ini untuk menghapus kontak berdasarkan nama
        # Anda bisa menggunakan list comprehension untuk menghapus kontak dengan nama tertentu
        self.contacts = [contact for contact in self.contacts if contact.get_name() != name]

    def search_contact(self, name):
        # Lengkapi metode ini untuk mencari kontak berdasarkan nama
        # Anda bisa menggunakan list comprehension untuk mencari kontak dengan nama tertentu
        found_contacts = [contact for contact in self.contacts if contact.get_name() == name]
        return found_contacts

    def display_contacts(self):
        # Lengkapi metode ini untuk menampilkan semua kontak dalam daftar
        for contact in self.contacts:
            print(contact)

# Membuat objek daftar kontak
contact_list = ContactList()

def main():
    print("\nMenu:")
    print("1. Tambah Kontak")
    print("2. Hapus Kontak")
    print("3. Cari Kontak")
    print("4. Tampilkan Semua Kontak")
    print("5. Keluar")

    choice = input("Pilih menu: ")

    if choice == "1":
        name = input("Masukkan nama kontak: ")
        phone = input("Masukkan nomor telepon kontak: ")
        contact = Contact(name, phone)
        contact_list.add_contact(contact)
        print(f"Kontak {name} telah ditambahkan.")
        back()

    elif choice == "2":
        name = input("Masukkan nama kontak yang akan dihapus: ")
        contact_list.delete_contact(name)
        print(f"Kontak {name} telah dihapus.")
        back()

    elif choice == "3":
        name = input("Masukkan nama kontak yang akan dicari: ")
        found_contacts = contact_list.search_contact(name)
        if found_contacts:
            print("Kontak ditemukan:")
            for contact in found_contacts:
                print(contact)
        else:
            print(f"Kontak dengan nama {name} tidak ditemukan.")
        back()

    elif choice == "4":
        print("Daftar Kontak:")
        contact_list.display_contacts()
        back()

    elif choice == "5":
        print("Terima kasih! Program selesai.")
        return False

    else:
        print("Pilihan tidak valid. Silakan pilih menu yang sesuai.")
def back():
    print("\nOperations Finished!")
    choice = input("Back to main menu(y/n)?: ")
    if choice == "y":
        main()
    else:
        return False

if __name__ == "__main__":
    main()