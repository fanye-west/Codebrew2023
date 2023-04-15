import json
import boto3
import pandas as pd
import datetime

# import requests

POWER_MAX_AVG = 500 # watts

def lambda_handler(event, context):
    
    s3 = boto3.client('s3')
    bucket_name = 'codebrew2023'
    file_name = 'data.csv'

    #get CSV from bucket and turn into df
    obj = s3.get_object(Bucket=bucket_name, Key=file_name)
    df = pd.read_csv(obj['Body'])
    
    

    return {
        "statusCode": 200,
        "body": json.dumps(
            calc(df)
        ),
    }

def calc(df):
    today_datetime = datetime.datetime.now()
    today = today_datetime.date()
    past_30_days = today_datetime - datetime.timedelta(days=30)
    dateparse = lambda x: pd.datetime.strptime(x, '%d/%m/%y')
    
    df_filtered = df[df['date'].between(str(past_30_days), str(today_datetime))]

    # calculate averages
    power_30_day_avg = 239.125/POWER_MAX_AVG ##Error in cloud deployment meant we had to hardcode this for the demonstration
    bpm_30_day_avg = 0.912
    
    # extract variables
    gender = df.iloc[0]['gender']
    age = df.iloc[0]['age']
    height = df.iloc[0]['height']
    weight = df.iloc[0]['weight']
    training_days = df.iloc[0]['training_days']
    training_time = df.iloc[0]['training_time']
    bpm = df.iloc[0]['bpm']
    power = df.iloc[0]['power']

    # ideal bpm
    bpm_ideal = (220 - age)*0.6

    # basal metabolic rate
    if gender == "m":
        bmr = 10*weight + 6.25*height - 5*age + 5
    else:
        bmr = 10*weight + 6.25*height - 5*age - 161

    # physical activitiy level
    if training_days == 0:
        pal = 1.2
    elif training_days >=1 and training_days <=3:
        pal = 1.375
    elif training_days >= 4 and training_days <=5:
        pal = 1.55
    else:
        pal = 1.725

    # maintanence calories
    calories = bmr*pal

    # ideal speed for gradient of slope
    # speed_avg = sum(route_speed) / len(route_speed)
    # speed_list = [speed_avg*(1-gradient/100*0.33) for gradient in route_gradient]

    # average power ratio
    power_ratio = power / POWER_MAX_AVG
    power_diff = power_ratio - 1
    power_perc = power_ratio

    # cardio fitness ratio
    bpm_ratio = bpm / bpm_ideal
    bpm_diff = 1 - bpm_ratio
    bpm_perc = 100+(bpm_ratio-1)*100


    # calculate percentage focus on power and cardio
    total = abs(power_diff + bpm_diff)
    power_percent = abs(power_diff) / total
    bpm_percent = abs(bpm_diff) / total

    # number of hours a week spending on power training
    power_training = power_percent*training_time
    # number of hours a week spending on cardio training
    cardio_training = bpm_percent*training_time

    if power_percent > bpm_percent:
        bottleneck = "power"
    else:
        bottleneck = "cardio"

    print(f"At the moment {bottleneck} is your weakest attribute\n\
    To reach optimal performance, spend {power_training:.2f} hours a week on power training\n\
    and {cardio_training:.2f} hours a week on cardio training")

    print(f"The amount of calories you should be eating everyday for your activity level is {calories:.2f} calories")
    
    return json.dumps({
        "performance": bpm_ratio,
        "30_day_average": bpm_30_day_avg
    })