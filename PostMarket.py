import os
import time
import tkinter as TK
import sys

from selenium import webdriver

MARKET_DIR = "./Markets/"

def main():
    """
    Main function for PostMarket
    """
    # startGUI()
    # markets = getMarkets()
    saveLoginInfo("chrome")

def getBrowser(browser):
    if browser.upper() = "FIREFOX":
        return webdriver.Firefox(executable_path="./geckodriver.exe")
    # if browser.upper() = "CHROME":
    return webdriver.Chrome(executable_path="./chromedriver.exe")

def getMarkets(includeExt=False):
    """
    Gets all available markets to post to.

    Args: 

    Return: Ordered List of Strings
    """
    mList = os.listdir(MARKET_DIR)
    if includeExt == True:
        mList = list(map(lambda x: x.split(".")[0], mList))
    return(mList.sort())

def saveLoginInfo(browser):
    markets = getMarkets(includeExt=True)
    browser = getBrowser(browser)


# def startGUI():
#     top = TK.Tk()
#     interface = [
#         [
#             TK.Label(top, height=2, width=200, text="PostMarket Tool", bg = "light grey"),
#             "TOP"
#         ],
#         [

#         ],
#         [
#             TK.Button(top, bg="light blue" ),
#         ],

#     ]
#     for obj in interface:
#         obj[0].pack(obj[1])
#     top.mainloop()

if __name__ == "__main__":
    main()
