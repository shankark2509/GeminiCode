import logging
import requests, json
import statistics

class AlertTool(object):
    """
    Class to generate alerts
    """
    def __init__(self,logger,currency,deviation):
        self.logger = logger
        self.currency = currency
        self.deviation = deviation

    def priceChange(self):
        """
        Function to generate alerts when a Currency has 24h - PercentChange greater than threshold
        :return:
        """
        base_url = "https://api.gemini.com/v1"
        if self.currency =="ALL":
            response = requests.get(base_url + "/pricefeed")
        else:
            response = requests.get(base_url + "/pricefeed/" + self.currency)
        self.logger.info("Requesting PriceFeed API Data")
        if response.ok:
            price = response.json()
            self.logger.info("Running checks to see if PriceChange Alert is met.")
            for stock in price:
                if float(stock["percentChange24h"]) >= self.deviation:
                    self.logger.error("Currency is %s \n Percent Change %s" % (stock["pair"],stock["percentChange24h"]))
        else:
            self.logger.info("Invalid currency")

    def getSymbols(self):
        """
        Function to get list of cryptocurrency supported by the exchange
        :return: List of Symbols
        """
        base_url = "https://api.gemini.com/v1"
        response = requests.get(base_url + "/symbols")
        symbols = response.json()
        return symbols
    def priceDeviation(self):
        """
        Function to generate alert when Currency has standard deviation greater than threshold
        :return:
        """
        base_url = "https://api.gemini.com/v2"
        if self.currency == "ALL":
            self.logger.info("Fetching list of currencies")
            symbols = self.getSymbols()
            for cur in symbols:
                self.logger.info("Fetching API data for currency %s" % cur)
                response = requests.get(base_url + "/ticker/" + cur)
                if response.ok:
                    currency_data = response.json()
                    priceList = [float(c) for c in currency_data["changes"]]
                    std = statistics.stdev(priceList)
                    self.logger.info("Running Standard Deviation check on %s" % currency_data["symbol"])
                    if std >= self.deviation:
                        self.logger.error("Price Deviation: Currency %s Standard Deviation Change %s"%(currency_data["symbol"],std))
                else:
                    self.logger.info("Invalid currency %s" % cur)
        else:
            self.logger.info("Fetching API data for currency %s" % self.currency)
            response = requests.get(base_url + "/ticker/" + self.currency)
            if response.ok:
                currency_data = response.json()
                priceList = [float(c) for c in currency_data["changes"]]
                std = statistics.stdev(priceList)
                self.logger.info("Running Standard Deviation check on %s" %self.currency)
                if std >= self.deviation:
                    self.logger.error("Price Deviation: Currency %s Standard Deviation Change %s" % (currency_data["symbol"], std))
            else:
                self.logger.info("Invalid currency %s" % cur)
    def volumeDeviation(self):
        """
        Function to calculate if latest trade is more than x% of 24h volume
        :return:
        """
        base_url = "https://api.gemini.com/v1"
        if self.currency == "ALL":
            self.logger.info("Fetching list of currencies")
            symbols = self.getSymbols()
            for cur in symbols:
                self.logger.info("Fetching API data for currency %s" % cur)
                response = requests.get(base_url + "/pubticker/" + cur)
                if response.ok:
                    currency_data = response.json()
                    #Check if price currency is USD
                    if "USD" in currency_data["volume"]:
                        self.logger.info("Fetching Volume in USD")
                        volume = currency_data["volume"]["USD"]
                    #Check if price currency is GUSD
                    elif "GUSD" in currency_data["volume"]:
                        self.logger.info("Fetching Volume in GUSD")
                        volume = currency_data["volume"]["GUSD"]
                    self.logger.info("Getting most recent trade information")
                    lastTrade = currency_data["last"]
                    self.logger.info("Checking for volume deviation for currency %s" % cur)
                    if float(lastTrade) >= ((self.deviation/100)*float(volume)):
                        self.logger.error("Volume Deviation: Currency %s - Quantity of most recent trade is greater than %f of the total volume"%(cur,self.deviation))
                else:
                    self.logger.info("Invalid currency")
        #Single Currency Passed by User
        else:
            self.logger.info("Fetching API data for currency %s" % self.currency)
            response = requests.get(base_url + "/pubticker/" + self.currency)
            if response.ok:
                currency_data = response.json()
                # Check if price currency is USD
                if "USD" in currency_data["volume"]:
                    self.logger.info("Fetching Volume in USD")
                    volume = currency_data["volume"]["USD"]
                # Check if price currency is GUSD
                elif "GUSD" in currency_data["volume"]:
                    self.logger.info("Fetching Volume in GUSD")
                    volume = currency_data["volume"]["GUSD"]
                self.logger.info("Getting most recent trade information")
                lastTrade = currency_data["last"]
                self.logger.info("Checking for volume deviation for currency %s" % self.currency)
                if float(lastTrade) >= ((self.deviation/100)*float(volume)):
                    self.logger.error("Volume Deviation: Currency %s - Quantity of most recent trade is greater than %f of the total volume"%(self.currency,self.deviation))
            else:
                self.logger.info("Invalid currency")



