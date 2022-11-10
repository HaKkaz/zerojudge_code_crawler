# Zerojudge Code Crawler
> HaKkaz Lin, 2022/11/10
> 從高中就一直想把自己 zerojudge 的 code 爬下來，加上有在接家教，每次都要找很麻煩，所以乾脆把它爬一爬。
## 工具介紹
此工具可以幫助你把自己的 Zerojudge 程式碼抓下來，目前僅能爬取 `.py` 及 `.cpp` 程式碼。

步驟如下：
1. 在指定 port 的瀏覽器登入好 Zerojudge 帳號，以解決登入的 capche 問題。
2. 使用 selenium 的 webdriver 在該瀏覽器進行爬蟲。
3. 使用 beautifulsoup 爬取網頁資料。
4. 用 python 輸出成 `.cpp`/`.py` 檔案。

這是個心血來潮開發的小工具，有任何問題都可以聯絡我＞＜''。

## 更新狀況
- 2022/11/9 應用程式完工

## 使用方法
### 作業環境
`windows10` + `gitbash` + `python3.8`。

其他版本不知道有沒有兼容。

### 前置作業
1. 將檔案中的 `app.py` 複製下來，你要用fork或是任何方式都行。
2. 確保你的電腦可以執行 `python3`。
3. 確保你的 `python` 有安裝 `beautifulsoup`, `selenium`。

在 gitbash 執行下列指令安裝，記得把 selenium, beautufulsoup 更新到最新版本。
```
pip install BeautifulSoup4
pip install selenium
```

### 繞過 Capche
先找到自己的chrome瀏覽器在哪個資料夾，然後再該資料夾執行下面的指令。
因為 Zerojudge 登入要 Capche 驗證，所以乾脆直接登入好再讓爬蟲去爬。
使用以下指令，先在指定的 port 打開 chrome 瀏覽器，然後請使用**該指令開啟的瀏覽器**登入 Zerojudge 帳號。
```
./chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\ChromeProfile"
```

### 打開`app.py`程式碼
1. 設定你要哪種 status 的程式碼（AC, WA, TLE, etc.）
2. 設定程式碼中 account_name ，請設成自己的帳號名稱（不是email）。
3. (Optional)設定程式碼中 MAX_PAGE 的值，但不設定也不影響程式執行，只是會跑到 RE 自己停下來。
    - 打開該 status 的 submissions 介面，看最多到幾頁（可以稍微二分搜一下）。
    - 附上 [AC code](https://zerojudge.tw/Submissions?account=HaKkaz&status=AC) 的網址。

### 執行程式碼
執行 `app.py` 程式碼

## 參考資料
- [How to connect Selenium to an existing browser that was opened manually?](https://cosmocode.io/how-to-connect-selenium-to-an-existing-browser-that-was-opened-manually/)
- [How To Execute Selenium Scripts On Already Opened Browser](https://learn-automation.com/how-to-execute-selenium-scripts-on-already-opened-browser/)
