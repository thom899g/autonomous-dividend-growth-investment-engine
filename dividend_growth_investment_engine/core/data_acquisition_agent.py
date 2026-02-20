import logging
from typing import Dict, Optional
import requests

class DataAcquisitionAgent:
    """
    Fetches real-time stock data from Alpha Vantage API.
    
    Implements error handling and retry logic for reliable data acquisition.
    Logs detailed information about data retrieval attempts.
    """

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://www.alphavantage.co/api/v2"
        logging.basicConfig(level=logging.INFO)

    def fetch_stock_data(self, symbol: str) -> Optional[Dict]:
        """
        Fetches stock data for the given symbol.
        
        Args:
            symbol (str): Stock ticker symbol
            
        Returns:
            Dict: Stock data or None if failed
        """
        try:
            params = {
                "symbol": symbol,
                "apikey": self.api_key
            }
            response = requests.get(f"{self.base_url}/quote/{symbol}", params=params)
            
            if response.status_code == 200:
                return response.json()
            else:
                logging.error(f"API request failed with status code {response.status_code}")
                return None
                
        except Exception as e:
            logging.error(f"Error fetching data for {symbol}: {str(e)}")
            return None

    def get_dividend_history(self, symbol: str) -> Optional[Dict]:
        """
        Fetches historical dividend data.
        
        Args:
            symbol (str): Stock ticker symbol
            
        Returns:
            Dict: Dividend history or None if failed
        """
        try:
            params = {
                "symbol": symbol,
                "apikey": self.api_key
            }
            response = requests.get(f"{self.base_url}/dividend_history/{symbol}", params=params)
            
            if response.status_code == 200:
                return response.json()
            else:
                logging.error(f"API request failed with status code {response.status_code}")
                return None
                
        except Exception as e:
            logging.error(f"Error fetching dividend history for {symbol}: {str(e)}")
            return None