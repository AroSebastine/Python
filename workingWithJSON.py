import json

with open("PEN999_Agreements_AgreementType_2019-02-20_091034.567178.json", "r") as read_file:
    AgreementTypes = json.load(read_file)
    
with open("PEN999_Agreements_Agreement_2019-02-20_091034.567178.json", "r") as read_file:
    Agreements = json.load(read_file)

for agreement in Agreements:
    for agreementType in AgreementTypes:
        if agreement["AgreementTypeId"] == agreementType["AgreementTypeId"]:
            agreement.update({"AgreementType" : agreementType["Description"]})            
            break
        
with open("oputput_json.json", "w") as write_file:
    json.dump(Agreements, write_file)            
        