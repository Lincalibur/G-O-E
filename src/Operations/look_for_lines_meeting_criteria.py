#Meet Criteria has the user taken to a new GUI, that will allow the user to fill in values in textBoxes
#These will be next to eachother in the format:
#Column name: ___________ looking for ____________
#Button __Add__

#When Button is pressed then the a new line/condition will be added to the list and the user will be able to add multiple conditions.
#The Conditions will be listed below in a textbox for the user to see before they can select the "Save" button.
#The Save Button will create a text file that will be deleted after the entire process is complete.
#The saved text file will contain the Conditions and the conditions must be able to take (<>, >,<,=,>=,<=,|) as well as appropriate values.

# The process will then take the Criteria on the Text file and make a new sheet for each criteria within one excel sheet.
# The Process will then execute the Criteria as filters on the appropriate columns for each sheet.
# Once the Entire process is complete everything is saved in one excel file called "applied_criteria"
import pandas as pd
import os

def apply_criteria(file_path, criteria_file_path, output_path):
    with open(criteria_file_path, 'r') as f:
        criteria = f.readlines()
    
    df = pd.read_excel(file_path)
    writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
    
    for i, criterion in enumerate(criteria):
        column, condition = criterion.strip().split(' looking for ')
        df_filtered = df.query(f'{column} {condition}')
        df_filtered.to_excel(writer, sheet_name=f'Criteria_{i+1}', index=False)
    
    writer.save()
    os.remove(criteria_file_path)
    print(f"Applied criteria and saved to {output_path}")
