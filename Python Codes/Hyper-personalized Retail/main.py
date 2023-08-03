import application_script as py1
import openai
import streamlit as st

data_dict=py1.converted_data

openai.api_key = 'your-api-key'

completion_1 = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", 
     "content": """Below is my data and information about the products that are offered by our BFSI organisation, just understanding it. 
                  Now i want you to recommend personalised product for each clients. Just say client id, the recommended product and 20 words reasoning for the product.
                  
                  Information about products:
                  1. Banking Services
                  2. Advisory Services
                  3. Wealth Management
                  4. Mutual Funds
                  5. Insurance
                  6. Brokerage Services
                  7. Credit Cards
                  8. Retirement Plans
                  9. Foreign Exchange Services
                  10. Payment Processing
                  
                  Data:
                  {{'ClientID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 
                  'Age': [35, 28, 45, 22, 33, 40, 28, 30, 50, 21, 38, 48, 25, 35, 42, 26, 30, 32, 45, 40], 
                  'Location': ['Mumbai', 'Delhi', 'Bengaluru', 'Hyderabad', 'Chennai', 'Kolkata', 'Ahmedabad', 'Pune', 'Jaipur', 'Lucknow', 'Kochi', 'Chandigarh', 'Indore', 'Vadodara', 'Visakhapatnam', 'Surat', 'Agra', 'Coimbatore', 'Patna', 'Bhubaneswar'], 
                  'FinancialGoals': ['Saving for a down payment on a house', 'Planning for retirement', 'Paying off student loans', 'Saving for a down payment on a house', 'Paying off student loans', 'Planning for retirement', 'Saving for a down payment on a house', 'Planning for retirement', 'Paying off student loans', 'Saving for a down payment on a house', 'Paying off student loans', 'Planning for retirement', 'Saving for a down payment on a house', 'Planning for retirement', 'Paying off student loans', 'Saving for a down payment on a house', 'Paying off student loans', 'Planning for retirement', 'Saving for a down payment on a house', 'Planning for retirement'], 'RiskAppetite': ['Moderate', 'Conservative', 'Aggressive', 'Moderate', 'Conservative', 'Aggressive', 'Moderate', 'Conservative', 'Aggressive', 'Moderate', 'Conservative', 'Aggressive', 'Moderate', 'Conservative', 'Aggressive', 'Moderate', 'Conservative', 'Aggressive', 'Moderate', 'Conservative'], 
                  'MonthlyIncome': [57017, 74302, 57502, 52696, 49878, 61983, 35670, 62535, 62877, 36910, 34147, 77883, 51347, 73147, 50545, 41324, 75998, 64630, 67745, 78257], 'EmploymentType': ['Salaried', 'Self-Employed', 'Salaried', 'Self-Employed', 'Salaried', 'Self-Employed', 'Salaried', 'Self-Employed', 'Salaried', 'Self-Employed', 'Salaried', 'Self-Employed', 'Salaried', 'Self-Employed', 'Salaried', 'Self-Employed', 'Salaried', 'Self-Employed', 'Salaried', 'Self-Employed'], 
                  'CreditScore': [601, 780, 656, 839, 733, 662, 840, 804, 787, 566, 642, 826, 815, 600, 760, 509, 597, 572, 824, 654], 
                  'LoanAmount': [3482199, 4942776, 1853757, 1039925, 983632, 2007370, 4882218, 1325374, 2896708, 3906877, 319601, 1426815, 3186156, 2608334, 3297190, 4054401, 3370512, 298485, 808258, 3693348], 
                  'LoanTerm': [36, 48, 24, 48, 60, 12, 12, 60, 36, 24, 12, 12, 48, 60, 24, 12, 12, 48, 24, 12], 
                  'NumOfPreviousLoans': [0, 5, 2, 2, 2, 5, 5, 2, 1, 4, 3, 1, 2, 1, 2, 2, 4, 2, 3, 2], 'NumOfDependents': [0, 0, 1, 1, 1, 1, 2, 1, 3, 1, 3, 1, 2, 0, 1, 0, 1, 1, 0, 2]}}"""
 
  }]
)

response_1=completion_1.choices[0].message.content
st.write(response_1)











