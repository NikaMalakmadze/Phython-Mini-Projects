import requests
from bs4 import BeautifulSoup
import json
import time

# set headers for requests library to simulate a get request from real browser
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Connection': 'keep-alive'
}

# function to visit all pages of moazrovne.net and get questions data from them
def scrap_images():

    BASE_URL = 'http://moazrovne.net/chgk/'

    last_page = 140

    questions_list = []                 # list were processed questions will be saved

    for page in range(1, last_page+1):
        try:
            response = requests.get(f'{BASE_URL}{page}', headers=HEADERS)       # send get request on specific page (from 1 to last page - 140)

            # skip page if get request was not successful
            if response.status_code != 200:
                print(f'Error While getting page N:{page}!')
                continue

            # process response using bs
            soup = BeautifulSoup(response.text, 'html.parser')

            # find ul on page that will have questions in it (select all li)
            questions_ul = soup.select('ul.questions li.q')

            # skip if no questions founded
            if not questions_ul:
                print(f'No questions on page N:{page}')
                continue

            print(f'Founded {len(questions_ul)} questions on page N:{page}')

            # loop through each li
            for li in questions_ul:

                # dict that will store data about question
                question_data = {}

                # find and get question id
                question_id = li.select_one('p.question_top span.left a')

                # if id founded, set new key:value pair in the question_data dict - 'id': id of question element
                if question_id:
                    question_data['id'] = question_id.text.split()[-1] 

                # find and get actual question
                question_desc = li.select_one('p.question_question')

                # if question founded, set new key:value pair in the question_data dict - 'question': question of question element
                if question_desc:
                    question_data['question'] = question_desc.text.strip()

                # find and get div that contains answer of question and some more info about it
                answers_div = li.select_one('div.answer_body')

                if answers_div:

                    # select every span item
                    spans = answers_div.select('span.clearfix')

                    # loop through each span
                    for span in spans:
                        # find and get needed elements
                        answer_label = span.select_one('span.left')
                        answer_value = span.select_one('span.right_nofloat')

                        # if elements were founded get their inner text
                        if answer_label and answer_value:
                            answer_label_text = answer_label.text.strip()
                            answer_value_text = answer_value.text.strip()

                            # save answer_value_text variable value if it is answer or comment of question
                            if 'პასუხი:' in answer_label_text:
                                question_data['answer'] = answer_value_text
                            elif 'კომენტარი:' in answer_label_text:
                                question_data['comment'] = answer_value_text
                
                # add question dict in the list if it has at least - id, question and answer
                if question_data['question'] and question_data['answer'] and question_data['id']:
                    questions_list.append(question_data)
            
            # give a rest to server
            time.sleep(0.5)

        # log info on console if any error and skip current page       
        except Exception as e:
            print(f'Error While proccessing page: {str(e)}')    
            continue

    # return all questions
    return questions_list

# simple function to save questions in seperated json file
#   it needs:
#       actual questions that will be saved in json file
#       path to the output json file
def save_to_json(questions, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print(f'Questions saved to {output_path}')

if __name__ == '__main__':
    questions = scrap_images()
    if questions:
        save_to_json(questions, 'MoazrovneScraper/output.json')
    else:
        print('No questions Found!')