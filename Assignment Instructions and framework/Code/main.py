import zipfile
import requests
import pandas as pd
URL = "https://storage.googleapis.com/kaggle-data-sets/9646/13736/compressed/penalty_data_set_2.csv.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20220928%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20220928T231208Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=2053554c58a3f39cd28a3ac07a7b659ced045cb4ad91d1e816060fc87bea748942b38d65eac7e1f1d1aa4bd7b89b99886859fec259a2fed55f65886879db75cb313b85e1f5bc56a4c175acf88c33cc9cce71b7cc9322aa23e8adafda21c62806ef68adc187bcc6ed2f0510af9333f77191ae3df2f00dd818be335f91cef68359e81cb7db38a362e1b4daa99eb97b2629951929b25191dbe6287b1957ee90b0f17a3bb00e383a1eb2986af3b96cdda48b7efb68e0d6f0348c28f883384be3994768330a009a41236167927f26a7a3f5bdc266a4704a5c3a6e9fc6847cdc0fab7e5e4fb6550ab464d497990e99ebd56f5b65629d538e5db144bd740438b4ef4eb8"
response = requests.get(URL)
open("penaltyData.zip", "wb").write(response.content)
with zipfile.ZipFile("penaltyData.zip", 'r') as zip_ref:
    zip_ref.extractall("")
df = pd.read_csv("penalty_data_set_2.csv", low_memory=False)

