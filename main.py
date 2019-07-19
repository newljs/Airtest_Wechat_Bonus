# -*- encoding=utf8 -*-
__author__ = "ljs"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from threading import Thread
import time


poco = AndroidUiautomationPoco(action_interval=0.3, use_airtest_input=True, screenshot_each_action=False)

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
            "Android://127.0.0.1:5037/192.168.88.66:7555",
    ])



def regular():
    i=0
    while True:
        time.sleep(0.01)
        if poco(text="[微信红包]恭喜发财，大吉大利"):
            poco(text="[微信红包]恭喜发财，大吉大利").click()
            clickhongbao()
            i=i+1
            print(i)
        elif poco(textMatches="^.*微信红包.*$"):
            poco(textMatches="^.*微信红包.*$").click()
            clickhongbao()
            i=i+1
            print(i)
        # poco().swipe([0.0, 0.0682]) #未开启充电防休眠模式时启用，自动点击屏幕，防止休眠


def clickhongbao():
    if poco("com.tencent.mm:id/as_"):
        poco("com.tencent.mm:id/as_")[len(poco("com.tencent.mm:id/as_"))-1].click()
        if poco("com.tencent.mm:id/d4h"):
            poco("com.tencent.mm:id/d4h").click()
        elif poco("com.tencent.mm:id/d4j"):
            poco("com.tencent.mm:id/d4j").click()
            time.sleep(1)
#         poco("com.tencent.mm:id/d4h").click()
#         poco("com.tencent.mm:id/lb").click()
#         poco("com.tencent.mm:id/d4h").click()
        
        keyevent("BACK")
#     poco("com.tencent.mm:id/l3").click()
    time.sleep(0.1)
    keyevent("BACK")

if __name__ == "__main__":
    regular()


