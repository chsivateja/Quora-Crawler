quora_crawl
===========
This script crawl question and topics in Quora

This script is used to test a novel Q&A system

steps:

1. get list_topic_quesiotn.txt

2. run quoraquestion_crawl.py to crawl quesiton content, user who asked question, datetime when quesiton is asked, answers num, answers content, answer upvote, users who answered the question, ect, which generate result.txt and user_url.txt

3. run user_quora_crawl.py to crawl users name and following topics, which generate user_info.txt

4. the question wrapper in format: 
{'qid':qid, 'ans_num':ans_num, 'question':question, 'answers':[{'answer':answer, 'upvote':upvote, 'answer_user':answer_user},{}...]}

5. the user_info wrapper in format:
{'user_name':user_name, 'user_topics':[topic1, topic2...]}



