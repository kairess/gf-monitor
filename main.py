import scapy.layers.l2
from pushover import Client
from dotenv import load_dotenv
load_dotenv()
import time, os

net = '192.168.35.1/24' # ip address of your wifi router
gf_mac = 'e0:89:7e:e4:e9:13' # mac address of your gf's phone
token = os.getenv('PUSHOVER_TOKEN')
user_key = os.getenv('PUSHOVER_USER_KEY')

client = Client(user_key, api_token=token)

while True:
    ans, noans = scapy.layers.l2.arping(net, timeout=1, verbose=False)

    for sent, received in ans.res:
        ip = received.psrc
        mac = received.hwsrc

        # print('%s\t%s' % (ip, mac))

        if mac == gf_mac:
            print('여자친구 옴!')
            client.send_message('경고!', title='여자친구 옴! 빨리 끄삼!')

    time.sleep(0.2)
