import requests

def send(users):
    url = "https://i.instagram.com/api/v1/direct_v2/create_group_thread/"

    payload='recipient_users=["16817136641","2109565415"]'
    headers = {
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'mid=YOvhfwAEAAH1u2rPBKyUESPbPqjZ; ig_did=37685605-DCA7-4403-973D-61C307DC3746; ds_user_id=11949406014; shbid="5458\05411949406014\0541659443397:01f78543a69d079d3e542ede4c362075d4fba306d69ff2cbd1850c11658352d6b86144ba"; shbts="1627907397\05411949406014\0541659443397:01f7e61225c558028170da80e87aa85e86ebfa35cfd5e1352729c15498f3691438dcdab8"; csrftoken=Mv1vPsfWA6yIvLo7kIwPsRzaAGOetoe9; sessionid=11949406014%3AH31Z0VAytoBAW3%3A18; rur="ASH\05411949406014\0541659463883:01f7937d630a2b42ab11a82c235513d2dd24fa3d5ba1c53536a6bff90fdbfbbad63b9719"',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 OPR/77.0.4054.277',
        'x-asbd-id': '437806',
        'x-csrftoken': 'Mv1vPsfWA6yIvLo7kIwPsRzaAGOetoe9',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR0k9m2HW_nPQhYTXtxXPmFsBiV8xAZ_1IfrhbxRguU3UDMV',
        'x-instagram-ajax': '8c4f274ffe7f'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)