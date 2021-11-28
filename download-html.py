#
#
#
#
import requests,os
dawnload=requests
website_path_google = input('Website: ')
file_website_html_css_path_shak=input(' name.File: ')
os.system('termux-setup-storage')
web = dawnload.get(website_path_google).text
css_html_website_dawnload = open('/sdcard/'+file_website_html_css_path_shak+'.html','w')
css_html_website_dawnload.write(web)
css_html_website_dawnload.close()