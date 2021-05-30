import json
with open('project_3_data.json') as f:
  player_data = json.load(f)
player_id=0
while player_id<len(player_data):
    
    temp_player_data=[]
    temp_player=[]
    years_to_remove=list()
    
    for years in range (len(player_data[player_id]['history'])):
      if (int((player_data[player_id]['history'][years]['date'].split( )[2]))>2012):
        if(years_to_remove==[]):
          years_to_remove=[years]
          
        else:
          years_to_remove+=[years]
        
    for i in range (len(player_data[player_id]['history'])):
      if i  in years_to_remove:

        temp_player_data.append(player_data[player_id]['history'][i].copy() ) 
    player_data[player_id]['history']=temp_player_data
    player_id+=1
player_id=0
while player_id<len(player_data):
  previous_year=0
  temp_player_data=[]
  
  for years in range (len(player_data[player_id]['history'])):

    
    
    year=int(player_data[player_id]['history'][years]['date'].split( )[2])
    
    if(year!=previous_year and previous_year!=0):   
      temp_player_data.append(player_data[player_id]['history'][years-1].copy()) 
    previous_year=year
    
  player_data[player_id]['history']=temp_player_data
  
  
  if(player_data[player_id]['name']=='Eden Hazard'):
    print(player_data[player_id]['history'])
  player_id+=1