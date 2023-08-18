import os
import openai
from .__init__ import OPENAI_API_KEY




openai.api_key = OPENAI_API_KEY




def openAIQuery(query):
    response = openai.Completion.create(
      engine="davinci-instruct-beta-v3",
      prompt=query,
      temperature=0.7,
      max_tokens=200,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0)
    
    if 'choices' in response:
        if len(response['choices']) > 0:
          answer = response['choices'][0]['text']
        else:
          answer = "Sorry, for the interruption we are unable to generate "
          
    else:
        answer = "Sorry, for the interruption we are unable to generate"
        
    return answer




def generatecontentTopics(prompt1):
    response = openai.Completion.create(
      engine="davinci-instruct-beta-v3",
      prompt="Generate content topics on: {}. \n  1.  ".format(prompt1),
      temperature=0.7,
      max_tokens=250,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
 
    return response['choices'][0]['text']

def generatecontentSections(prompt1):
    response = openai.Completion.create(
      engine="davinci-instruct-beta-v3",
      prompt="Expand the content title in to high level content sections: {} \n \n  Introduction: 1. ".format(prompt1),
      temperature=0.7,
      max_tokens=100,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    return response['choices'][0]['text']


def contentSectionExpander(prompt1):
    response = openai.Completion.create(
      engine="davinci-instruct-beta-v3",
      prompt="Expand the content section in to a detailed professional , witty and clever explanation.\n\n {}".format(prompt1),
      temperature=0.7,
      max_tokens=1900,
      top_p=0,
      frequency_penalty=0,
      presence_penalty=0
    )

    return response['choices'][0]['text']
