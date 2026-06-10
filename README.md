to run the app run those commands : 

terminal 1 : 
    cd .\frontend\
    npm i
    npm run dev
terminal 2 : 
    cd .\backend\
    .\venv\Scripts\activate ( activate virtual environment for windows )
    uvicorn app.main:app --reload

the app uses both gemini-3.5-flash and mistral 7b (local) and it has a swap feature in the frontend main page

put GOOGLE_API_KEY in .env in backend folder (gemini-3.5-flash use case )
put NEXT_PUBLIC_BACKEND_URL = http://localhost:8000 in .env in frontendfolder

for both cases check the .env.sample file for better understanding


to use the summerize tool drag a document to summerize from the sibarbar panel and drop it in the input area (1 document per input)