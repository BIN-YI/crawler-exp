class BrowserSettings:
    browser_path = ''
    web_driver_path = ''


class TargetSettings:
    tickers = ['TSM']


configs = {
    'bs': BrowserSettings,
    'ts': TargetSettings
}
