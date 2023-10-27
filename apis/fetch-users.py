import requests

# Get the list of users
users_url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(users_url)
users_data = response.json()

if response.status_code == 200:
    for user in users_data:
        user_id = user['id']
        
        # Get user data for each user
        user_data_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
        user_data_response = requests.get(user_data_url)
        user_data = user_data_response.json()

        if user_data_response.status_code == 200:
            print(f"User ID: {user_data['id']}")
            print(f"Name: {user_data['name']}")
            print(f"Username: {user_data['username']}")
            print(f"Email: {user_data['email']}")
            print(f"Phone: {user_data['phone']}")
            print(f"Website: {user_data['website']}")
            print("Address:")
            print(f"  Street: {user_data['address']['street']}")
            print(f"  Suite: {user_data['address']['suite']}")
            print(f"  City: {user_data['address']['city']}")
            print(f"  Zipcode: {user_data['address']['zipcode']}")
            print("Company:")
            print(f"  Name: {user_data['company']['name']}")
            print(f"  Catchphrase: {user_data['company']['catchPhrase']}")
            print(f"  Business: {user_data['company']['bs']}")
            print()
        else:
            print(f"Failed to retrieve user data for user ID {user_id}.")
    else:
        print("All users have been processed.")
else:
    print(f"Failed to retrieve the list of users. Status code: {response.status_code}")
