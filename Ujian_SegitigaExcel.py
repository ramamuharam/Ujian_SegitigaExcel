def segitigaExcel(kata):
    # Membentuk pola segitiga dengan elemen berupa karakter-karakter dari kata
    kata = kata.replace(' ', '')

    # Pola segitiga
    pola = list(map(lambda t : t * (t + 1)/ 2, range(len(kata))))
    pola = list(map(int, pola))
    
    # Membentuk segitiga dari kata jika kata memenuhi pola segitiga
    if len(kata) not in pola:
        # Kata tidak memenuhi pola segitiga
        print('Mohon maaf, jumlah karakter tidak memenuhi syarat membentuk pola.') 
    else: 
        # Membentuk segitiga dari kata
        import xlsxwriter
        book = xlsxwriter.Workbook('Ujian_SegitigaExcel.xlsx')
        sheet = book.add_worksheet('Sheet1')

        jumlahBaris = pola.index(len(kata))
        for i in range(jumlahBaris):
            col = 0
            for j in range(pola[i], pola[i + 1]):
                sheet.write(i, col, kata[j])
                col += 1
        book.close()
    

segitigaExcel('Purwadhika')
segitigaExcel('Purwadhika Startup and Coding School @BSD')
segitigaExcel('kode')
segitigaExcel('kode python')
segitigaExcel('Lintang')
