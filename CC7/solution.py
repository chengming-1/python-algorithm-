"""
Name:chengming wang
Coding Challenge 7 - Lonely Rolling Star - Solution Code
CSE 331 Fall 2020
Professor Sebnem Onsay
"""
from typing import List, Tuple


class Item:
    """
    A class that will store an item's name and category
    """
    def __init__(self, item_name: str, item_category: str):
        self.name = item_name
        self.category = item_category

    def __repr__(self):
        return "Item('" + self.name + "','" + self.category + "')"

    def get_name(self) -> str:
        """
        returns the strng representing the item's name
        :return: Item name string
        """
        return self.name

    def get_category(self) -> str:
        """
        Returns the string representation of the item's category
        :return: Item category string
        """
        return self.category


class RoboKingOfAllCosmos:

    def __init__(self):
        pass
        # put your scoring container here

    def construct_score_book(self, items_and_size: List[Tuple[str, float]]) -> None:
        pass

    def get_score_book(self) -> List[Tuple[str, float]]:
        pass

    def judge_katamari(self, katamari_contents: List[Item]) -> Tuple[float, List[Tuple[str, int]], List[str]]:
        pass



