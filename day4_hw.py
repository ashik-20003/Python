web_development = ["Ashik","Akash","Athul"]
data_science = ["Rahna","Surya","Zaida"]
ui_ux = ["Akthar","Adithyan","Varun"]
all_participants = [web_development,data_science,ui_ux]
web_development.append("Geetha")
print(web_development)
data_science.insert(1,"Sahadevan")
print(data_science)
ui_ux.pop()
print(ui_ux)
new_data_science = data_science.copy()
data_science.clear()
print(new_data_science)
print(web_development[:2])
name_len = [len(name) for name in new_data_science]
print(name_len)
if "asha" in all_participants:
    print("Yes, Asha is in the list")
else:
    print("No, Asha is not in the list")
first = (web_development[0],new_data_science[0],ui_ux[0])
print(first)

