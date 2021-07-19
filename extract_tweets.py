import os

TWEETS_TOPICS = [
    ("quarentena", "quarentena.json"),
    ("ficar em casa", "ficaremcasa.json"),
    ("#quarentena", "hash_quarentena.json"),
    ("#FiqueEmCasa", "hash_fiqueemcasa.json" ),
    ("#covid19 #Brasil", "hash_covidbrasil.json"),
    ("lockdown brasil", "lockdownbrasil.json"),
    ("medidas restritivas", "medidasrestritivas.json"),
    ("toque de recolher", "toquederecolher.json")
]

TWEETS_SENTIMENTS = [
    ("#desprezo", "desprezo.json"),
    ("#nojo", "nojo.json"),
    ("#raiva", "raiva.json"),
    ("#triste", "tristeza.json")
]

DATE_INTERVAL = [
            ("2020-02-01", "2020-07-31"),
            ("2020-08-01", "2021-01-31")
]

def extract_tweets(since, until, topic, filename, formato="jsonl", max_results=350000):
  os.system(f"snscrape --jsonl --max-results {max_results} --since {since} twitter-search '{topic} until:{until}' > raw/{since}/{filename}")


if __name__ == "__main__":
    for topic, filename in TWEETS_TOPICS:
        for since, until in DATE_INTERVAL:
            extract_tweets(since, until, topic, filename)
