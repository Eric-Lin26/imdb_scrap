import requests
from bs4 import BeautifulSoup

def get_movie_data(movie_name):
    query_data = {
        'q': movie_name,
        'ref_': 'nv_sr_sm'
    }
    url = 'https://www.imdb.com/find'
    rep = requests.get(url, params=query_data)
    soup = BeautifulSoup(rep.text, 'html.parser')

    result_hrefs = [e.get("href") for e in soup.select(".result_text > a")]
    href = 'https://www.imdb.com' + result_hrefs[0]
    mrep = requests.get(href)
    msoup = BeautifulSoup(mrep.text, 'html.parser')

    Title = msoup.select('h1')
    movieTitle = [t.text for t in Title]
    Poster = msoup.select('.poster img')[0]
    moviePoster = Poster.get('src') # 用.get取得src="這裡的網址"
    rating = msoup.select('strong span')
    movieRating = [r.text for r in rating]
    genre = msoup.select('.subtext a')
    movieGenre = [d.text for d in genre]
    movieGenre.pop()
    cast = msoup.select('.primary_photo+ td a')
    movieCast = [a.text.strip('\n') for a in cast]

    movie_data = {
        '電影名稱：': movieTitle,
        '電影海報：': moviePoster,
        '電影評分：': movieRating,
        '電影類型：': movieGenre,
        '演員：': movieCast
    }
    return movie_data

movie_key = input('請輸入電影名稱：')
print(get_movie_data(movie_key))