from bs4 import BeautifulSoup


def extract_colors(file_path):
    with open(file_path, "r") as file:
        soup = BeautifulSoup(file, "html.parser")

    table = soup.find('table')
    rows = table.find_all('tr')

    colors = []
    for row in rows[1:]:
        cols = row.find_all('td')
        colors.extend(cols[1].text.strip().split(', '))

    return colors
