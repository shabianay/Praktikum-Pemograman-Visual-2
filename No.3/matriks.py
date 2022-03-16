import numpy as np

class matriks:
    def __init__(self):
        self.a = np.ones((3,3))
        self.a[0][0] = 1
        self.a[0][1] = 2
        self.a[0][2] = 3
        self.a[1][0] = 2
        self.a[1][1] = 3
        self.a[1][2] = 6
        self.a[2][0] = 4
        self.a[2][1] = 9
        self.a[2][2] = 4
        
        self.b = np.ones((3,3))
        self.b[0][0] = 3
        self.b[0][1] = 4
        self.b[0][2] = 7
        self.b[1][0] = 5
        self.b[1][1] = 2
        self.b[1][2] = 8
        self.b[2][0] = 8
        self.b[2][1] = 4
        self.b[2][2] = 5

#       self.a = ([1,2,3],[2,3,6],[4,9,4])
#       self.b = ([3,4,7],[5,2,8],[8,4,5])

    def perkalian(self):
        self.res = np.dot(self.a, self.b)
        print ("Hasil Kali = ")
        print (self.res)

    def penjumlahan(self):
        self.res = self.a + self.b
        print ("Hasil Penjumlahan = ")
        print (self.res)

    def pengurangan(self):
        self.res = self.a - self.b
        print ("Hasil Pengurangan = ")
        print (self.res)

    def determinan(self):
        self.det_a = np.linalg.det(self.a)
        self.det_b = np.linalg.det(self.b)
        self.hasil_a = round(self.det_a)
        self.hasil_b = round(self.det_b)
        print ("Determinan Matriks A : ")
        print (self.hasil_a)
        print ("Determinan Matriks B : ")
        print (self.hasil_b)

    def transpose(self):
        self.t_a = np.transpose(self.a)
        self.t_b = np.transpose(self.b)
        print ("Transpose Matriks A : ")
        print (self.t_a)
        print ("Transpose Matriks B : ")
        print (self.t_b)

    def show(self):
        print ("Matriks A : ")
        print (self.a)
        print ("Matriks B : ")
        print (self.b)
        menu = """
# Program Menghitung Matriks #
1. Penjumlahan
2. Pengurangan
3. Perkalian
4. Determinan
5. Transpose
6. Keluar
Silahkan Pilih Menu (1 - 6): """
        status = 0
        while not status:
            pilihan = input(menu)
            print (" ")
            print ("Anda memilih menu ke-", pilihan)
            print ("")

            if pilihan not in '123456':
                print ("Anda salah memasukkan angka!")
                print ("Masukkan 1 - 6")
                print (" ")

            else:
                if pilihan == '6':
                    status = 1
                    print ("~~Terimakasih~~")
                elif pilihan == '1':
                    self.penjumlahan()
                elif pilihan == '2':
                    self.pengurangan()
                elif pilihan == '3':
                    self.perkalian()
                elif pilihan == '4':
                    self.determinan()
                elif pilihan == '5':
                    self.transpose()

matriks = matriks()
matriks.show()
