from django.shortcuts import render
from bs4 import BeautifulSoup
from lxml import html
import requests
import re
import cssutils


def main(request):


    page = requests.get("https://grajpopolsku.pl/")
    soup = BeautifulSoup(page.content, "html.parser")

    # Przyklad 1
    all_h2_tags = []
    for element in soup.select("h2"):
        all_h2_tags.append(element.text)
    all_h2_tagslen=len(all_h2_tags)
    first_h2_text = soup.select("h2")[0].text

    # Przykład 2
    # Create top_items as empty list
    top_items = []

    # Extract and store in top_items according to instructions on the left
    products = soup.select("div.post-list-box")
    for elem in products:
        title = elem.select("h2")[0].text
        content_label = elem.select("div.post-content")[0].text
        # strip() usuwa zbędne spacje
        info = {"title": title.strip(), "content": content_label.strip()}
        top_items.append(info)



       #Przykład 3
    # Create top_items as empty list

    page2 = requests.get("https://grajpopolsku.pl/downloads/psp/")
    soup2 = BeautifulSoup(page2.content, "html.parser")

    image_data = []

    # Extract and store in top_items according to instructions on the left
    images = soup2.select("div.post-list-box")
    print("Liczba obrazków =", len(images))
    for image in images:

        src = cssutils.parseStyle(image.select("div.dwn_bg")[0].get('style'))['background'].replace('url(', '').replace(')', '')
        
        title = image.select("h2.title")[0].text
        image_data.append({"src": src,"title": title}) #({"src": src}) "alt": alt})







    # Przykład 4

    page3 = requests.get("https://grajpopolsku.pl/downloads/page/5/")
    soup3 = BeautifulSoup(page3.content, "html.parser")
    

    all_products = []

    # Extract and store in top_items according to instructions on the left
    products = soup3.select('div.post-list-box')

    for product in products:
        name = product.select('h2 > a')[0].text.strip()
        platform = product.select('div.thumb-cats > a')[1].text.strip()
        image = cssutils.parseStyle(product.select("div.dwn_bg")[0].get('style'))['background'].replace('url(', '').replace(')', '')

        all_products.append({"name": name, "platform": platform,"image": image})  




    # xPath
    url = 'https://grajpopolsku.pl/'    
    path = '/html/body/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div[7]/div/div[2]/div[1]'
    response = requests.get(url)
    source = html.fromstring(response.content)    
    tree = source.xpath(path)
    lxmlPrzyklad1 = tree[0].text_content()
    
    # klasy   
    url = 'https://grajpopolsku.pl/'  
    path = '//*[@class="title-span"]'
    response = requests.get(url)    
    source = html.fromstring(response.content)    
    tree = source.xpath(path)
    lxmlPrzyklad2 = tree[0].text_content()









    # Scraping

    if request.method == "POST":
        all_elements = []

        page4 = request.POST.get('web_link', None)
        element = request.POST.get('element', None)
        source=requests.get(page4).text 
            
        
        soup4 = BeautifulSoup(source, "html.parser")

        items = soup4.find_all(element)
        amount = len(items)    

        index = 1 

        for i in items:
            # Szukanie klasy
            find_class = i.get('class')
            if find_class is None:
                find_class = "Brak"   
            
            # Szukanie id
            find_id = i.get('id')
            find_id = find_id.strip() if find_id is not None else "Brak"

            # Szukanie linków
            find_href = i.get('href')
            find_href = find_href.strip() if find_href is not None else "Brak"

            # Szukanie tekstu
            get_text = i.text
            get_text = get_text.strip() if get_text is not None else "Brak"

            # Szukanie źródeł
            find_src = i.get('src')            
            if find_src is None:
                find_src = "Brak"
            # Szukanie atrybutu
            find_alt = i.get('alt')
            find_alt = find_alt.strip() if find_alt is not None else "Brak"

            all_elements.append({"find_id": find_id, "find_class": find_class, "find_href": find_href, "get_text": get_text, 'find_alt':find_alt, 'find_src': find_src, 'index': index})
            index += 1
     
        return render(request,'main.html',{'top_items':top_items,'first_h2_text':first_h2_text,'all_h2_tagslen':all_h2_tagslen,'image_data':image_data,'all_products':all_products, 'lxml1': lxmlPrzyklad1,'lxml2': lxmlPrzyklad2, 'all_elements':all_elements , 'amount': amount, 'page4': page4, 'element':element})


    return render(request,'main.html',{'top_items':top_items,'first_h2_text':first_h2_text,'all_h2_tagslen':all_h2_tagslen,'image_data':image_data,'all_products':all_products, 'lxml1': lxmlPrzyklad1,'lxml2': lxmlPrzyklad2})
