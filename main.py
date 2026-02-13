import time
import random

def cetak_dramatis(teks):
    """Menampilkan teks dengan jeda 0.5 detik untuk efek dramatis"""
    print(teks)
    time.sleep(0.5)

def tampilkan_pedang():
    """Menampilkan ASCII art pedang (kemenangan)"""
    pedang = """
    ⚔️  SELAMAT KAMU MENANG! ⚔️
    
         /|\\
        / | \\
       /  |  \\
      /   |   \\
      |   |   |
      |   |   |
      |   🗡   |
       \\  |  /
        \\ | /
         \\|/
          |
      """
    print(pedang)

def tampilkan_tengkorak():
    """Menampilkan ASCII art tengkorak (kekalahan)"""
    tengkorak = """
    💀 KAMU KALAH! 💀
    
        .-""""""-.
       /        \\
      |  o    o  |
      |     >    |
      |  \\____/  |
       \\        /
        '-.____.-'
         |      |
         |  __  |
        /| |  | |\\
       / | |__| | \\
    """
    print(tengkorak)

def game_utama():
    cetak_dramatis("--- MEMULAI PETUALANGAN DIGITAL ---")
    nama = input("Siapa namamu? ")
    nyawa = 100
    
    cetak_dramatis(f"\nSelamat datang, {nama}!")
    cetak_dramatis(f"Nyawa: ❤️ {nyawa} HP")
    cetak_dramatis("Kamu menemukan diri di persimpangan jalan misterius...")
    cetak_dramatis("\nDua jalur terbentang di hadapanmu:")
    cetak_dramatis("1. Lembah Coding - Sebuah lembah yang penuh dengan kode-kode ajaib")
    cetak_dramatis("2. Gunung Bug - Sebuah gunung tinggi yang dipenuhi bug-bug berbahaya")
    
    pilihan = input("\nKe mana kamu ingin pergi? (1 atau 2): ")
    
    if pilihan == "1":
        cetak_dramatis(f"\n✨ {nama} memilih Lembah Coding ✨")
        cetak_dramatis("Kamu memasuki lembah yang bercahaya dengan banyak buku-buku coding...")
        cetak_dramatis("Suara-suara aneh terdengar dari kejauhan...")
        
        # Elemen keberuntungan di Lembah Coding
        keberuntungan = random.randint(1, 100)
        if keberuntungan > 60:
            cetak_dramatis("\n🍀 Kamu beruntung! Menemukan buku kode langka...")
            cetak_dramatis("Nyawa bertambah! ❤️ +15 HP")
            nyawa += 15
        elif keberuntungan > 30:
            cetak_dramatis("\n😐 Kamu menemukan buku biasa saja...")
            cetak_dramatis("Tidak ada yang istimewa di sini.")
        else:
            cetak_dramatis("\n😱 Mendadak gulungan kode menyerang!")
            cetak_dramatis("Kamu terluka saat menghindar!")
            nyawa -= 15
            
    elif pilihan == "2":
        cetak_dramatis(f"\n⛏️ {nama} memilih Gunung Bug ⛏️")
        cetak_dramatis("Kamu mulai mendaki gunung yang tinggi dan berbatu...")
        cetak_dramatis("Udara semakin dingin seiring semakin tingginya pendakianmu...")
        
        # Elemen keberuntungan di Gunung Bug
        keberuntungan = random.randint(1, 100)
        if keberuntungan > 50:
            cetak_dramatis("\n🍀 Nasib baik! Kamu menemukan jalan pintas yang aman...")
            cetak_dramatis("Kamu lolos dari perangkap bug!")
        elif keberuntungan > 25:
            cetak_dramatis("\n⚔️ Kamu bertemu dengan bug tier menengah...")
            cetak_dramatis("Pertarungan sengit! Nyawa berkurang.")
            nyawa -= 10
        else:
            cetak_dramatis("\n👹 BUG BESAR MUNCUL! Ini sangat berbahaya!")
            cetak_dramatis("Kamu terjatuh dan terluka parah!")
            nyawa -= 25
            
    else:
        cetak_dramatis("\n⚠️ Pilihan tidak valid! Kamu terjatuh di persimpangan...")
        nyawa -= 20
        cetak_dramatis(f"Nyawa berkurang! ❤️ Nyawa saat ini: {nyawa} HP")
    
    cetak_dramatis(f"\n📊 Status Nyawa Akhir: {nyawa} HP")
    
    # Tampilkan ASCII art berdasarkan status akhir
    time.sleep(1)
    if nyawa > 0:
        tampilkan_pedang()
        cetak_dramatis(f"\n🏆 {nama} selamat sampai tujuan dengan {nyawa} HP sisa!")
    else:
        tampilkan_tengkorak()
        cetak_dramatis(f"\n💀 {nama} tidak berhasil selamat dari petualangan ini...")
    
if __name__ == "__main__":
    main_lagi = True
    while main_lagi:
        game_utama()
        
        # Tanyakan apakah pemain ingin bermain lagi
        cetak_dramatis("\n" + "="*50)
        tanya = input("Main lagi? (y/n): ").lower()
        
        if tanya == "y":
            cetak_dramatis("\n✨ Petualangan baru dimulai! ✨\n")
            time.sleep(1)
        else:
            cetak_dramatis("\n👋 Terima kasih telah bermain Game Mystery Adventure Bot!")
            cetak_dramatis("Sampai jumpa lagi, petualang... 🌙")
            main_lagi = False