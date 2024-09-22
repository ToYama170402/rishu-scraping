from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from typing import List


def rishu_scraping() -> List[List[str]]:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)

    print("Accessing the target page...")
    driver.get(
        "https://eduweb.sta.kanazawa-u.ac.jp/portal/Public/Regist/RegistrationStatus.aspx?year=2024&lct_term_cd=21"
    )

    # ドロップダウンリストの要素を取得
    print("Selecting the dropdown list...")
    dropdown = Select(
        driver.find_element(By.ID, "ctl00_phContents_ucRegistrationStatus_ddlLns_ddl")
    )
    # オプションを全件に変更
    print("Changing the dropdown list to 'All'...")
    dropdown.select_by_index(0)

    # テーブル行の要素を取得
    print("Getting the table rows...")
    records = driver.find_elements(
        By.CSS_SELECTOR, "#ctl00_phContents_ucRegistrationStatus_tbGridView table tr"
    )

    # 各行のすべての列を取得
    arr = list(
        map(
            lambda record: list(
                map(
                    lambda column: column.text,
                    record.find_elements(By.CSS_SELECTOR, "td, th"),
                )
            ),
            records,
        )
    )
    return arr
