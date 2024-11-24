from playwright.sync_api import Playwright,sync_playwright,expect

def scrape_finance(playwright: Playwright, symbol: str,date: str) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://finance.yahoo.com/quote/{symbol}")

    price_selector = page.query_selector("fin-streamer.livePrice")
    price = price_selector.inner_text()
    print(symbol, price)

    context.close()
    browser.close()

    return {
        "symbol": symbol,
        "price": price,
        "date": date

    }


with sync_playwright() as playwright:
    sym_data = scrape_finance(playwright, "AAPL", "2024-11-11")
    print(sym_data)