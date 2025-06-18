import os, time
from selenium import webdriver
from selenium.webdriver.common.by import By


current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
print(current_dir)
print(file_path)
print(print(os.path.abspath(os.path.dirname(__file__))))
print(os.path.abspath(__file__))