elevated_limit = 5 #micrograms / deciliter
poison_limit = 40 #micrograms / deciliter
adult_blood_avg = 5 #liters
child_blood_avg = 2.6 #liters
M_pb = 207.2 # g/mol
adult_absorption_coef = 0.15
child_absorption_coef = 0.50

oregano_molar_mass = 150.217 #g/mol ## good approximation for all dried spices
oregano_density = 1.12 # g/ tsp
oregano_serving = 1 # tsp
oregano_serving_mols = (oregano_serving * oregano_density) / oregano_molar_mass

micrograms_per_gram = 10 ** 6
deciliters_per_liter = 10

def ppb_to_bll(ppb, mols_spice_consumed=oregano_serving_mols, adult_or_child='adult'):
    if adult_or_child == 'adult':
        liters_blood=adult_blood_avg 
        ab_coef=adult_absorption_coef
    elif adult_or_child == 'child':
        liters_blood=child_blood_avg 
        ab_coef=child_absorption_coef
    else: 
        raise ValueError('adult_or_child must be set to "adult" or "child"')
    percent = ppb / 10**9;
    mols_lead_consumed = percent * mols_spice_consumed
    grams_lead_consumed =  M_pb * mols_lead_consumed
    grams_lead_absorbed = ab_coef * grams_lead_consumed
    grams_per_liter = grams_lead_absorbed / liters_blood 
    micrograms_per_deciliter = micrograms_per_gram * grams_per_liter / deciliters_per_liter
    return micrograms_per_deciliter

def report(ppb, mols=oregano_serving_mols):
    """
    Amount of lead added to blood from single consumption
    """
    print(f"PPB lead: {ppb}")
    print(f"Adult level: {ppb_to_bll(ppb, mols_spice_consumed=mols, adult_or_child='adult'):.4f} microg/dL")
    print(f"Child level: {ppb_to_bll(ppb, mols_spice_consumed=mols, adult_or_child='child'):.4f} microg/dL")

if __name__ == "__main__":
    report(212)
    report(700)
    report(2000)
    report(146000)
    report(1090000, mols = 6 / 150)
