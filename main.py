"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai

genai.configure(api_key="AIzaSyBoS4G9SRo7mN2WCD9EIRYyfeAhiljKhp8")

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.5,
  "top_k": 0,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
  
])

prompt='Je veux que tu te comportes comme un expert en ressource humaine .Tu es un expert dans ce domaine, et je t\'ai recruté afin que tu entraines  les etudiants à passer des entretiens de stages dans le secteur du developpement web.Au debut de la conversation tu lui diras ce message : \'Bonjour , Mon role est de t\'entrainer  afin que  réussisses ton entretien\'.Puis par après reviens à la ligne et tu commences l\'entrainement en lui posant une question.' 
convo.send_message(prompt)
print(convo.last.text)
convo.history=convo.history.pop(1)


for i in range(10) :        
        
            reponse=input('>')
            convo.send_message(f'voici la reponse : {reponse}.repond :`\'c\'est super ça\' si ça reponse est pertinente .Sinon repond : \'okey\' ou repon en utilisant des synonyme de \'okey\' .Tu ne diras rien d\'autres autres que la consille que je t\'ai doné ')
            print(convo.last.text)
            convo.send_message('Poses lui une autre Question. Cette question peut aller dans le sens de sa reponse ou pas . Je ne veux pas voir de commentaire dans ta reponse . Je dis bien une question et uniquement une question .')
            print(convo.last.text)
        
            
    
    
