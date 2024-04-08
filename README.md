# Password Generator API

##
This API allows users to generate secure passwords based on specified criteria and retrieve nutritional information for food items.
##

1. Clone the repository:

    ```bash
    git clone https://github.com/Shreyascreate/Password_Generator_API.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your_repository
    ```

3. Install dependencies:

    ```bash
    pip install fastapi uvicorn
    ```
    ```bash
    pip install pydantic
    ```
4. Obtain API keys:
   - **Password Generator API:** No API keys required.
   - **Nutrition API:** Obtain API keys from Edamam Nutrition API and replace `"YOUR_API_KEY"` and `"YOUR_API_ID"` in the code with your actual API key and ID.

5. Run the application:

    ```bash
    uvicorn main:app --reload
    ```

The API will now be running locally on http://localhost:8000.
##
## Usage

### Generate Password

#### Endpoint: `/generate-password`
- **Method:** POST
- **Request Body:** JSON object with the following fields:
  - `length` (int): Length of the password (required)
  - `req_uppercase` (bool): Include uppercase letters (default: true)
  - `req_lowercase` (bool): Include lowercase letters (default: true)
  - `req_digit` (bool): Include digits (default: true)
  - `req_special_char` (bool): Include special characters (default: true)
##
Example request:
```json
{
    "password": "3&ZpW}s!b@6tA1+8",
    "length": 16
}

```
##
Example response:
```json
{
    "length": 16,
    "req_uppercase": true,
    "req_lowercase": true,
    "req_digit": true,
    "req_special_char": true
}

``` 
##
### Get Nutrition Information
#### Endpoint: `/food/nutrition`
- **Method:** GET
- **Query Parameter**
 -> `meal` (string): Food item for which nutrition information is requested (required)
##

Example request: 
```bash
GET /food/nutrition?meal=coffee
```
##
Example response

```json
{
    "uri": "http://www.edamam.com/ontologies/edamam.owl#recipe_5ca389b530e4a100588b08f6e72dce8d",
    "yield": 1.0,
    "calories": 430.24,
    "totalWeight": 223.0,
    "dietLabels": [],
    "healthLabels": [
        "SUGAR_CONSCIOUS",
        "PEANUT_FREE",
        "TREE_NUT_FREE",
        "ALCOHOL_FREE",
        "SULPHITE_FREE"
    ],
    ...
}
```
##

## Testing

You can test the API endpoints using tools like cURL, Postman, or writing your own client application. Make requests to the respective endpoints with appropriate parameters to generate passwords and retrieve nutrition information. The screenshots of the outputs are available in the screenshot folder.
##
## Conclusion
This README provides a brief overview of how to set up and use the API for testing purposes. Make sure to replace placeholders like "YOUR_API_KEY" and "YOUR_API_ID" with your actual API keys before running the application. Since the API key and API ID are private. 

