# !/usr/bin/env python312
# -*- coding: utf-8 -*-
# __author__ = 'R. Sengupta | r_xn'
# __copyright__ = 'Copyright 2023, Ledgr | www.alphaLedgr.com'
# __credits__ = ['r_xn, s.sengupta,  adasgupta@gmail.com']
# __license__ = 'Ledgr | alphaledgr.com'
# __version__ = '01.02.04'
# __maintainer__ = 'r_xn@alphaledgr.com'
# __emails__ = 'r_xn@alphaledgr.com / response@alphaledgr.com'
# __status__ = 'In active development'

# from yaml.loader import SafeLoader
import os
import streamlit as st
import streamlit_authenticator as stauth

#from streamlit_option_menu import option_menu
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
direc = os.getcwd()

##################################################################
logofile = f'{direc}/pages/appdata/imgs/Ledgr_Logo_F2.png'
#links1 = ["https://www.investopedia.com/", "https://www.wsj.com/"]
#selected = option_menu(
#    menu_title=None,
#    options = ["News", "LedgrSite", "Media, Visuals & Posts"],

#    default_index=1,
#    orientation="Horizontal",
#    )

with st.sidebar:
    st.image(logofile)
    st.caption("Your unified Fintelligence Portal!")

# #######################################
# Icons and Links ###########################
ytube = f'{direc}/pages/appdata/imgs/ytube.svg'
fbook = f'{direc}/pages/appdata/imgs/fbook.svg'
insta = f'{direc}/pages/appdata/imgs/insta.svg'
linkedin = f'{direc}/pages/appdata/imgs/linkedin.svg'
ledgrblog = f'{direc}/pages/appdata/imgs/Ledgr_Logo_F2.png'

url_ytube = "https://www.youtube.com/@LedgrInc"
url_fbook = "https://www.facebook.com/share/1BnXaYvRzV/"
url_insta = 'https://www.instagram.com/alphaledgr/'
url_blog = 'https://www.alphaledgr.com/Blog'
url_linkedin = "https://www.linkedin.com/company/ledgrapp/"


        # Main Streamlit app starts here

    
st.markdown('''
            <div align="center">
            <h3>Learn how to get started on the platform!
            See below for details..</h3></div>''',
            unsafe_allow_html=True)
# st.write(f'{username} Welcome!')
st.image(f'{direc}/pages/appdata/imgs/The alphaLedgr Web3 Platform.png',
         width="content")
with st.container():
    a1, a2a, a2, a3 = st.columns([1, 1, 4, 1])
    with a1:
        st.image(f'{direc}/pages/appdata/imgs/LedgrBase.svg',
                 caption='Your Unified Wealth Dashboard')
    with a2a:
        st.write(" ")
    with a2:
        st.subheader("Part I: Ledgrbase")
        st.write("Map your existing asset holdings and portfolios.")
        st.write("Review and note their overall performance till date.")
        st.subheader("Part II: MarketBoard")
        st.write("Calculate Returns from SIPs, Explore ETFs and Mutual Funds.")
    with a3:
        st.image(f'{direc}/pages/appdata/imgs/MarketBoard.png',
                 caption='Market Profiles, Plots and Instruments')
st.write("-------------------------------------------------------------------")



st.write("-------------------------------------------------------------------")


with st.container():
    c1, c2a, c2 = st.columns([1, 1, 3])
    with c1:
        st.image(f'{direc}/pages/appdata/imgs/AnalyticsBox.png',
                 caption='Analytics and Information')
    with c2a:
        st.write(" ")
    with c2:
        st.subheader("AnalyticsBox")
        st.write("Analyze a Security In-Depth. Visualize Metrics & Indicators")
        st.write("Gather comprehensive knowhow on a selected Security.")
st.write("-------------------------------------------------------------------")
with st.container():
    d1, d2a, d2 = st.columns([3, 1, 1])
    with d1:
        st.subheader("InvestmentLab")
        st.write("Optimize Investment Allocations.")
        st.write("Generate Efficient Portfolios to Maximize Returns.")
        st.write("""Input assets and amount to proceed.""")
        st.write("""Select any from 5 Optimized portfolios presented.""")

    with d2a:
        st.write(" ")
    with d2:
        st.image(f'{direc}/pages/appdata/imgs/InvestmentLab.png',
            caption='Generate Optimal Portfolios',
            width='content')



#if not st.user.is_logged_in:
 #   login_screen()
#else:
 #   st.header(f"Welcome1, {st.user}!")
    




st.write("-------------------------------------------------------------------")


with st.container():
    
    column1, column2, column3, column4, column5 = st.columns([1, 1, 1, 2, 1])
    with column1:
        st.image(ytube, '[Ledgr\'s YouTube Channel](%s)' % url_ytube, width=60)
    with column2:
        st.image(fbook, '[Ledgr\'s FaceBook Page ](%s)' % url_fbook, width=60)
    with column3:
        st.image(linkedin,  '[Our LinkedIn Page ](%s)' % url_linkedin, width=60)
    with column4:
        st.write(" ")
        st.image(ledgrblog,  '[Ledgr\'s Blog ](%s)' % url_blog)
        st.write(" ")
    with column5:
        st.image(insta,  '[Ledgr\'s @ Instagram ](%s)' % url_insta, width=60)
# # ###################################################################
with st.container():
    f9, f10, f11 = st.columns([1, 5, 1])
    with f9:
        st.write(" ")
    with f10:
        st.caption(""":|2025 - 2026|All Rights Resrved © Ledgr Inc.|alphaLedgr:
                   """)
    with f11:
        st.write(" ")

