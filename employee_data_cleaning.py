def clean_data(data):
    for row in data:
        # Standardize gender
        if row['Gender']:
            row['Gender'] = row['Gender'].strip().capitalize()
        
        # Fill missing salary with 0
        if not row['Salary'] or row['Salary'] == 'N/A':
            row['Salary'] = 0
        else:
            row['Salary'] = int(row['Salary'])
        
        # Standardize department capitalization
        if row['Department']:
            row['Department'] = row['Department'].capitalize()
        
        # Handle missing email
        if not row['Email']:
            row['Email'] = "unknown@company.com"
    
    return data