from playwright.async_api import async_playwright,Playwright,expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com")

    heading = page.selector_all("h2,h3")
    for heading in heading:
        tag = heading.evaluate(" e1 => e1.tagName ")
        text = heading.inner_text()
        print(f"{tag} - {text}")
        if tag  == "h3":
            print(f" {text}")
        else:
            print({text})

    context.close()
    browser.close()

with async_playwright() as playwright:
    run(playwright)