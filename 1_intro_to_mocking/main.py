import requests

url = "http://www.randomnumberapi.com/api/v1.0/random?min=1&max=100&count=2"

def get_random_numbers():
    response = requests.get(url).json()
    return response[0], response[1]

def add():
    a, b = get_random_numbers()
    return a+b

def main():
    result = add()
    print(result)

if __name__ == "__main__":
    main()