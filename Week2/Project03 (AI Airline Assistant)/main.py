# AI Airline assistant

import openai
import ollama
import os
import json
from dotenv import load_dotenv
import gradio as gr
from jupyter_server.services.contents.fileio import path_to_intermediate

load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')
if openai_api_key:
    print(f"Key is present and it begins with {openai_api_key[:8]}")
else:
    print("Key not found")

MODEL = "gpt-4o-mini"
openai = openai.OpenAI()

system_message = "You are a helpful assistant for an Airline called FlightAI."
system_message += "Give short, courteous answers, no more than 1 sentence. "
system_message += "Always be accurate. If you don't know the answer, say so."

# Tool
ticket_prices = {"london": "$799", "paris": "$899", "tokyo": "$1499", "berlin": "$499"}
flight_timings = {"london" : "6:00am IST and 7:00 pm IST"}

def get_ticket_price(destination_city):
    print(f"Tool is called for city : {destination_city}")
    city = destination_city.lower()
    return ticket_prices.get(city, "Unknown")

def get_flight_timings(destination_city):
    print(f"Tool called for city : {destination_city}")
    city = destination_city.lower()
    return  flight_timings.get(city,"Unknown")

price_function = {
    "name": "get_ticket_price",
    "description": "Get the price of a return ticket to the destination city. Call this whenever you need to know the ticket price, for example when a customer asks 'How much is a ticket to this city'",
    "parameters": {
        "type": "object",
        "properties": {
            "destination_city": {
                "type": "string",
                "description": "The city that customer wants to travel to",
            },
        },
        "required": ["destination_city"],
        "additionalProperties": False,
    }
}

timings_function = {
    "name": "get_flight_timings",
    "description": "Get the timings of a return ticket to the destination city. Call this whenever you need to know the ticket price, for example when a customer asks 'When is a flight to this city'",
    "parameters": {
        "type": "object",
        "properties": {
            "destination_city": {
                "type": "string",
                "description": "The city that customer wants to travel to",
            },
        },
        "required": ["destination_city"],
        "additionalProperties": False,
    }
}

# And this is included in a list of tools:
tools = [{"type": "function", "function": price_function},{"type": "function", "function": timings_function}]

def chat(message, history):
    # print("History is :",history,"\n")
    messages = [{"role": "system", "content": system_message}] + history + [{"role": "user", "content": message}]

    response = openai.chat.completions.create(model=MODEL, messages=messages, tools=tools)

    # When the model asks to run tool
    if response.choices[0].finish_reason=="tool_calls":
        message = response.choices[0].message
        # print("Message ie response.choices[0].message :",message,"\n")
        response,city = handle_tool_call(message)
        # print("Response from handle_tool_call :",response)
        messages.append(message)
        messages.append(response)
        response = openai.chat.completions.create(model=MODEL, messages=messages)
    return response.choices[0].message.content


def handle_tool_call(message):
    # print("Handle tool call : \n")
    tool_call = message.tool_calls[0]
    func_name = tool_call.function.name
    print("message.tool_cal[0] : ",tool_call)

    arguments = json.loads(tool_call.function.arguments)
    city = arguments.get('destination_city')

    if func_name == 'get_ticket_price':
        price = get_ticket_price(city)
        response = {
            "role" : "tool",
            "content" : json.dumps({"destination_city":city, "price" : price}),
            "tool_call_id" : tool_call.id
        }
    else:
        timings = get_flight_timings(city)
        response = {
            "role": "tool",
            "content": json.dumps({"destination_city": city, "timings": timings}),
            "tool_call_id": tool_call.id
        }
    return response, city

gr.ChatInterface(fn=chat,type="messages").launch()

