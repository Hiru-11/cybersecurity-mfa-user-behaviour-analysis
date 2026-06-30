Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel(r"C:\Users\Owner\Downloads\Cleaned_Google_Security_Dataset.xlsx")
responses = df['Verification_Action'].dropna().str.lower()
themes = {
    'Careful Verification': responses.str.contains('check|careful|review|read'),
    'Automatic Approval': responses.str.contains('accept|approve|just accept|approve without'),
    'Suspicious Behaviour Awareness': responses.str.contains('deny|reject|not approve'),
    'Confusion/Fatigue': responses.str.contains('confused|annoyed|tired|multiple notifications')
}
theme_counts = {theme: condition.sum() for theme, condition in themes.items()}
theme_df = pd.DataFrame(list(theme_counts.items()), columns=['Theme', 'Count'])
plt.figure(figsize=(8,5))
<Figure size 800x500 with 0 Axes>
plt.bar(theme_df['Theme'], theme_df['Count'])
<BarContainer object of 4 artists>
plt.xlabel("Behavioural Themes")
Text(0.5, 0, 'Behavioural Themes')
plt.ylabel("Number of Responses")
Text(0, 0.5, 'Number of Responses')
plt.title("Behavioural Patterns in Verification Actions")
Text(0.5, 1.0, 'Behavioural Patterns in Verification Actions')
plt.xticks(rotation=10)
([0, 1, 2, 3], [Text(0, 0, 'Careful Verification'), Text(1, 0, 'Automatic Approval'), Text(2, 0, 'Suspicious Behaviour Awareness'), Text(3, 0, 'Confusion/Fatigue')])
plt.show()
print(theme_df)
                            Theme  Count
0            Careful Verification     30
1              Automatic Approval     20
2  Suspicious Behaviour Awareness      5
3               Confusion/Fatigue      1


responses = df['Suspicious_Login_Experience'].dropna().str.lower()
themes = {
    'Experienced Suspicious Activity': responses.str.contains('yes|experienced|approved|continuous notifications'),
    
    'No Experience but Security Aware': responses.str.contains('deny|secure my account|change my password'),
    
...     'Unsafe Approval Behaviour': responses.str.contains('approve them without checking|just approve|accidentally approved'),
...     
...     'No Experience': responses.str.contains('no|have not|haven’t experienced|nope')
... }
>>> theme_counts = {theme: condition.sum() for theme, condition in themes.items()}
>>> theme_df = pd.DataFrame(list(theme_counts.items()), columns=['Theme', 'Count'])
>>> plt.figure(figsize=(9,5))
<Figure size 900x500 with 0 Axes>
>>> plt.bar(theme_df['Theme'], theme_df['Count'])
<BarContainer object of 4 artists>
>>> plt.xlabel("Behavioural Themes")
Text(0.5, 0, 'Behavioural Themes')
>>> plt.ylabel("Number of Responses")
Text(0, 0.5, 'Number of Responses')
>>> plt.title("User Experiences with Suspicious Login Notifications")
Text(0.5, 1.0, 'User Experiences with Suspicious Login Notifications')
>>> plt.xticks(rotation=10)
... 
([0, 1, 2, 3], [Text(0, 0, 'Experienced Suspicious Activity'), Text(1, 0, 'No Experience but Security Aware'), Text(2, 0, 'Unsafe Approval Behaviour'), Text(3, 0, 'No Experience')])
>>> plt.show()
... 
>>> print(theme_df)
                              Theme  Count
0   Experienced Suspicious Activity     21
1  No Experience but Security Aware      1
2         Unsafe Approval Behaviour      5
3                     No Experience     45
