# Unbabel Customer Reporting
This service compiles a monthly report based on each customer's usage of the Unbabel services.


## Usage
To run the server: ```python manage.py runserver```


## Database Structure
![Database Structure](http://i.imgur.com/Xj76y41.png)

The "per_lp" field is an array of JSONs, one for each LP, of the form:
```javascript
{
    'average_ht_delivery_time': float,
    'average_mt_delivery_time': float,
    'avg_price': float,
    'avg_words': float,
    'language_pair': string,
    'number_of_human_translations': int,
    'number_of_progressive_translations': int,
    'number_of_tickets': int,
    'number_of_translations': int,
    'number_of_upgraded_progressive_translations': int,
    'total_price': float,
    'total_words': int
}
```

The "totals" field is a JSON of the form:
```javascript
{
    'delivery_time': {
        'average_ht_delivery_time': float,
        'average_mt_delivery_time': float
    },
    'tickets': {
        'total_ticket_count': int,
        'total_unbabeled_ticket_count': int
    },
    'translations': {
        u'number_of_human_translations': int,
        u'number_of_progressive_translations': int,
        u'number_of_translations': int,
        u'number_of_upgraded_progressive_translations': int
    },
    'words_and_prices': {
        u'avg_price': float,
        u'avg_words': float,
        u'total_price': float,
        u'total_words': int
    }
}
```
