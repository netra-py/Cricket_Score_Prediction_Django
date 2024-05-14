from django.shortcuts import render
from .models import team_data,venue_data
import pickle
import pandas as pd
import requests



# Create your views here.
def index(request):
    return render(request,'navs.html')


def score_prediction_page(request):
    teams = team_data.objects.values()
    venues = venue_data.objects.values()
     
    


    if request.method == "POST":
        venue = request.POST.get('ven')
        bat_team = request.POST.get('bat-team')
        bowl_team = request.POST.get('bowl-team')
        curr_score = request.POST.get('c-score')
        curr_score = int(curr_score)
        ball_left = request.POST.get('b-left')
        wick_left = request.POST.get('w-left')
        last5_score = request.POST.get('5-score')
        
        
        test1 = pd.DataFrame()
        test1['venue'] = [venue]
        test1['batting_team'] = [bat_team]
        test1['bowling_team'] = [bowl_team]
        test1['cum_runs'] = [curr_score]
        test1['balls_left'] = [ball_left]
        test1['wickets_left'] = [wick_left]
        test1['last_five'] = [last5_score]
        


        def load_pickle_from_github(owner, repo, path):
            url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
            headers = {"Accept": "application/vnd.github.v3.raw"}

            try:
                response = requests.get(url, headers=headers)
                response.raise_for_status()
                content = response.content
                return pickle.loads(content)
            except requests.exceptions.RequestException as e:
                print(f"Error fetching pickle file: {e}")
                return None
            except pickle.UnpicklingError as e:
                print(f"Error unpickling file content: {e}")
                return None

        # Replace these with your GitHub repository details and pickle file path
        owner = "netra-py"
        repo = "Cricket_Score_Prediction_Model"
        path = "model.pkl"
        pickled_model = load_pickle_from_github(owner,repo,path)

        pred_runs = pickled_model.predict(test1)
        final_score = round((test1['cum_runs']+pred_runs).values[0],0)
        
        
        return render(request, 'winner_prediction.html',{'allowed':'yes','teams':teams,'venues':venues,'final_score':final_score})

    else:
        return render(request,'index.html',{'allowed':'no','teams':teams,'venues':venues})



    
    
    # context = {'teams':teams,'venues':venues,'final_score':final_score}

    # return render(request,'score_prediction.html',context=context)

def winner_prediction_page(request):
    return render(request, 'winner_prediction.html')
