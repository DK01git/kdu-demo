import os
from dotenv import load_dotenv, find_dotenv

# tload env diel                                                                                                                    
def load_env():
    _ = load_dotenv(find_dotenv())

def get_groc_api_key():
    load_env()
    groc_api_key = os.getenv("GROQ_API_KEY")
    if not groc_api_key:
        raise ValueError("No GROQ_API_KEY set for Groc API")
    return groc_api_key

def get_serper_api_key():
    load_env()
    groc_api_key = os.getenv("SERPER_API_KEY")
    return groc_api_key


# break to 50
# don't break in the middle 
def pretty_print_result(result):
  parsed_result = []
  for line in result.split('\n'):
      if len(line) > 50:
          words = line.split(' ')
          new_line = ''
          for word in words:
              if len(new_line) + len(word) + 1 > 50:
                  parsed_result.append(new_line)
                  new_line = word
              else:
                  if new_line == '':
                      new_line = word
                  else:
                      new_line += ' ' + word
          parsed_result.append(new_line)
      else:
          parsed_result.append(line)
  return "\n".join(parsed_result)
