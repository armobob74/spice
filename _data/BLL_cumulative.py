from BLL_single import oregano_serving_mols, ppb_to_bll

half_life = (28 + 36) / 2 #days (half life of lead in blood of adults)

typical_daily_consumption = oregano_serving_mols
ppb = 2012 #50th percentile

typical_daily_increase = ppb_to_bll(ppb, mols_spice_consumed=typical_daily_consumption)

def cumulative_bll(days):
    total_bll = 0
    daily_decay_factor = 0.5 ** (1 / half_life)

    for day in range(days):
        total_bll = total_bll * daily_decay_factor + typical_daily_increase
    return total_bll

if __name__ == "__main__":
    print(f"Cumulative BLL after 30 days: {cumulative_bll(30)}")
    print(f"Cumulative BLL after 90 days: {cumulative_bll(90)}")
    print(f"Cumulative BLL after 365 days: {cumulative_bll(365)}")
