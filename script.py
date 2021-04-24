#!/usr/bin/env python2

"""
Be a Best CODER Okay

"""
# Code_Start
import os
os.system("clear")

print("\033[1m\033[33m]\033[32m───────────────────────────────────────────\033[33m[")

print("            \033[7m\033[1m\033[36m\033[4m[Coded \033[38;5;209mBy\033[33m Mandeep]\033[0m")

print()

print("     \033[1m\033[36mTool Name       \033[32m: \033[33mWater_Notifier ")
print("     \033[1m\033[36mAuthor_Name     \033[32m: \033[33mMandeep Malakar ")
print("     \033[1m\033[36mYouTube_Channel \033[32m: \033[33mMathematical Program")
print("     \033[1m\033[36mCountry         \033[32m: \033[33mIndia")
print("     \033[1m\033[36mState           \033[32m: \033[33mJharkhand")
print()
print("\033[1m\033[32m]\033[32m───────────────────────────────────────────\033[33m[")

print()
print("          \033[1m\033[31m>───LOADING─────<")
print()
print("         \033[1m\033[33mTool Is Running in \n                  The Background")
os.system("sleep 1800") 
os.system("termux-notification -t Please_Drink_Water")
os.system("termux-notification --sound ")
os.system("termux-dialog -i Please_Drink_Water_Sir__[Yes/No] -t Water_Notifier_By_Mandeep")

os.system("python script.py &")

