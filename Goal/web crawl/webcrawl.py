from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# 設定 Chrome driver 的路徑
chromedriver_path = r'./chromedriver.exe'  # 請確保這個路徑是正確的

# 設定 Chrome options（如果需要）
options = Options()
options.add_argument('--disable-gpu')  # 禁用 GPU
options.add_argument('--no-sandbox')  # 這對某些系統有幫助
# 例如：options.add_argument('--headless')  # 如果你想要無頭模式
options.add_argument('--headless')  # 無頭模式


# 初始化 WebDriver，並指定 chromedriver 路徑
driver = webdriver.Chrome(service=Service(chromedriver_path), options=options)

# 打開目標網址
url = 'https://www.youtube.com/playlist?list=PL221E2BBF13BECF6C'  # 替換為實際的網址
driver.get(url)

# 爬取目標資料
video_elements = driver.find_elements('id', 'video-title')

# 遍歷所有找到的元素並輸出
for video_element in video_elements:
    print("影片標題:", video_element.text)

# 結束 WebDriver
driver.quit()
