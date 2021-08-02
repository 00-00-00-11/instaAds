import requests

def send(users):
    url = "https://i.instagram.com/api/v1/direct_v2/create_group_thread/"

    payload='recipient_users=["16817136641","2109565415"]'
    headers = {
        'cookie': 'mid=YOvhfwAEAAH1u2rPBKyUESPbPqjZ; ig_did=37685605-DCA7-4403-973D-61C307DC3746; csrftoken=wDwQ8cmHLkDe7iG6CjJgHJZL132eDmo7; ds_user_id=11949406014; sessionid=11949406014%3AvKv1OkhsPxcNUm%3A18; shbid="5458\\05411949406014\\0541659443397:01f78543a69d079d3e542ede4c362075d4fba306d69ff2cbd1850c11658352d6b86144ba"; shbts="1627907397\\05411949406014\\0541659443397:01f7e61225c558028170da80e87aa85e86ebfa35cfd5e1352729c15498f3691438dcdab8"; rur="ASH\\05411949406014\\0541659463431:01f70a7ab16cf218b78e9ca8e67df9570d9ff807340bf4647b5f15dc3ed4f1b4abe6c480"; csrftoken=wDwQ8cmHLkDe7iG6CjJgHJZL132eDmo7; ds_user_id=11949406014',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 OPR/77.0.4054.277',
        'x-asbd-id': '437806',
        'x-csrftoken': 'wDwQ8cmHLkDe7iG6CjJgHJZL132eDmo7',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR0k9m2HW_nPQhYTXtxXPmFsBiV8xAZ_1IfrhbxRguU3UDMV',
        'x-instagram-ajax': '8c4f274ffe7faccept: */*',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'mid=YOvhfwAEAAH1u2rPBKyUESPbPqjZ; ig_did=37685605-DCA7-4403-973D-61C307DC3746; csrftoken=wDwQ8cmHLkDe7iG6CjJgHJZL132eDmo7; ds_user_id=11949406014; sessionid=11949406014%3AvKv1OkhsPxcNUm%3A18; shbid="5458\\05411949406014\\0541659443397:01f78543a69d079d3e542ede4c362075d4fba306d69ff2cbd1850c11658352d6b86144ba"; shbts="1627907397\\05411949406014\\0541659443397:01f7e61225c558028170da80e87aa85e86ebfa35cfd5e1352729c15498f3691438dcdab8"; rur="ASH\\05411949406014\\0541659463431:01f70a7ab16cf218b78e9ca8e67df9570d9ff807340bf4647b5f15dc3ed4f1b4abe6c480"',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-ch-ua': '"Opera";v="77", "Chromium";v="91", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 OPR/77.0.4054.277',
        'x-asbd-id': '437806',
        'x-csrftoken': 'wDwQ8cmHLkDe7iG6CjJgHJZL132eDmo7',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR0k9m2HW_nPQhYTXtxXPmFsBiV8xAZ_1IfrhbxRguU3UDMV',
        'x-instagram-ajax': '8c4f274ffe7f'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)