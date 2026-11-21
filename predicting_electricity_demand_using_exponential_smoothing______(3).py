import matplotlib.pyplot as plt # type: ignore
consumption = [120, 125, 130, 128, 135, 140, 138]

def calculate_exp_smooth(actual, previous_forecast, alpha):
    return previous_forecast + alpha * (actual - previous_forecast)

def calculate_forecast(consumption, alpha):

  forecast = [consumption[0]]
  for actual in consumption:

    forecast.append(
        calculate_exp_smooth(actual,forecast[-1], alpha)
    )

  return forecast

forecast_day1 = consumption[0]
forecast_day2 = calculate_exp_smooth(consumption[0], forecast_day1, 0.2)
forecast_day3 = calculate_exp_smooth(consumption[1], forecast_day2, 0.2)
forecast_day4 = calculate_exp_smooth(consumption[2], forecast_day3, 0.2)

print(f"Forecast for Day 1: {forecast_day1}")
print(f"Forecast for Day 2: {forecast_day2}")
print(f"Forecast for Day 3: {forecast_day3}")
print(f"Forecast for Day 4: {forecast_day4}")


def round_forecasts(forecasts, digits=2):
    return [round(f, digits) for f in forecasts]

def format_report(alpha, rounded):
    return f"alpha = {alpha} -> {rounded}"


def plot_forecasts(consumption):
    days = [f'Day {i+1}' for i in range(len(consumption) + 1)]

    forecast_02 = calculate_forecast(consumption, 0.2)
    forecast_04 = calculate_forecast(consumption, 0.4)
    forecast_08 = calculate_forecast(consumption, 0.8)

    plt.figure(figsize=(10, 6))

    plt.plot(days[:-1], consumption,
             marker='o', label='Actual Consumption')

    plt.plot(days, forecast_02,
             marker='s', linestyle='--', label='α = 0.2')

    plt.plot(days, forecast_04,
             marker='^', linestyle='--', label='α = 0.4')

    plt.plot(days, forecast_08,
             marker='x', linestyle='--', label='α = 0.8')

    plt.title('Actual Consumption vs Forecast')
    plt.xlabel('Days')
    plt.ylabel('Electricity Consumption')
    plt.legend()
    plt.grid(True)
    plt.show()


# Call the function
plot_forecasts(consumption)


def add_observation(consumption, new_observations):
    consumption.extend(new_observations)

    print(f"Successfully added {len(new_observations)} new observations!")
    print(f"Added values: {new_observations}")
    print(f"Total observations: {len(consumption)}")


add_observation(consumption, [141, 145])