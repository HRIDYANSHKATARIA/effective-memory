from tkinter import *
import requests
import json

root=Tk()
root.title("My Country App")
root.geometry("350x300")


root.configure(background="white")
#Setting labels
capital_name_label=Label(root, text="Capital City Name",font=("Helvetica", 18,'bold'),bg="white")
capital_name_label.place(relx=0.28,rely=0.15,anchor=CENTER)

capital_entry=Entry(root)
capital_entry.place(relx=0.28,rely=0.35,anchor=CENTER)

country_info_label = Label(root,text="Country: ", bg="white", font=("bold", 10))
country_info_label.place(relx=0.22,rely=0.5,anchor=CENTER) 

region_info_label = Label(root,text="Region: ", bg="white", font=( "bold",10)) 
region_info_label.place(relx=0.22,rely=0.6,anchor=CENTER) 

language_info_label = Label(root,text="Language: ", bg="white", font=( "bold",10)) 
language_info_label.place(relx=0.22,rely=0.7,anchor=CENTER) 

population_info_label = Label(root,text="Population: ", bg="white", font=( "bold",10)) 
population_info_label.place(relx=0.22,rely=0.8,anchor=CENTER) 

area_info_label = Label(root,text="area: ", bg="white", font=( "bold",10)) 
area_info_label.place(relx=0.22,rely=0.9,anchor=CENTER) 



def city_name():
    api_request = requests.get("https://restcountries.com/v2/capital/"+capital_entry.get())
    api_output_json = json.loads(api_request.content)
    country_info = api_output_json[0]['name']
    print(country_info)
    region = api_output_json[0]['region']
    print(region)
    language = api_output_json[0]['languages']
    print(language)
    population =  api_output_json[0]['population']
    print(population)
    area =  api_output_json[0]['area']
    print(area)
    country_info_label["text"] = "Country: "+str(country_info)
    region_info_label["text"] = "Region: "+str(region)
    language_info_label["text"] = "Language: "+str(language)
    population_info_label["text"] = "Population: "+str(population)
    area_info_label["text"] = "Area: "+str(area)
    capital_name_label["text"] = capital_entry.get()
    capital_entry.destroy()
    search_btn.destroy()


search_btn = Button(root,text="City Details",command=city_name)
search_btn.place(relx=0.5,rely=0.48,anchor=CENTER)




root.mainloop()