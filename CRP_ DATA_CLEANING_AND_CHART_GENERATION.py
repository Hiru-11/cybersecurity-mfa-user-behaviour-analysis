Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Load Data
df=pd.read_excel(r"C:\Users\Owner\Downloads\Cybersecurity Threats and Mitigation Strategies in Google Accounts_ Analysis of User Behaviour and System Defense form (Responses).xlsx")
print(df.head())
  What is your age group?    ... Have you ever experienced a suspicious login attempt or accidentally approved a prompt you didn't start? If so, please briefly explain.  
0                     18–24  ...  Yes, I got a lot of login prompts at once, and...                                                                                       
1                     18–24  ...  No, I haven’t experienced that. But if it happ...                                                                                       
2                     25–34  ...  I usually approve them without checking becaus...                                                                                       
3                     35–44  ...  Yes, I’ve experienced this. I got a notificati...                                                                                       
4                     18–24  ...  I'm not sure.... I just approve the login atte...                                                                                       

[5 rows x 20 columns]

#Display the column names
print(df.columns)
Index(['What is your age group?  ',
       'What is your highest level of education?  ',
       'Do you currently work or study in the IT or Cybersecurity field?',
       '  What do you primarily use your Google Account for?  (Select all that apply)',
       'Do you have any formal training in Information Technology or Cybersecurity?',
       'How frequently do you use your Google Account?',
       'Which Google services do you regularly use? (Select all that apply)',
       'Were you aware that a single Google Account provides access to multiple Google services?',
       'Have you enabled Two-Step Verification (MFA) on your Google Account?',
       'What Authentication Method do you commonly use? ',
       'How often do you receive Google login verification notifications?',
       'When you receive a login verification prompt, how often do you check details such as device, location, or time?',
       'Have you ever received a login notification for a login attempt that you did NOT initiate?',
       'If you receive multiple authentication notifications repeatedly, what would you most likely do?',
       'To what extent do you agree with the statement: 'Repeated login notifications can cause users to approve requests without carefully verifying them.'',
       'Before this survey, were you aware of MFA Fatigue attacks?',
       'Do you believe user behaviour plays an important role in the effectiveness of authentication systems? ',
       'Are you aware of the following authentication security mechanisms? (Select all that apply)',
       'What do you usually do when you receive a login verification notification?  ',
       'Have you ever experienced a suspicious login attempt or accidentally approved a prompt you didn't start? If so, please briefly explain.  '],
      dtype='str')

#Rename the column to shorter headings
      
df.columns = [
    'Age_Group',
    'Education_Level',
    'IT_Background',
    'Primary_Use',
    'Formal_Training',
    'Usage_Frequency',
    'Google_Services',
    'Aware_Single_Access',
    'MFA_Enabled',
    'Authentication_Method',
    'Login_Notifications',
    'Check_Login_Details',
    'Suspicious_Login_Notification',
    'Repeated_Notification_Response',
    'Agreement_Fatigue',
    'Aware_MFA_Fatigue',
    'Behaviour_Importance',
    'Security_Mechanisms',
    'Verification_Action',
    'Suspicious_Login_Experience'
]
      
print(df.columns)
      
Index(['Age_Group', 'Education_Level', 'IT_Background', 'Primary_Use',
       'Formal_Training', 'Usage_Frequency', 'Google_Services',
       'Aware_Single_Access', 'MFA_Enabled', 'Authentication_Method',
       'Login_Notifications', 'Check_Login_Details',
       'Suspicious_Login_Notification', 'Repeated_Notification_Response',
       'Agreement_Fatigue', 'Aware_MFA_Fatigue', 'Behaviour_Importance',
       'Security_Mechanisms', 'Verification_Action',
       'Suspicious_Login_Experience'],
      dtype='str')

#check for missing values
      
print(df.isnull().sum())
      
Age_Group                         0
Education_Level                   0
IT_Background                     0
Primary_Use                       0
Formal_Training                   0
Usage_Frequency                   0
Google_Services                   0
Aware_Single_Access               0
MFA_Enabled                       0
Authentication_Method             0
Login_Notifications               0
Check_Login_Details               0
Suspicious_Login_Notification     0
Repeated_Notification_Response    0
Agreement_Fatigue                 0
Aware_MFA_Fatigue                 0
Behaviour_Importance              0
Security_Mechanisms               0
Verification_Action               0
Suspicious_Login_Experience       1
dtype: int64

#Filling the missing values in text response
      
df['Suspicious_Login_Experience'] = df['Suspicious_Login_Experience'].fillna('No Response')
      
print(df.isnull().sum())
      
Age_Group                         0
Education_Level                   0
IT_Background                     0
Primary_Use                       0
Formal_Training                   0
Usage_Frequency                   0
Google_Services                   0
Aware_Single_Access               0
MFA_Enabled                       0
Authentication_Method             0
Login_Notifications               0
Check_Login_Details               0
Suspicious_Login_Notification     0
Repeated_Notification_Response    0
Agreement_Fatigue                 0
Aware_MFA_Fatigue                 0
Behaviour_Importance              0
Security_Mechanisms               0
Verification_Action               0
Suspicious_Login_Experience       0
dtype: int64

#Remove Duplicates
      
df = df.drop_duplicates()
      
print("Duplicates removed successfully")
      
Duplicates removed successfully
print(df.info())
      
<class 'pandas.DataFrame'>
RangeIndex: 64 entries, 0 to 63
Data columns (total 20 columns):
 #   Column                          Non-Null Count  Dtype
---  ------                          --------------  -----
 0   Age_Group                       64 non-null     str  
 1   Education_Level                 64 non-null     str  
 2   IT_Background                   64 non-null     str  
 3   Primary_Use                     64 non-null     str  
 4   Formal_Training                 64 non-null     str  
 5   Usage_Frequency                 64 non-null     str  
 6   Google_Services                 64 non-null     str  
 7   Aware_Single_Access             64 non-null     str  
 8   MFA_Enabled                     64 non-null     str  
 9   Authentication_Method           64 non-null     str  
 10  Login_Notifications             64 non-null     str  
 11  Check_Login_Details             64 non-null     str  
 12  Suspicious_Login_Notification   64 non-null     str  
 13  Repeated_Notification_Response  64 non-null     str  
 14  Agreement_Fatigue               64 non-null     str  
 15  Aware_MFA_Fatigue               64 non-null     str  
 16  Behaviour_Importance            64 non-null     str  
 17  Security_Mechanisms             64 non-null     str  
 18  Verification_Action             64 non-null     str  
 19  Suspicious_Login_Experience     64 non-null     str  
dtypes: str(20)
memory usage: 10.1 KB
None

#Saving the cleaned data
      
df.to_excel("Cleaned_Google_Security_Dataset.xlsx", index=False)
      
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    df.to_excel("Cleaned_Google_Security_Dataset.xlsx", index=False)
  File "C:\Users\Owner\AppData\Roaming\Python\Python314\site-packages\pandas\core\generic.py", line 2312, in to_excel
    formatter.write(
  File "C:\Users\Owner\AppData\Roaming\Python\Python314\site-packages\pandas\io\formats\excel.py", line 1003, in write
    writer = ExcelWriter(
  File "C:\Users\Owner\AppData\Roaming\Python\Python314\site-packages\pandas\io\excel\_openpyxl.py", line 62, in __init__
    super().__init__(
  File "C:\Users\Owner\AppData\Roaming\Python\Python314\site-packages\pandas\io\excel\_base.py", line 1281, in __init__
    self._handles = get_handle(
  File "C:\Users\Owner\AppData\Roaming\Python\Python314\site-packages\pandas\io\common.py", line 935, in get_handle
    handle = open(handle, ioargs.mode)
PermissionError: [Errno 13] Permission denied: 'Cleaned_Google_Security_Dataset.xlsx'
df.to_excel(r"C:\Users\Owner\Downloads\Cleaned_Google_Security_Dataset.xlsx", index=False)
  
#For better chart sze and style
  
plt.style.use('ggplot')
  
#RESPONDENT AGE DISTRIBUTION
  
#Counting the age groups
  
age_counts = df['Age_Group'].value_counts()
  
print(age_counts)
  
Age_Group
18–24    42
25–34    13
55+       4
35–44     3
45–54     2
Name: count, dtype: int64

#Generating the Chart for Age Distribution- A bar chart
  
plt.figure(figsize=(8,5))
  
<Figure size 800x500 with 0 Axes>
bars = age_counts.plot(kind='bar')
  
plt.title('Respondent Age Distribution', fontsize=14)
  
Text(0.5, 1.0, 'Respondent Age Distribution')
plt.xlabel('Age Groups', fontsize=12)
  
Text(0.5, 0, 'Age Groups')
plt.ylabel('Number of Respondents', fontsize=12)
  
Text(0, 0.5, 'Number of Respondents')
plt.xticks(rotation=0)
  
(array([0, 1, 2, 3, 4]), [Text(0, 0, '18–24'), Text(1, 0, '25–34'), Text(2, 0, '55+'), Text(3, 0, '35–44'), Text(4, 0, '45–54')])

plt.show()
  
#IT/Cybesecurity Background Vs Non IT
  
it_counts = df['IT_Background'].value_counts()
  
print(it_counts)
  
IT_Background
No     37
Yes    27
Name: count, dtype: int64
#Generating a pie chart for the IT/CYbersecurity Vs Non-IT
  
plt.figure(figsize=(7,7))
  
<Figure size 700x700 with 0 Axes>
plt.pie(
    it_counts,
     labels=it_counts.index
    )
  
([<matplotlib.patches.Wedge object at 0x00000211813446E0>, <matplotlib.patches.Wedge object at 0x000002118135C050>], [Text(-0.26727822399779944, 1.067034371975234, 'No'), Text(0.2672784444813143, -1.0670343167469587, 'Yes')])
plt.title('IT/Cybersecurity Background vs Non-IT')
  
Text(0.5, 1.0, 'IT/Cybersecurity Background vs Non-IT')
plt.show()
  
#Highest Educational Level
  
education_counts = df['Education_Level'].value_counts()
  
print(education_counts)
  
Education_Level
Undergraduate Student (Currently pursuing a Bachelor's Degree)    22
Secondary Education (O/L or A/L)                                  19
Bachelor’s Degree (Graduated/Completed)                           12
Professional Qualification (e.g., CIMA, ACCA, BCS)                 8
Postgraduate Degree (Completed Master’s/PhD)                       2
Postgraduate Student (Currently pursuing Master's/PhD)             1
Name: count, dtype: int64

#Generating a Bar chart
                      
plt.figure(figsize=(10,6))
                      
<Figure size 1000x600 with 0 Axes>
bars = education_counts.plot(kind='barh')
                      
plt.title('Highest Education Level', fontsize=14)
                      
Text(0.5, 1.0, 'Highest Education Level')
plt.xlabel('Number of Respondents', fontsize=12)
                      
Text(0.5, 0, 'Number of Respondents')
plt.ylabel('Education Level', fontsize=12)
                      
Text(0, 0.5, 'Education Level')
plt.show()
                      
#Generating the same Bar Chart because the text is not being displayed
                      
plt.figure(figsize=(10,6))
                      
<Figure size 1000x600 with 0 Axes>
bars = education_counts.plot(kind='barh')
                      
plt.title('Highest Education Level', fontsize=14)
                      
Text(0.5, 1.0, 'Highest Education Level')
plt.xlabel('Number of Respondents', fontsize=12)
                      
Text(0.5, 0, 'Number of Respondents')
plt.ylabel('Education Level', fontsize=12)
                      
Text(0, 0.5, 'Education Level')
plt.tight_layout()
                      
plt.show()
                      
#Google Service Usage
                      
#Splitting the Responses based on the usage
                      
ervices = df['Google_Services'].str.split(', ')
                      
services = df['Google_Services'].str.split(', ')
                      
all_services = []
                      
for item in services:
                all_services.extend(item)
            service_counts = pd.Series(all_services).value_counts()
                      
SyntaxError: unindent does not match any outer indentation level
for item in services:
                all_services.extend(item)
            service_counts = pd.Series(all_services).value_counts()
                      
SyntaxError: unindent does not match any outer indentation level
for item in services:
        all_services.extend(item)
 service_counts = pd.Series(all_services).value_counts()
                      
SyntaxError: unindent does not match any outer indentation level
for item in services:
      all_services.extend(item)

                      
service_counts = pd.Series(all_services).value_counts()
                      
print(service_counts)
                      
Gmail                            56
YouTube                          54
Google Drive                     41
Google Photos                    25
Google Docs / Sheets / Slides    21
Google Pay                       21
Other                             7
Name: count, dtype: int64

#Generating the Graph
                      
service_counts = service_counts.sort_values(ascending=False)
                      
plt.figure(figsize=(12,6))

<Figure size 1200x600 with 0 Axes>
bars = service_counts.plot(kind='bar')
                      
plt.title('Google Services Usage', fontsize=14)
                      
Text(0.5, 1.0, 'Google Services Usage')
plt.xlabel('Google Services', fontsize=12)
                      
Text(0.5, 0, 'Google Services')
plt.ylabel('Frequency', fontsize=12)
                      
Text(0, 0.5, 'Frequency')
plt.xticks(rotation=45)

(array([0, 1, 2, 3, 4, 5, 6]), [Text(0, 0, 'Gmail'), Text(1, 0, 'YouTube'), Text(2, 0, 'Google Drive'), Text(3, 0, 'Google Photos'), Text(4, 0, 'Google Docs / Sheets / Slides'), Text(5, 0, 'Google Pay'), Text(6, 0, 'Other')])
plt.tight_layout()
                      
plt.show()
                      
#Authentication Methods
                      
mfa_counts = df['Authentication_Method'].value_counts()
                      
print(mfa_counts)
                      
Authentication_Method
Google Prompt (The "Yes/No" notification on your phone)                               32
SMS Verification Code (A 6-digit code sent via text message)                          18
Passkey (Using your phone's fingerprint, face ID, or screen lock)                      9
Not Sure                                                                               3
Authenticator App (Generating a code in an app like Google Authenticator or Authy)     2
Name: count, dtype: int64
#Gnereta the Bar Chart
         
plt.figure(figsize=(8,5))

<Figure size 800x500 with 0 Axes>
plt.bar(mfa_counts.index, mfa_counts.values)
         
<BarContainer object of 5 artists>
plt.title('Commonly Used Authentication Methods')
         
Text(0.5, 1.0, 'Commonly Used Authentication Methods')
plt.xlabel('Authentication Method')
         
Text(0.5, 0, 'Authentication Method')
plt.ylabel('Count')
         
Text(0, 0.5, 'Count')
plt.xticks(rotation=45)
         
([0, 1, 2, 3, 4], [Text(0, 0, 'Google Prompt (The "Yes/No" notification on your phone)'), Text(1, 0, 'SMS Verification Code (A 6-digit code sent via text message)'), Text(2, 0, "Passkey (Using your phone's fingerprint, face ID, or screen lock)"), Text(3, 0, 'Not Sure'), Text(4, 0, 'Authenticator App (Generating a code in an app like Google Authenticator or Authy)')])
plt.tight_layout()
         

Warning (from warnings module):
  File "<pyshell#118>", line 1
UserWarning: Tight layout not applied. The bottom and top margins cannot be made large enough to accommodate all Axes decorations.
plt.show()
         
plt.figure(figsize=(10,6))
         
<Figure size 1000x600 with 0 Axes>
plt.bar(mfa_counts.index, mfa_counts.values)
         
<BarContainer object of 5 artists>
plt.title('Commonly Used Authentication Methods')
         
Text(0.5, 1.0, 'Commonly Used Authentication Methods')
plt.xlabel('Authentication Method')
         
Text(0.5, 0, 'Authentication Method')
plt.ylabel('Count')
         
Text(0, 0.5, 'Count')
plt.tight_layout()
         
plt.show()
         
#Error in Graph
         
plt.figure(figsize=(10,6))
         
<Figure size 1000x600 with 0 Axes>
plt.bar(mfa_counts.index, mfa_counts.values)
         
<BarContainer object of 5 artists>
plt.title('Commonly Used Authentication Methods')
         
Text(0.5, 1.0, 'Commonly Used Authentication Methods')
plt.xlabel('Authentication Method')
         
Text(0.5, 0, 'Authentication Method')
plt.ylabel('Count')
         
Text(0, 0.5, 'Count')
plt.xticks(rotation=45)
         
([0, 1, 2, 3, 4], [Text(0, 0, 'Google Prompt (The "Yes/No" notification on your phone)'), Text(1, 0, 'SMS Verification Code (A 6-digit code sent via text message)'), Text(2, 0, "Passkey (Using your phone's fingerprint, face ID, or screen lock)"), Text(3, 0, 'Not Sure'), Text(4, 0, 'Authenticator App (Generating a code in an app like Google Authenticator or Authy)')])
plt.tight_layout()
         
plt.show()
         

#Error in Chart - Diifcult to read the output
         
#Generating a pie chart instead
         
plt.figure(figsize=(7,7))

<Figure size 700x700 with 0 Axes>
plt.pie(
   mfa_counts,
   labels=mfa_counts.index,
   autopct='%1.1f%%',
   )
         
([<matplotlib.patches.Wedge object at 0x0000021182EB4A50>, <matplotlib.patches.Wedge object at 0x0000021182EB4E10>, <matplotlib.patches.Wedge object at 0x0000021182EB51D0>, <matplotlib.patches.Wedge object at 0x0000021182EB5590>, <matplotlib.patches.Wedge object at 0x0000021182EB5950>], [Text(-4.8082529002048655e-08, 1.099999999999999, 'Google Prompt (The "Yes/No" notification on your phone)'), Text(-0.69783263770722, -0.8503114780776417, 'SMS Verification Code (A 6-digit code sent via text message)'), Text(0.6552691591337401, -0.8835283408517021, "Passkey (Using your phone's fingerprint, face ID, or screen lock)"), Text(1.0356985288104086, -0.3705786791222014, 'Not Sure'), Text(1.0947032395858842, -0.1078184457324934, 'Authenticator App (Generating a code in an app like Google Authenticator or Authy)')], [Text(-2.6226834001117445e-08, 0.5999999999999994, '50.0%'), Text(-0.3806359842039381, -0.4638062607696227, '28.1%'), Text(0.35741954134567633, -0.4819245495554738, '14.1%'), Text(0.5649264702602228, -0.2021338249757462, '4.7%'), Text(0.5971108579559368, -0.058810061308632755, '3.1%')])
plt.title('Commonly Used Authentication Methods')
         
Text(0.5, 1.0, 'Commonly Used Authentication Methods')
plt.savefig('Authentication_Methods_Pie.png')
         
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    plt.savefig('Authentication_Methods_Pie.png')
  File "C:\Users\Owner\AppData\Roaming\Python\Python314\site-packages\matplotlib\pyplot.py", line 1250, in savefig
    res = fig.savefig(*args, **kwargs)  # type: ignore[func-returns-value]
  File "C:\Users\Owner\AppData\Roaming\Python\Python314\site-packages\matplotlib\figure.py", line 3490, in savefig
    self.canvas.print_figure(fname, **kwargs)
  File "C:\Users\Owner\AppData\Roaming\Python\Python314\site-packages\matplotlib\backend_bases.py", line 2186, in print_figure
    result = print_method(
  File "C:\Users\Owner\AppData\Roaming\Python\Python314\site-packages\matplotlib\backend_bases.py", line 2042, in <lambda>
    print_method = functools.wraps(meth)(lambda *args, **kwargs: meth(
  File "C:\Users\Owner\AppData\Roaming\Python\Python314\site-packages\matplotlib\backends\backend_agg.py", line 481, in print_png
    self._print_pil(filename_or_obj, "png", pil_kwargs, metadata)
  File "C:\Users\Owner\AppData\Roaming\Python\Python314\site-packages\matplotlib\backends\backend_agg.py", line 430, in _print_pil
    mpl.image.imsave(
  File "C:\Users\Owner\AppData\Roaming\Python\Python314\site-packages\matplotlib\image.py", line 1657, in imsave
    image.save(fname, **pil_kwargs)
  File "C:\Users\Owner\AppData\Roaming\Python\Python314\site-packages\PIL\Image.py", line 2708, in save
    fp = builtins.open(filename, "w+b")
PermissionError: [Errno 13] Permission denied: 'Authentication_Methods_Pie.png'
plt.show()
  
#Vulnerability and Fatigue
  
plt.figure(figsize=(8,5))
  
<Figure size 800x500 with 0 Axes>
sns.heatmap(usage_vs_vigilance, annot=True, fmt='d', cmap='Blues')
  
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    sns.heatmap(usage_vs_vigilance, annot=True, fmt='d', cmap='Blues')
NameError: name 'usage_vs_vigilance' is not defined


usage_vs_vigilance = pd.crosstab(
    df['Usage_Frequency'],
    df['Check_Login_Details']
)
  
plt.figure(figsize=(8,5))
  
<Figure size 800x500 with 0 Axes>
sns.heatmap(
    usage_vs_vigilance,
    annot=True,
    fmt='d',
    cmap='Blues'
)
  
<Axes: xlabel='Check_Login_Details', ylabel='Usage_Frequency'>
plt.title('Usage Frequency vs Vigilance')
  
Text(0.5, 1.0, 'Usage Frequency vs Vigilance')
plt.xlabel('Check Login Details')
  
Text(0.5, 25.722222222222214, 'Check Login Details')
plt.ylabel('Usage Frequency')
  
Text(70.7222222222222, 0.5, 'Usage Frequency')
plt.tight_layout()
  
plt.show()
  
#Bar Chart for MFA Fatigue Response
  
fatigue_counts = df['Repeated_Notification_Response'].value_counts()
  
print(fatigue_counts)
  
Repeated_Notification_Response
Change my password immediately                   24
Approve one request to stop the notifications    15
Carefully review each request                    15
Ignore the notifications                         10
Name: count, dtype: int64
plt.figure(figsize=(12,6))
  
<Figure size 1200x600 with 0 Axes>
bars = fatigue_counts.plot(kind='bar')
  
plt.title('MFA Fatigue Response', fontsize=14)
  
Text(0.5, 1.0, 'MFA Fatigue Response')
plt.xlabel('User Response', fontsize=12)
  
Text(0.5, 0, 'User Response')
plt.ylabel('Number of Respondents', fontsize=12)
  
Text(0, 0.5, 'Number of Respondents')
plt.xticks(rotation=15)
  
(array([0, 1, 2, 3]), [Text(0, 0, 'Change my password immediately'), Text(1, 0, 'Approve one request to stop the notifications'), Text(2, 0, 'Carefully review each request'), Text(3, 0, 'Ignore the notifications')])
plt.tight_layout()
  
plt.show()
...   
>>> #Awarness Gap
...   
>>> awareness_gap = pd.crosstab(
...      df['Aware_MFA_Fatigue'],
...     df['Agreement_Fatigue']
... )
...   
>>> print(awareness_gap)
...   
Agreement_Fatigue  Agree  Disagree  Neutral  Strongly Agree  Strongly Disagree
Aware_MFA_Fatigue                                                             
No                    15         1       14              18                  1
Yes                    3         3        2               6                  1
>>> awareness_gap.plot(
...     kind='bar',
...     figsize=(12,6)
... )
...   
<Axes: xlabel='Aware_MFA_Fatigue'>
>>> plt.title('Awareness Gap: Knowledge vs Agreement', fontsize=14)
...   
Text(0.5, 1.0, 'Awareness Gap: Knowledge vs Agreement')
>>> plt.xlabel('Awareness of MFA Fatigue', fontsize=12)
...   
Text(0.5, 0, 'Awareness of MFA Fatigue')
>>> plt.ylabel('Number of Respondents', fontsize=12)
...   
Text(0, 0.5, 'Number of Respondents')
>>> plt.xticks(rotation=0)
...   
(array([0, 1]), [Text(0, 0, 'No'), Text(1, 0, 'Yes')])
>>> plt.tight_layout()
...   
>>> plt.show()
...   
