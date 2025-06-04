from flask import Flask, render_template
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from bs4 import BeautifulSoup 
import requests
from wordcloud import WordCloud, STOPWORDS
from collections import Counter
import re
from collections import defaultdict, Counter
from datetime import datetime, timedelta

#don't change this
matplotlib.use('Agg')
app = Flask(__name__) #do not change this

#insert the scrapping here
url_get = requests.get('https://www.detik.com/search/searchall?query=gempa')
soup = BeautifulSoup(url_get.content,"html.parser")

#find your right key here
table = soup.find('article', attrs={'class':'list-content__item'})
earthquake = soup.find_all('article', attrs={'class':'list-content__item'})

row_length = len(earthquake)

temp = [] #initiating a list 

for i in range(0, 12):
	article = earthquake[i]

	# Judul
	title_tag = article.find('h3', class_='media__title')
	title_link = title_tag.find('a') if title_tag else None
	title = title_link.get_text(strip=True) if title_link else 'Judul tidak ditemukan'

	# Berita
	summary_tag = article.find('div', class_='media__desc')
	summary = summary_tag.get_text(strip=True) if summary_tag else 'Ringkasan tidak ditemukan'

	# Tanggal
	date_tag = article.find('div', class_='media__date')
	date_span = date_tag.find('span') if date_tag else None
	date = date_span.get_text(strip=True) if date_span else 'Tanggal tidak ditemukan'

	temp.append((title, summary, date))

temp = temp[::-1]

#change into dataframe
gempa = pd.DataFrame(temp, columns= ('title', 'summary', 'date'))

#insert data wrangling here
from datetime import datetime, timedelta

bulan_map = {
    'Januari': 'Jan',
    'Februari': 'Feb',
    'Maret': 'Mar',
    'April': 'Apr',
    'Mei': 'May',
    'Juni': 'Jun',
    'Juli': 'Jul',
    'Agustus': 'Aug',
    'September': 'Sep',
    'Oktober': 'Oct',
    'November': 'Nov',
    'Desember': 'Dec'
}

def convert_relative_date(text):
    now = datetime.now()
    if "jam yang lalu" in text:
        hours = int(text.split()[0])
        return (now - timedelta(hours=hours)).date()
    elif "menit yang lalu" in text:
        minutes = int(text.split()[0])
        return (now - timedelta(minutes=minutes)).date()
    else:
        return pd.NaT

def translate_bulan(text):
    for indo, eng in bulan_map.items():
        if indo in text:
            return text.replace(indo, eng)
    return text

def parse_date(text):
    if "yang lalu" in text:
        return convert_relative_date(text)
    if "WIB" in text:
        text = text.replace("WIB", "").strip()
        text = translate_bulan(text)
        parts = text.split(", ")
        if len(parts) == 2:
            try:
                # Ubah ke format hanya tanggal (tanpa jam)
                return pd.to_datetime(parts[1], format="%d %b %Y %H:%M").date()
            except:
                try:
                    # Kalau tidak ada jam
                    return pd.to_datetime(parts[1], format="%d %b %Y").date()
                except:
                    return pd.NaT
    return pd.NaT

gempa['date_parsed'] = gempa['date'].apply(parse_date)

print(gempa[['date', 'date_parsed']].head(20))


#end of data wranggling 
import re
from collections import Counter
import matplotlib.pyplot as plt
from io import BytesIO
import base64

stopwords_id = {
    'm', 'terjadi', 'hingga', 'di', 'dan', 'dengan', 'dari', 'ke', 'yang', 'untuk',
    'pada', 'ada', 'tak', 'usai', 'saat', 'akibat', 'akan', 'tidak', 'itu', 'ini',
    'oleh', 'tersebut', 'dalam', 'bagi', 'karena', 'setelah', 'sebagai', 'wni',
    'video', 'dini', 'narapidana', 'lebih', 'kabur', 'km', 'skala', 'magnitudo',
    'update', 'korban', 'orang', 'warga', 'tewas', 'luka', 'besar', 'kondisi',
    'ratusan', 'puluhan', 'kabupaten', 'bagian', 'terasa', 'bernama', 'gempa', 'bumi'
}

@app.route("/")
def index(): 
  
    text = ' '.join(gempa['title'].fillna('') + ' ' + gempa['summary'].fillna('')).lower()
    tokens = re.findall(r'\b[a-z]{2,}\b', text)
    filtered_tokens = [word for word in tokens if word not in stopwords_id]

    top_words = Counter(filtered_tokens).most_common(10)
    words, freqs = zip(*top_words)

    card_data = f"{', '.join([w for w, _ in top_words])}"

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.barh(words[::-1], freqs[::-1], color='mediumseagreen')
    ax.set_title("Top 10 Words from Gempa News")
    ax.set_xlabel("Frequency")
    plt.tight_layout()

    figfile = BytesIO()
    plt.savefig(figfile, format='png', bbox_inches='tight')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    plot_result = str(figdata_png)[2:-1]

    # ✅ Return to HTML
    return render_template('index.html',
                        card_data=card_data, 
                        plot_result=plot_result)

# ✅ Flask entry point
if __name__ == "__main__": 
    app.run(debug=True)