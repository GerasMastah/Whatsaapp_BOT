from flask import Flask
import requests
import os
from flask import request
from twilio.twiml.messaging_response import MessagingResponse
from sisa_scraper import *
from classroom import *


app = Flask(__name__)



@app.route('/', methods=['POST'])
def bot():
        
        incoming_msg = request.values.get('Body', '').lower()
        resp = MessagingResponse()
        msg = resp.message()
        responded = False
    
        if '.geras' in incoming_msg:
                if 'cat' in incoming_msg:
                    msg.media('https://image.shutterstock.com/image-photo/cat-medical-mask-protective-antiviral-600w-1684423789.jpg')
                    responded = True
                if 'sisa' in incoming_msg:
                    msg.body(grades())
                    responded = True
                if 'tarea' in incoming_msg:
                    msg.body(main())
                    responded = True
                if not responded:
                    msg.body('No te puedo ayudar')
        return str(resp)

    

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
