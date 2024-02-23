"""
This script connects to the StackExchange API and parses it to get the following:
1. The number of answered and unanswered responses
2. The answer with the least number of views
3. The oldest and most current answer
4. The response of the owner who has a greater reputation

**Author:** Paul Martin Garcia Morfin
**Date:** 2024-02-22

**Output:**
* Prints the information found.
"""

import requests

def connect_to_api(api_url):
    """
    Connects to the API and retrieves data.
    """
    try:
        # Connect to API
        response = requests.get(api_url)
        response.raise_for_status()
        return response
    
    except Exception as e:
        # Handle API specific error
        print(f"Error connecting to the API: {e}")
        return None
    
def count_answers(data):
    """
    Counts the number of answered and unanswered responses.
    """
    answered_count = 0
    unanswered_count = 0
    for item in data["items"]:
        if item["is_answered"]:
            answered_count += 1
        else:
            unanswered_count += 1
    return answered_count, unanswered_count

def get_least_views_item(data):
    """
    Finds the item with the least number of views.
    """
    min_views_item = None
    for item in data["items"]:
        if min_views_item is None or item["view_count"] < min_views_item["view_count"]:
            min_views_item = item
    return min_views_item

def get_oldest_and_newest_item(data):
    """
    Finds the oldest and newest item based on creation date.
    """
    oldest_item = None
    newest_item = None
    for item in data["items"]:
        if oldest_item is None or item["creation_date"] < oldest_item["creation_date"]:
            oldest_item = item
        if newest_item is None or item["creation_date"] > newest_item["creation_date"]:
            newest_item = item
    return oldest_item, newest_item   

def get_owner_highestrep_item(data):
    """
    Finds the item from the owner who has the highest reputation.
    """
    owner_highestrep_item = None
    for item in data["items"]:
        if owner_highestrep_item is None or item["owner"]["reputation"] > owner_highestrep_item["owner"]["reputation"]:
            owner_highestrep_item = item
    return owner_highestrep_item

def main():  
    # API URL
    api_url = "https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow"
    data = connect_to_api(api_url).json()

    if data:
        answered_count, unanswered_count = count_answers(data)
        min_views_item = get_least_views_item(data)
        oldest_item, newest_item = get_oldest_and_newest_item(data)
        owner_highestrep_item = get_owner_highestrep_item(data)

        print(f"Respuestas contestadas: {answered_count}")
        print(f"Respuestas no contestadas: {unanswered_count}")
        print("Respuesta con menor número de vistas (ID):", min_views_item["question_id"])
        print("Respuesta más vieja (ID):", oldest_item["question_id"])
        print("Respuesta más actual (ID):", newest_item["question_id"])
        print("Respuesta del owner con mayor reputación (ID):", owner_highestrep_item["question_id"])

if __name__ == "__main__":
    main()