import requests

print("Malleeee")

def fetch_rand_usr():
  url= "https://api.freeapi.app/api/v1/public/randomusers/user/random"
  response = requests.get(url)
  data= response.json()
 # print (data)

  if data["success"] and "data" in data:
    user_info= data["data"]
    user_email= user_info["email"]
    city= user_info["location"]["city"]
    return user_email, city
  
  else:
    raise Exception("Failed to fetch user")
  

def main():
    try:
     user_email,city= fetch_rand_usr()
     print("Email: ", user_email, "City: ", city)
    except Exception as e:
      print(str(e))

if __name__=="__main__":
  main()

