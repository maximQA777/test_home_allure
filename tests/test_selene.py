from selene import browser, have,  by
from selene.support.shared.jquery_style import s



browser.open("https://github.com")
browser.driver.fullscreen_window()
s('.search-input').click()
s('#query-builder-test').send_keys("eroshenkoam/allure-example").press_enter()

s(by.link_text("eroshenkoam/allure-example")).click()

s("#issues-tab").click()

s("[data-testid='list-row-repo-name-and-number']").should(have.text('95'))