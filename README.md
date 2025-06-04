# Web-Scrapping using Beautifulsoup

Projek ini dikembangkan sebagai salah satu capstone project dari Algoritma Academy dalam spesialisasi _Data Analytics_. Deliverables yang diharapkan dari projek ini adalah melakukan _web scraping_ sederhana untuk mendapatkan informasi. Kita juga akan menggunakan dashboard sederhana Flask untuk menampilkan hasil _scrap_ dan visualisasi.

Untuk panduan langkah demi langkah, Anda dapat membuka repositori Git berikut [di sini](https://github.com/t3981-h/Webscrapping-with-BeautifulSoup "Web Scraping with Beautiful Soup"). *⚠️ Disclaimer: link di atas akan mengarah ke sebuah direktori GitHub lain yang sama dengan direktori pada [video panduan capstone web scraping](https://drive.google.com/drive/u/4/folders/1GyRYIUgaREwcz5FT76UDNyobLSrnERgw). Namun, kasus yang ada pada direktori GitHub tersebut hanya merupakan contoh agar Bapak/Ibu dapat memahami workflow web scraping, bukan kasus yang akan Bapak/Ibu kerjakan dalam capstone ini. Kasus yang bisa Bapak/Ibu pilih dan kerjakan dapat dilihat pada bagian di bawah ini.*

## Project Requirements

**Relevant Topics**:
- Python for Data Analysts (P4DA)
- Exploratory Data Analysis (EDA)
- Data Wrangling and Visualization (DWV)

**New Exploratory Topics**:
- Python for-loop
- Webscrapping with `BeautifulSoup`
- Visualization with `matplotlib`
- Building dashboard using `flask`

**Workflow**:
1. Virtual environment preparation
2. Scrap data from website using `BeautifulSoup`
3. Creating dataframe
4. Data preprocessing
   - Data Cleansing
   - Data Wrangling
5. Data visualization
6. Building `flask` Dashboard

## Dependencies

- beautifulsoup4==4.12.3
- Flask==3.0.2
- Jinja2==3.1.3
- Werkzeug==3.0.1
- pandas==2.2.2

Atau Anda dapat menginstal library tersebut menggunakan `requirements.txt` dengan menjalankan perintah berikut:

```python
pip install -r requirements.txt
```

## Rubics

- Environment preparation (2 points)
- Finding the right key to scrap the data & Extracting the right information (5 points)
- Creating data frame, Data wrangling, and Visualization (5 points)
- Creating a tidy python notebook as a report (2 points)
- Implement it on flask dashboard (2 points)

## What You Need to Do

- Unduh atau klon repositori ini. File repositori ini adalah kerangka kerja untuk melakukan _scraping_ hingga membuat visualisasi plot yang akan digunakan dalam dashboard sederhana menggunakan Flask.
- Coba lakukan _scraping_ dari situs web sesuai dengan kasus yang ingin Anda pilih (pilihan kasus terdapat di bawah) menggunakan `Beautiful Soup` dalam notebook Anda terlebih dahulu.
- Buka notebook template pada capstone ini dan isi sesuai dengan petunjuk yang ada. Pastikan Anda memberikan analisis yang dibutuhkan dalam notebook tersebut.
- Isilah bagian yang masih kosong baik itu pada `Notebook Skeleton Guide Capstone Beautiful Soup.ipynb`, `app.py`, maupun pada `templates/index.html`.
- Pertama, isi fungsi `get` dengan memasukkan tautan web yang akan Anda _scrap_.

```python
url_get = requests.get(___) #insert url here
```

- Isi fungsi `scrap` dengan proses scraping yang sudah Anda lakukan di notebook.

```python
table = soup.find(___)
tr = table.find_all(___)
```

> Pada bagian diatas, untuk melakukan _scrap_, kata kunci `table` dan `tr` dapat disesuaikan kembali berdasarkan kasus yang Anda ambil.

- Isi bagian ini untuk menyimpan hasil _scrap_ yang Anda buat menjadi sebuah _dataframe_.

```python
df = pd.DataFrame(name of your tupple, columns = (name of the columns))
```

- Terakhir, lakukan _cleaning dataframe_ untuk visualisasi yang sesuai dengan kasus yang Anda ambil.

- Mengacu pada poin rubrik terakhir, selain melakukan _scrap_ pada situs web dan membuat visualisasi dalam `notebook.ipynb`, Anda harus mendemonstrasikan bagaimana cara menampilkan plot tersebut dalam aplikasi Flask dan menampilkannya pada templates/halaman HTML. Perhatikan bagian `app.py`. Isi bagian yang kosong pada `app.py` dengan menyesuaikan kode yang sudah dibuat pada `notebook.ipynb`.

- Anda juga dapat bermain dengan _UI_ (antarmuka pengguna) pada `index.html`, di mana Anda dapat mengikuti komentar yang ada untuk mengetahui bagian mana yang dapat diubah.

### The Final Mission

Pada **capstone** kali ini, Anda dapat memilih salah satu dari kasus berikut untuk dikerjakan:

1. [Case Data kurs US Dollar ke rupiah](https://www.exchange-rates.org/exchange-rate-history/usd-idr)

   - Dari halaman tersebut carilah `tanggal`, dan `harga harian`
   - Bualah plot pergerakan kurs USD

2. [Case IMDB Box Office Mojo](https://www.boxofficemojo.com/year/world/)

   - Dari Halaman tersebut carilah kolom `Rank`, `Release Group`, `Worldwide`, `Domestic`, dan `Foreign`
   - Note: kolom `worldwide` merupakan total dari kolom `domestic` dan `foreign`, analisa dan plot bisa disesuaikan.
   - Buatlah plot dari 10 film paling populer di tahun 2024

3. [Case Berita Detik.com tentang Gempa](https://www.detik.com/search/searchall?query=gempa)
   - Dari halaman tersebut carilah `judul`, `berita` , dan `tanggal`
   - Bualah word cloud dari judul. hint: gunakan bantuan `.str.cat()`

Happy Learning!
