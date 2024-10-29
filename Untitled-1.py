class PersegiPanjang:  # membuat class untuk penghitungan persegi panjang
    def __init__(self, panjang, lebar):  # konstruktor untuk inisialisasi atribut panjang dan lebar
        self.panjang = panjang  # menyimpan nilai panjang sebagai atribut objek
        self.lebar = lebar      # menyimpan nilai lebar sebagai atribut objek
     
    def keliling(self):  # metode untuk menghitung keliling persegi panjang
        return 2 * (self.panjang + self.lebar)  # menggunakan rumus keliling: 2 * (panjang + lebar)
     
    def luas(self):  # metode untuk menghitung luas persegi panjang
        return self.panjang * self.lebar  # menggunakan rumus luas: panjang * lebar
     
    def __str__(self):  # metodes khusus untuk representasi string dari objek
        return f"Persegi Panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm"  
        # mengembalikan string yang mendeskripsikan objek

# fungsi utama untuk menjalankan program
def main():  
    try:  
        # meminta input panjang dan lebar dari pengguna
        panjang = float(input("Masukkan panjang persegi panjang (cm): "))  
        lebar = float(input("Masukkan lebar persegi panjang (cm): "))  
        
        # memeriksa apakah panjang dan lebar valid (lebih dari 0)
        if panjang <= 0 or lebar <= 0:  
            raise ValueError("Panjang dan lebar harus lebih dari 0.")  
        
        # membuat objek PersegiPanjang dengan panjang dan lebar yang diberikan
        persegi_panjang = PersegiPanjang(panjang, lebar)  
        
        # mencetak representasi string dari objek
        print(persegi_panjang)  
        
        # mencetak hasil keliling dan luas persegi panjang
        print("Keliling:", persegi_panjang.keliling(), "cm")  
        print("Luas:", persegi_panjang.luas(), "cm²")  
        
    except ValueError as e:  # menangani kesalahan jika input tidak valid
        print("Error:", e)  

# menjalankan fungsi main jika file ini dijalankan sebagai skrip utama
if __name__ == "__main__":  
    main()
