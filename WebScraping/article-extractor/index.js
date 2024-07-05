import { chromium } from require("playwright")

;(async () => {
    const browser = await chromium.launch()
    const page = await browser.newPage()
    await page.goto("https://www.microsoft.com/es-es/d/xbox-series-x/8wj714n3rbtl?activetab=pivot:informaci%C3%B3ngeneraltab")
    await page.screenshot({ path: "xbox.png" })
    await browser.close()
    }
)()