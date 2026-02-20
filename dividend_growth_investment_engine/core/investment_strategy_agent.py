from typing import Dict, List
import pandas as pd

class InvestmentStrategyAgent:
    """
    Implements multi-criteria screening for undervalued dividend stocks.
    
    Uses a combination of fundamental metrics and market conditions to identify attractive investments.
    """

    def __init__(self):
        pass

    def screen_stocks(self, stock_data: Dict) -> List[Dict]:
        """
        Screens stocks based on predefined criteria.
        
        Args:
            stock_data (Dict): Dictionary containing stock data
            
        Returns:
            List[Dict]: List of recommended stocks with buy signals
        """
        # Example screening logic
        recommendations = []
        
        for symbol, data in stock_data.items():
            if self.is_undervalued(data) and self.has_growth_potential(data):
                recommendations.append({
                    "symbol": symbol,
                    "recommendation": "BUY",
                    "score": self.calculate_score(data)
                })
                
        return recommendations

    def is_undervalued(self, data: Dict) -> bool:
        """
        Checks if the stock is undervalued based on P/E ratio and dividend yield.
        
        Args:
            data (Dict): Stock data
            
        Returns:
            bool: True if undervalued
        """
        pe_ratio = data.get("pe_ratio", float('inf'))
        div_yield = data.get("dividend_yield", 0)
        
        return pe_ratio < 15 and div_yield > 2

    def has_growth_potential(self, data: Dict) -> bool:
        """
        Assesses growth potential based on dividend growth rate.
        
        Args:
            data (Dict): Stock data
            
        Returns:
            bool: True if具备增长潜力
        """
        div_growth = data.get("dividend_growth_rate", 0)
        
        return div_growth > 5

    def calculate_score(self, data