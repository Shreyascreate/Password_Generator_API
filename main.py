from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
import string
import requests
import random

app = FastAPI()

class PasswordGenerator(BaseModel):
	length : int
	req_uppercase : bool = True
	req_lowercase : bool = True
	req_digit : bool = True
	req_special_char : bool = True

def generate_password(length : int, req_uppercase : bool = True, req_lowercase : bool = True, req_digit : bool = True, req_special_char: bool = True) -> str:
	pass_word = ""
	if req_uppercase: 
		pass_word += string.ascii_uppercase
	if req_lowercase:
		pass_word += string.ascii_lowercase
	if req_digit:
		pass_word += string.digits
	if req_special_char:
		pass_word += string.punctuation
	pass_word_list = random.choices(pass_word, k = length)
	return ''.join(pass_word_list)

@app.post("/generate-password")
async def new_password_generator(pass_word_request: PasswordGenerator = Body(...)):
	if pass_word_request.length < 12 or pass_word_request.length > 64:
		raise HTTPException(status_code=400, detail= "The length of password should be more 12 and less than 64")
	password = generate_password(pass_word_request.length, pass_word_request.req_uppercase, pass_word_request.req_lowercase, pass_word_request.req_digit, pass_word_request.req_special_char)
	return {"password" : password, "length" : pass_word_request.length}

@app.get("/food/nutrition")
async def get_nutrition(meal : str):
	api_key = "YOUR_API_KEY"
	api_id = "YOUR_API_ID"
	url = f"https://api.edamam.com/api/nutrition-data?app_id={api_id}&app_key={api_key}&ingr={meal}"
	response = requests.get(url)
	if response.status_code != 200:
		raise HTTPException(status_code=404, detail="Food not found")
	data = response.json()
	return data