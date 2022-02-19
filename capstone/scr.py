#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from bs4 import BeautifulSoup
import lxml

def parse(full_url):
    
    page_content = BeautifulSoup(full_url.content, 'lxml')
    containers = page_content.findAll('div', 
                 {'data-tn-section':'reviews'})
    
    global df, df1
    
    df = pd.DataFrame(columns = 
         ['rating', 'rating_title',  'rating_description',
                         'rating_pros', 'rating_cons'])
    
    for item in containers:
        #RATING
        try:
            rating = item.find('button', 
                     {'class': 'css-1c33izo e1wnkr790'}).text.replace('\n', '')

        except:
            rating = None
                     
        # TITLE             
        try:
            rating_title = item.find('h2', 
                           {'data-testid': 'title'}).text.replace('\n', '')

        except:
            rating_title = None

        #DESCRIPTION 
        try:
            rating_description = item.find('div', 
                                 {'data-tn-component': 'reviewDescription'}).text.replace('\n', '.')

        except:
            rating_description = None

         #<span class="css-82l4gy eu4oa1w0">great place to work, nice people, interesting, impactful projects. Lots of great perks, and very supportive culture. Hardest par to job is learning to navigate the large company quickly. </span>
    
        #PROS
        try:
            rating_pros = item.find('div', 
                          {'class': 'css-1z0411s e1wnkr790'}).text.replace('\n', '')

                        
        except:
            rating_pros = None

        #CONS
        try:
            cons_ = page_content.findAll('class', 
                 {'css-82l4gy eu4oa1w0'})

            for i, j in zip(cons_, range(1, 3)):
                if j == 1:
                    pass
                else:
                    output = i
                    print(output)
                          
        except:
            
            rating_cons = None
        
        
        df = df.append({'rating': rating, 
             'rating_title': rating_title, 
             'rating_description': rating_description,
             'rating_pros': rating_pros,
             'rating_cons': rating_cons}, ignore_index=True)

    return df
    

