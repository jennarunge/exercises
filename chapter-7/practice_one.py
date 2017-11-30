daily_sales = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ]
days_of_week = ["Sunday",
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday"]
                
for i in range(len(daily_sales)):
    day = days_of_week[i]
    phrase = "Enter the sales for " + day + ":"
    prompt = input(phrase)
    daily_sales[i] = prompt
print(daily_sales)