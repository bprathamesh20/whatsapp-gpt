from fastapi import FastAPI, Request, Response
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from datetime import datetime
from llm import get_response
import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

# Twilio credentials
account_sid = os.getenv('ACCOUNT_ID')
auth_token = os.getenv('AUTH')
client = Client(account_sid, auth_token)

@app.post("/whatsapp")
async def handle_whatsapp(request: Request):
    form_data = await request.form()
    incoming_msg = form_data.get('Body', '').lower()
    sender = form_data.get('From', '')


    response = get_response(incoming_msg)

    # Create a TwiML response
    twiml_response = MessagingResponse()
    msg = twiml_response.message()
    msg.body(response)
    
    
    return Response(content=str(twiml_response), media_type="application/xml")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)