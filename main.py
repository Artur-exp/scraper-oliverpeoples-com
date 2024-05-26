# install packages
# pip install requests beautifulsoup4 lxml
import json
import os
import random
from time import sleep
import requests
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO, filename="error_log.log", filemode="a",
                    format="%(asctime)s %(levelname)s %(message)s")


def save_data_to_json2(filename_json, export_data):
    try:
        if not os.path.exists("export"):
            os.mkdir("export")

        new_data = []
        if os.path.isfile(filename_json):

            with open(filename_json, encoding='utf-8') as file:
                value_1 = json.load(file)
            for ii in value_1:
                new_data.append(ii)
            for iii in export_data:
                if iii not in new_data:
                    new_data.append(iii)
        else:
            for i in export_data:
                if i not in new_data:
                    new_data.append(i)

        with open(filename_json, "w", encoding='utf-8') as file2:
            json.dump(new_data, file2, indent=4, ensure_ascii=False)

    except Exception as exf:
        print(f"# Ошибка: {str(exf)}")
        logging.error("Exception", exc_info=True)


def search_title_json_file(title, filename_json):
    try:
        with open(filename_json, encoding='utf-8') as file:
            value_all = json.load(file)

        for i in value_all:
            title_search = i['name_prod_cat']
            if title == title_search:
                return title
    except:
        print(f"Файла {filename_json} несуществует")
        logging.error("Exception", exc_info=True)

# Category
# categoryId Sunglasses 3074457345616714176
# categoryId Eyeglasses 3074457345616714171
# categoryId Accessories 3074457345616714168
# categoryId Collaborations(collections) 3074457345616714169


def pars_prod():
    pages_str = 1
    post = 0
    filename_json = "export/data_oliverpeoples.json"

    try:
        data_category_id = ["3074457345616714176", "3074457345616714171",
                            "3074457345616714168", "3074457345616714169"]
        for category_id in data_category_id:
            print(f"category_id: {category_id}")

            for count in range(1, 2):
                headers = {
                    'accept': '*/*',
                    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6,pl;q=0.5,nl;q=0.4',
                    # 'cookie': 'aka-zp=; dtCookie=v_4_srv_-2D98_sn_RF765MLFS3U9GFUHOPP9Q8F8F9I5JVVL; rxVisitor=1714146169409CTIMG7SSLGGGLC3BANUBSFE3UEGGPL68; WC_X_LoggedUser=No; storeId=715839041; WC_GuestUserId_715839041=1886209946873722.5; JSESSIONID=0000O0bA7h2FRB_2oAaa4tDOCov:1etejcaha; WC_SESSION_ESTABLISHED=true; WC_PERSISTENT=UK5wbjt8BT0BAiKhMC5p18uxEsYko4naE7vgRKw5Ftc%3D%3B2024-04-26+17%3A42%3A51.302_1714146171292-922113_715839041_13411301%2C-1%2CUSD_715839041; WC_AUTHENTICATION_13411301=13411301%2CaVJ8XsDqzjJdRgzY32wzAeC1P1tPqCP2Ev4msbcq%2F5c%3D; WC_ACTIVEPOINTER=-1%2C715839041; WC_USERACTIVITY_13411301=13411301%2C715839041%2Cnull%2Cnull%2C1714146171304%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C308542901%2Cc0IbNL0oqUH7%2Fd1Mzh7zlIOMpsxnNEUjQqMLXS9ftpwGtin5DLRWDCJ4wN1bzZSmL5fR%2Fh%2FDAaSayVMijZVMiyQ5bHbEoNDt1WyKJo9i2Y0hooUuUgf5zSAstw6Xv6ZStAf%2FrBe3BbSHqua632iBIdotrqp9vAvOlzyVd4OogPGYLqJfwRePguUKNG3SWV%2FTg7xL2dH9PbKWNm2qkCk5j3YJpNeayYrvLz7ZUsBfkv%2FqadGlDu%2Ff7s2LL5TOqUq0naFiiJfWRa56S8lj%2FULUzg%3D%3D; ak_bmsc=D703D0DA08C16E3973C279C917C146EC~000000000000000000000000000000~YAAQtx0SAuSGyw6PAQAA0N0SGxcII28AH6hqPyJ42lvkHisCf6SR1cmoeAa5zjZS6GhYqZFVmmW6vN+HG6cvbbxJBZORLAfl/WXmDYqAE0DGTgEklXRTy7ksAn0XlTtYsPZZCbAywgZOKJwqGpR/N7lAtFd9kD0T5FbXk9fAH9JVuR6n6a2MzmwuGuPYdv8kXotaLRwj70lKG173ecKFTsLs+MizTRxmeaLa3HzE1K1f6tN5jUm0I+4eIPE6Vm7IwVMIeqJq2qU+cyPnVofJWg2y5m8pSgSiUdPw8QamFksd811qVN3mx90W7AF60rMey9rL2RLhR7jROXUoCsN0RV1LWm3jkuyc8DQ342ERPYCd4xboaD6q1SP7DPTVtwUSmTfhvpbEu0MZPu9eR3lXQALpctzNeRcwRoip9jtspkCaF8clWDF5R8Le19+64BFJR77FkZJLuM6q5Ac0hHOLDBQU56c=; tealium_data2track_Tags_AdobeAnalytics_TrafficSourceMid_ThisHit=upwork.com/; tealium_data_tags_adobeAnalytics_trafficSourceMid_thisSession=upwork.com/; utag_main_v_id=018f1b12e2f7001e65bb1e967e7805065002b05d00e50; utag_main__sn=1; utag_main_ses_id=1714146173691%3Bexp-session; tealium_data_session_timeStamp=1714146173727; TrafficSource_Override=1; utag_main__ss=0%3Bexp-session; utag_main_vapi_domain=oliverpeoples.com; s_fid=55B3084DD1ADA9B7-2D3D5F251A42070D; s_cc=true; utag_main_dc_visit=1; utag_main_dc_region=eu-central-1%3Bexp-session; _ga=GA1.2.1456480775.1714146175; _gid=GA1.2.974922203.1714146175; _tt_enable_cookie=1; _ttp=FOIMLYLvRHxq3KQlAl6dmILuBjc; _abck=E4C9BBEEA4766DFC26AF676BF8F70940~0~YAAQtx0SApKXyw6PAQAAkIsUGwtncRP7nmoJV7OTiNUj5v1wXCfjI0Mr2g1ovkzPjwN6np0dpd2qhpektJRPcoNs1+9Ee5jZJC6dltftKHhqFovc3lMrbY0rV+0P22/YU+YHgkDRgcTGSLSn69ZpJ0r/SqC7dDBHeIcP71HA3zX8VjVABcUuwF3Nh8C9i6lz4E57iwqmAY7LVfA/JtV+ksY+e/WUsXxLFYNpjXd6PcXUvxMcqDaxbcvH4r+0PU7v2PGljO123Tw9kk9bi/aSXzEaup0Ju/Iq+RlO30mVlYDORPyoD9NieF2bTjOhWYApdqD+6E1TzP16oi8HtJ6qwQtjx3JUxXTtF6XB04yTOqb6OlAjEf644EhCJUktuuZgz68gtLU3zs2YF3G4GVyX9svOZFWm7uhr2BPaE1WSFSYShepvTTJgEVol3DCsOj7LY56B1MT8k6lVtcBegnKM~-1~-1~-1; CompareItems_715839041=; isVMOpen=null; ModelName=null; aka-cc=UA; aka-ct=KIEV; rxvt=1714149850137|1714148050137; bm_sz=08F3193251CC587092239D9CD18615DA~YAAQtx0SAogLzQ6PAQAA3iUwGxdMoUCeW3S2NoV2CbKjdJT/Y7hrYk9DzNFbdTaRETiiARxGQOGpdKQudNWU7+D+G/SinJkxjVTtHjihUiLow5lI07mQHP1x0id6dBsEigbPxFAQEjg4NtTrLrbMyikLksawOD+zc/PFWYcktFluq4OJ5Ogp20cbmLjBoDrXcMirmNNkgWlLPFoI0nPSc6roeUYX8MaalCWTZul92WZh7V0WJ3UO4iLnAaYUPl7kSe+GNYwE8WmEIHroJwBTRRF+1xjvOKV9c2cmi2mPtQwq46lJWBuFDjwMWkFL6ElY3csJXzf+jBbJK0K30C3jFRqy8qhby0F7F2V7fM6hFvnRhfRvuF6J78iBMvFgnCNwf1gr3wYdQ5GI+TdoAMdjHLqavp4o0gOX7Prc4WJIWy8BooPcYBQthCxIuVlXE1/Z~4342321~3355957; dtPC=-98$548050101_220h1p-98$548091540_872h1vMPVPCLOKIVKTPPMUMFEPKEBMUFHDVUJA-0e0; utag_main__pn=5%3Bexp-session; TS01fce19a=010855713b3a3801f8acf0e90d2960e964b46302cbe6845fd9f25910dbb2f8caebebf630e87997e356a75527bdd9369668d7ff0cc025c40b33c7d116c7330749b746fb49609ba5311f341c3d173402a8e426131fe72e3ff4a7579ffc93e07726bf883e540edbd10c5e12e96de4b15eae268666a959a38d23ef4334d96d2ab61ebed0dea4399ddd99bdde114cd34316968742fdab63c1436808c7f4df255ab38aea57a35b903ba104ec02ce426c5b04ed0039da693ecb0c740e290be2be6d5e6ceea667327fb11e66d540902839ef9049a07ceaf278721c68168ee603d7335d931003c1efc2c272079e4e698c241d4ae81a29eb8484cc73e8c43afa86176f6d3808e03da316; utag_main_dc_event=5%3Bexp-session; bm_sv=A9CE6CF124259DCC921B6FCE64498D33~YAAQtx0SAgMNzQ6PAQAAIVkwGxeCX9f+FdaEWw/RWyz1bAQ507Q4DXzEWQeokusj8nH4FBA4PbM9ydKZSvJYK5sO18dtJZhH/9wpRlJVZty/TdWDteEXQqQmGwhG+y+mUTsQNjiazNLFUjbYtaYK0qhmsf6+Bnn/fET+oWdQ68H3cGlKj4Caj8hHgE/reHuW92z8KMtta3+Sc9YgNCzuKiWrj/zX/PTtDF1f+OvZ6JjPShK0/bzbA1dtwXrZHLbrFiLE1uO7Fu4=~1; utag_main__se=20%3Bexp-session; utag_main__st=1714149963731%3Bexp-session; tealium_data_action_lastAction=Sunglasses:Plp click [Loadmore Cta][LOADMORE]; tealium_data_action_lastEvent=click [Loadmore Cta][LOADMORE]',
                    'priority': 'u=1, i',
                    'referer': 'https://www.oliverpeoples.com/international/sunglasses',
                    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Linux"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
                    'x-requested-with': 'XMLHttpRequest',
                }

                params = {
                    'storeId': '715839041',
                    'catalogId': '3074457345616683368',
                    'responseFormat': 'json',
                    'langId': '-1',
                    'currency': 'USD',
                    'profileName': 'LUX_findProductsByCategory_group',
                    'searchSource': 'E',
                    'isForPLP': 'true',
                    'categoryId': category_id,
                    'pageNumber': f'{count}',
                    'pageSize': '18',
                }

                response = requests.get(
                    f'https://www.oliverpeoples.com/international/search/resources/store/715839041/productview/byCategory/{category_id}',
                    params=params,
                    # cookies=cookies,
                    headers=headers,
                ).json()

                count_goods = response['recordSetTotal']
                print(f"count_goods: {count_goods}")
                catalog = response['catalogEntryGroupView']

                for cat in catalog:
                    data_cat_products = []

                    name_prod_cat = cat
                    if name_prod_cat == search_title_json_file(name_prod_cat, filename_json):
                        print(f"# product: {name_prod_cat} существует")
                        continue

                    all_data_product = []
                    for inf_prod in catalog[name_prod_cat]:
                        name = inf_prod['name']

                        part_number = inf_prod['partNumber']
                        url_part_number = part_number.replace("__", "--")
                        # part_number = "0OV5413SU--14923R"
                        url_product = "https://www.oliverpeoples.com/international/" + url_part_number
                        print(f"{name}: {url_product}")
                        headers2 = {
                            'Referer': 'https://www.oliverpeoples.com/international/sunglasses',
                            'Upgrade-Insecure-Requests': '1',
                            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
                            'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': '"Linux"',
                        }

                        response2 = requests.get(url_product, headers=headers2)
                        soup = BeautifulSoup(response2.text, "lxml")

                        catalog_entry_details_temp = soup.find("div", id="catalogEntryDetails_temp")

                        data_prod_details = catalog_entry_details_temp.text
                        js2 = json.loads(data_prod_details)

                        try:
                            long_description = js2['longDescription']
                        except Exception as ex1:
                            print(f"[Error]: {ex1}")
                            long_description = ""

                        manufacturer = js2['manufacturer']
                        try:
                            mf_part_number_ntk = js2['mfPartNumber_ntk']
                        except Exception as ex2:
                            mf_part_number_ntk = ""
                            print(f"[Error]: {ex2}")

                        name_product = js2['name']

                        try:
                            price_usd = js2['price_USD']
                        except Exception as ex3:
                            price_usd = ""
                            print(f"[Error]: {ex3}")
                        short_description = js2['shortDescription']
                        unique_id = js2['uniqueID']

                        images = []
                        for img in js2['manifest']['payload']['images']:
                            path_img = img['path']
                            if path_img not in images:
                                images.append(path_img)
                        try:
                            channel = js2['manifest']['channel']
                        except Exception as ex6:
                            channel = ""
                            print(f"[Error]: {ex6}")
                        try:
                            gender = js2['manifest']['key']['gender']
                        except Exception as ex7:
                            gender = ""
                            print(f"[Error]: {ex7}")

                        try:
                            geo_fit = js2['manifest']['key']['geoFit']
                        except Exception as ex5:
                            geo_fit = ""
                            print(f"[Error]: {ex5}")

                        try:
                            product_type = js2['manifest']['key']['productType']
                        except Exception as ex4:
                            product_type = ""
                            print(f"[Error]: {ex4}")

                        try:
                            color_code = js2['manifest']['key']['mocoId']['colorCode']
                        except Exception as ex8:
                            color_code = ""
                            print(f"[Error]: {ex8}")
                        try:
                            model_code = js2['manifest']['key']['mocoId']['model']
                        except Exception as ex9:
                            model_code = ""
                            print(f"[Error]: {ex9}")

                        sku_data = []
                        for sku in js2['sKUs']:
                            mf_part_number_ntk_sku = sku['mfPartNumber_ntk']
                            sku_attributes = []
                            for sk_atr in sku['attributes']:
                                name_sk_atr = sk_atr['name']
                                value_sk_atr = sk_atr['values'][0]['value']
                                sku_attributes.append(
                                    {
                                        f"{name_sk_atr}": value_sk_atr
                                    }
                                )
                            sku_data.append(
                                {
                                    "mfPartNumber_ntk": mf_part_number_ntk_sku,
                                    "sku_attributes": sku_attributes
                                }
                            )
                        category = ""
                        attributes_prod = []
                        for atr in js2['attributes']:
                            name_atr = atr['name']
                            out_values = []
                            for ii in atr['values']:
                                value_atr = ii['value']
                                if name_atr == "PROD_HIERARCHY_1":
                                    category = value_atr
                                out_values.append(
                                    {
                                        "value": value_atr,
                                    }
                                )

                            attributes_prod.append(
                                {
                                    "name": name_atr,
                                    "values": out_values
                                }
                            )

                        all_data_product.append(
                            {
                                "partNumber": part_number,
                                "longDescription": long_description,
                                "manufacturer": manufacturer,
                                "mfPartNumber_ntk": mf_part_number_ntk,
                                "name": name_product,
                                "price_USD": price_usd,
                                "shortDescription": short_description,
                                "uniqueID": unique_id,
                                "images": images,
                                "channel": channel,
                                "gender": gender,
                                "geoFit": geo_fit,
                                "productType": product_type,
                                "colorCode": color_code,
                                "model_code": model_code,
                                "category": category,
                                "sku_products": sku_data,
                                "attributes": attributes_prod
                            }
                        )
                        # print(all_data_product)
                        sleep(1)
                    data_cat_products.append(
                        {
                            "name_prod_cat": name_prod_cat,
                            "all_data_product": all_data_product
                        }
                    )
                    save_data_to_json2(filename_json, data_cat_products)
                    print(f"# Products: {name_prod_cat} записаны...")

                    post += 1
                    print(f"# post: {post}")
                    sleep(random.randrange(2, 3))

                print(f"### pages_str: {pages_str}")
                pages_str += 1
                sleep(random.randrange(2, 4))

    except Exception as exf:
        print(f"# Ошибка: {str(exf)}")
        logging.error("Exception", exc_info=True)


pars_prod()

