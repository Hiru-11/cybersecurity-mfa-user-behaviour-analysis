Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import pandas as pd
import matplotlib.pyplot a
s plt
SyntaxError: unexpected indent
import matplotlib.pyplot as plt
impo
r
import seaborn as sns

sns.set(style="Whitegrid')
        
SyntaxError: unterminated string literal (detected at line 1)
sns.set(style="whitegrid")
        
df=pd.read_excel(r"C:\Users\Owner\Downloads\Cleaned_Google_Security_Dataset.xlsx")
        
print(df.head())
        
  Age_Group  ...                        Suspicious_Login_Experience
0     18–24  ...  Yes, I got a lot of login prompts at once, and...
1     18–24  ...  No, I haven’t experienced that. But if it happ...
2     25–34  ...  I usually approve them without checking becaus...
3     35–44  ...  Yes, I’ve experienced this. I got a notificati...
4     18–24  ...  I'm not sure.... I just approve the login atte...

[5 rows x 20 columns]

plt.figure(figsize=(6,5))
        
<Figure size 600x500 with 0 Axes>
sns.countplot(
    x='Aware_MFA_Fatigue',
    data=df
)
plt.title('Awareness of MFA Fatigue Attacks')
        
Text(0.5, 1.0, 'Awareness of MFA Fatigue Attacks')
plt.xlabel('Awareness')

Text(0.5, 0, 'Awareness')
plt.ylabel('Number of Respondents')
        
Text(0, 0.5, 'Number of Respondents')
plt.show()
        


Aware_MFA_Fatigue
        
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    Aware_MFA_Fatigue
NameError: name 'Aware_MFA_Fatigue' is not defined
plt.figure(figsize=(6,5))
        
<Figure size 600x500 with 0 Axes>
sns.countplot(
    x='Aware_MFA_Fatigue',
    data=df
  )
        
<Axes: xlabel='Aware_MFA_Fatigue', ylabel='count'>
plt.title('Awareness of MFA Fatigue Attacks')
        
Text(0.5, 1.0, 'Awareness of MFA Fatigue Attacks')
plt.xlabel('Awareness')
        
Text(0.5, 0, 'Awareness')
plt.ylabel('Number of Respondents')
        
Text(0, 0.5, 'Number of Respondents')
plt.show()
        
order = [
    'Strongly Disagree',
    'Disagree',
    'Neutral',
    'Agree',
    'Strongly Agree'
]
        
plt.figure(figsize=(8,5))
        
<Figure size 800x500 with 0 Axes>
sns.countplot(
    x='Agreement_Fatigue',
    data=df,
    order=order
)

<Axes: xlabel='Agreement_Fatigue', ylabel='count'>
plt.title('User Agreement on MFA Fatigue Risk')
        
Text(0.5, 1.0, 'User Agreement on MFA Fatigue Risk')
plt.xlabel('Level of Agreement')
        
Text(0.5, 0, 'Level of Agreement')
plt.ylabel('Number of Respondents')
        
Text(0, 0.5, 'Number of Respondents')
plt.xticks(rotation=10)
        
([0, 1, 2, 3, 4], [Text(0, 0, 'Strongly Disagree'), Text(1, 0, 'Disagree'), Text(2, 0, 'Neutral'), Text(3, 0, 'Agree'), Text(4, 0, 'Strongly Agree')])
plt.show()
        
counts = df['Suspicious_Login_Notification'].value_counts()
        
plt.figure(figsize=(6,6))
        
<Figure size 600x600 with 0 Axes>
plt.pie(
    counts,
    labels=counts.index,
    autopct='%1.1f%%'
... )
...         
([<matplotlib.patches.Wedge object at 0x000001DB208DECF0>, <matplotlib.patches.Wedge object at 0x000001DB20911A90>, <matplotlib.patches.Wedge object at 0x000001DB20911E50>], [Text(-0.05397451174995693, 1.0986749983873092, 'No'), Text(-0.26727791023115616, -1.0670344505696459, 'Yes'), Text(1.0526344629629776, -0.3193128362321875, 'Not sure')], [Text(-0.02944064277270378, 0.5992772718476231, '51.6%'), Text(-0.14578795103517608, -0.5820187912198068, '39.1%'), Text(0.5741642525252605, -0.17417063794482954, '9.4%')])
>>> plt.title('Experience with Suspicious Login Notifications')
...         
Text(0.5, 1.0, 'Experience with Suspicious Login Notifications')
>>> plt.show()
...         
>>> mechanism_df = (
...     df['Security_Mechanisms']
...     .dropna()
...     .str.split(',')
...     .explode()
...     .str.strip()
...     .value_counts()
...     .reset_index()
... )
...         
>>> mechanism_df.columns = ['Mechanism', 'Count']
...         
>>> sns.barplot(data=mechanism_df, x='Mechanism', y='Count')
...         
<Axes: xlabel='Mechanism', ylabel='Count'>
>>> plt.title('Awareness of Authentication Security Mechanisms')
...         
Text(0.5, 1.0, 'Awareness of Authentication Security Mechanisms')
>>> plt.xticks(rotation=20)
...         
([0, 1, 2, 3], [Text(0, 0, 'SMS verification codes'), Text(1, 0, 'Passkeys'), Text(2, 0, 'Google Authenticator'), Text(3, 0, 'Security Keys (FIDO2)')])
>>> plt.show()
...         
