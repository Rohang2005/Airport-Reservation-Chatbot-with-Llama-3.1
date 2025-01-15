import firebase_admin
from firebase_admin import credentials, db
import json
import ollama

cred = credentials.Certificate("FirebaseKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://aoop-46569-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

def download_flight_data():
    try:
        ref = db.reference('flights')
        flight_data = ref.get()
        if flight_data:
            print('Flight data downloaded from Firebase Realtime Database.')
            if isinstance(flight_data, dict):
                flight_data = list(flight_data.values())
            return flight_data
        else:
            print('No flight data found in the database.')
            return []
    except Exception as e:
        print(f"Error downloading flight data: {e}")
        return []

def filter_flight_data(flight_data, query):
    relevant_flights = []
    for flight in flight_data:
        if isinstance(flight, dict):
            if query.lower() in flight.get('destination', '').lower() or \
               query.lower() in flight.get('origin', '').lower():
                relevant_flights.append({
                    'flight_number': flight.get('flight_number'),
                    'origin': flight.get('origin'),
                    'destination': flight.get('destination'),
                    'departure_time': flight.get('departure_time'),
                    'arrival_time': flight.get('arrival_time'),
                    'price': flight.get('price'),
                })
    return relevant_flights

def ask_llama(prompt, relevant_flights):
    system_prompt = """You are an assistant for an airport ticket reservation system. 
You help users find available domestic and international flights, provide flight prices, 
and assist with booking flights. Use the following relevant flight data to answer queries. 
If no relevant flights are available, respond no flights available. 
You can also have normal conversations with users:\n\n"""

    if relevant_flights:
        formatted_flights = json.dumps(relevant_flights, indent=2)
    else:
        formatted_flights = "No relevant flights available."

    full_prompt = system_prompt + formatted_flights + "\n\nUser: " + prompt + "\nAssistant:"

    try:
        response = ollama.generate(model="llama3.1", prompt=full_prompt)

        if isinstance(response, dict) and 'response' in response:
            return response['response'].strip() 
        else:
            return "Unexpected response structure from Ollama."
    
    except Exception as e:
        print(f"Error querying Llama model: {e}")
        return "I'm sorry, I couldn't process your request."

def start_conversation(flight_data):
    while True:
        user_prompt = input("You: ")

        if user_prompt.lower() in ['exit', 'quit', 'bye', 'goodbye']:
            print("Airbot: Goodbye!")
            break
        
        relevant_flights = filter_flight_data(flight_data, user_prompt)
        response = ask_llama(user_prompt, relevant_flights)
        print("AirBot:", response)

if __name__ == "__main__":
    flight_data = download_flight_data()

    start_conversation(flight_data)
