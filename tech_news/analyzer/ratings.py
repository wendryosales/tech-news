from tech_news.database import get_collection


def top_5_news():
    query = [
        {
            "$group": {
                "_id": "$title",
                "comments_count": {"$sum": "$comments_count"},
                "url": {"$first": "$url"},
            }
        },
        {"$sort": {"comments_count": -1, "_id": 1}},
        {"$limit": 5},
    ]
    response = list(get_collection().aggregate(query))
    result = [(item["_id"], item["url"]) for item in response]
    return result


def top_5_categories():
    query = [
        {"$group": {"_id": "$category", "count": {"$sum": 1}}},
        {"$sort": {"count": -1, "_id": 1}},
        {"$limit": 5},
    ]
    response = list(get_collection().aggregate(query))
    return [item["_id"] for item in response]
