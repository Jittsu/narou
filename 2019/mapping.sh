#!/bin/sh

curl -XPUT 'localhost:9200/narou_index' -H 'Content-Type: application/json' -d'
{
  "settings": {
    "analysis": {
      "tokenizer": {
        "kuromoji": {
          "type": "kuromoji_tokenizer",
          "mode": "search"
        }
      },
      "analyzer": {
        "kuromoji": {
          "type": "custom",
          "tokenizer": "kuromoji",
          "filter": [
            "kuromoji_baseform",
            "kuromoji_part_of_speech"
          ]
        }
      }
    }
  },
  "mappings" : {
    "properties" : {
      "all_hyoka_cnt" : {
        "type" : "long"
      },
      "all_point" : {
        "type" : "long"
      },
      "biggenre" : {
        "type" : "long"
      },
      "end" : {
        "type" : "long"
      },
      "fav_novel_cnt" : {
        "type" : "long"
      },
      "general_all_no" : {
        "type" : "long"
      },
      "general_firstup" : {
        "type" : "date",
        "format" : "yyyy-MM-dd HH:mm:ss"
      },
      "general_lastup" : {
        "type" : "date",
        "format" : "yyyy-MM-dd HH:mm:ss"
      },
      "genre" : {
        "type" : "long"
      },
      "gensaku" : {
        "type" : "text",
        "fields" : {
          "keyword" : {
            "type" : "keyword",
            "ignore_above" : 256
          }
        }
      },
      "global_point" : {
        "type" : "long"
      },
      "isbl" : {
        "type" : "long"
      },
      "isgl" : {
        "type" : "long"
      },
      "isr15" : {
        "type" : "long"
      },
      "isstop" : {
        "type" : "long"
      },
      "istenni" : {
        "type" : "long"
      },
      "istensei" : {
        "type" : "long"
      },
      "iszankoku" : {
        "type" : "long"
      },
      "kaiwaritu" : {
        "type" : "long"
      },
      "keyword" : {
        "type" : "text",
        "fields" : {
          "keyword" : {
            "type" : "keyword",
            "ignore_above" : 256
          }
        },
	"analyzer" : "kuromoji"
      },
      "length" : {
        "type" : "long"
      },
      "ncode" : {
        "type" : "text",
        "fields" : {
          "keyword" : {
            "type" : "keyword",
            "ignore_above" : 256
          }
        }
      },
      "novel_type" : {
        "type" : "long"
      },
      "novelupdated_at" : {
        "type" : "date",
        "format" : "yyyy-MM-dd HH:mm:ss"
      },
      "pc_or_k" : {
        "type" : "long"
      },
      "review_cnt" : {
        "type" : "long"
      },
      "sasie_cnt" : {
        "type" : "long"
      },
      "story" : {
        "type" : "text",
        "fields" : {
          "keyword" : {
            "type" : "keyword",
            "ignore_above" : 256
          }
        },
	"analyzer" : "kuromoji"
      },
      "time" : {
        "type" : "long"
      },
      "title" : {
        "type" : "text",
        "fields" : {
          "keyword" : {
            "type" : "keyword",
            "ignore_above" : 256
          }
        },
	"analyzer" : "kuromoji"
      },
      "updated_at" : {
        "type" : "date",
        "format" : "yyyy-MM-dd HH:mm:ss"
      },
      "userid" : {
        "type" : "long"
      },
      "writer" : {
        "type" : "text",
        "fields" : {
          "keyword" : {
            "type" : "keyword",
            "ignore_above" : 256
          }
        }
      }
    }
  }
}
'
