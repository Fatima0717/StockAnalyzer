from bs4 import BeautifulSoup

def parse_shikiho_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    data = {}

    # Example: Extracting growth and profit margin
    growth_element = soup.find('div', class_='growth')
    profit_margin_element = soup.find('div', class_='profit_margin')

    if growth_element:
        data['growth'] = int(growth_element.text.strip('%'))
    if profit_margin_element:
        data['profit_margin'] = float(profit_margin_element.text.strip('%'))

    return data