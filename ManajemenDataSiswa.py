import datetime

class Student:
    def __init__(self, id, name, age, address):
        self.id = id
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return f"Id: {self.id}, Nama: {self.name}, Umur: {self.age}, Alamat: {self.address}"


class StudentList:
    def __init__(self):
        self.students = []

    def get_timestamp(self):
        return datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    def lihat_data_siswa(self):
        if self.students.__len__() < 1:
            print("Tidak ada data siswa yang ditemukan!")
            return False
        for student in self.students:
            print(student)

    def simpan_data_siswa(self):
        name = input("Nama: ")
        age = input("Umur: ")
        address = input("Alamat: ")

        id = self.get_timestamp()
        student = Student(id=id, name=name, age=age, address=address)
        self.students.append(student)

    def ubah_data_siswa(self, nama):
        for i, student in enumerate(self.students):
            if student.name == nama:
                print(f"Data siswa saat ini: {student}")

                # pengecekan data yang diupdate
                name_baru = input("Nama baru: ")
                if name_baru:
                    student.name = name_baru

                age_baru = input("Umur baru: ")
                if age_baru:
                    student.age = age_baru

                address_baru = input("Alamat baru: ")
                if address_baru:
                    student.address = address_baru

                print("Data siswa telah diubah!")
                break
        else:
            print("Data siswa tidak ditemukan!")

    def hapus_data_siswa(self, nama):
        for i, student in enumerate(self.students):
            if student.name == nama:
                self.students.pop(i)
                print("Data siswa telah dihapus!")
                break
        else:
            print("Data siswa tidak ditemukan!")


def main():
    student_list = StudentList()

    while True:
        print("===== Selamat Datang di Kumpulan Tool Management =====")
        print(
            """
        Silahkan Masukkan Angka Dari Option Berikut Untuk Melanjutkan:
        1. Lihat Data Siswa
        2. Masukkan Data Siswa
        3. Ubah Data Siswa
        4. Hapus Data Siswa
        5. Keluar
        """
        )
        pilihan = input("Pilihan: ")

        if pilihan == "1":
            student_list.lihat_data_siswa()
        elif pilihan == "2":
            student_list.simpan_data_siswa()
        elif pilihan == "3":
            name = input("Nama Siswa: ")
            student_list.ubah_data_siswa(name)
        elif pilihan == "4":
            name = input("Nama Siswa: ")
            student_list.hapus_data_siswa(name)
        elif pilihan == "5":
            break
        else:
            print("Mohon pilih pilihan yang tersedia!")


if __name__ == "__main__":
    main()
