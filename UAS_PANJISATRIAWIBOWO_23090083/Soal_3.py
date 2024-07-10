class AntrianRestoran:
    def __init__(self):
        self.antrian = []

    def tambah_pesanan(self, pesanan):
        self.antrian.append(pesanan)
        print(f"Pesanan '{pesanan}' telah ditambahkan ke antrian.")

    def layani_pesanan(self):
        if len(self.antrian) > 0:
            pesanan = self.antrian.pop(0)
            print(f"Pesanan '{pesanan}' telah dilayani.")
            return pesanan
        else:
            print("Tidak ada pesanan dalam antrian untuk dilayani.")
            return None

    def tampilkan_antrian(self):
        if len(self.antrian) > 0:
            print("Antrian saat ini:", self.antrian)
        else:
            print("Antrian kosong.")

if __name__ == "__main__":
    antrian_restoran = AntrianRestoran()

    while True:
        print("\nSistem Antrian Pesanan Restoran")
        print("1. Tambah pesanan (Enqueue)")
        print("2. Layani pesanan (Dequeue)")
        print("3. Tampilkan antrian saat ini")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == '1':
            pesanan = input("Masukkan pesanan yang akan ditambahkan: ")
            antrian_restoran.tambah_pesanan(pesanan)
        elif pilihan == '2':
            antrian_restoran.layani_pesanan()
        elif pilihan == '3':
            antrian_restoran.tampilkan_antrian()
        elif pilihan == '4':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
